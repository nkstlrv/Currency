import time
import random
import csv
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://auto.ria.com/uk/search/"


def get_page(url: str, page: int, page_size: int = 100) -> str:
    query_parameters = {
        "indexName": "auto,order_auto,newauto_search",
        "categories.main.id": "1",
        "brand.id[0]": "59",
        "country.import.usa.not": "-1",
        "price.currency": "1",
        "abroad.not": "0",
        "custom.not": "1",
        "page": str(page),
        "size": str(page_size),
    }

    response = requests.get(url=url, params=query_parameters)
    response.raise_for_status()
    page_html = response.text
    return page_html


def get_card_detailed_page(car_url: str) -> str:
    response = requests.get(f"https://auto.ria.com/uk{car_url}")
    response.raise_for_status()
    return response.text


def get_car_detailed_data(page_html: str) -> dict:
    result = dict()
    soup = BeautifulSoup(page_html, "html.parser")

    result["car_price"] = soup.find("div", {"class", "price_value"}).find("strong").text
    result["car_description"] = soup.find("div", {"class", "full-description"}).text

    additional_data = soup.find("div", {"class", "box-panel description-car"}).find_all("dd")
    for item in additional_data:
        if item.find("span") is not None:
            if "Пробіг" in item.text:
                result["car_run"] = item.find("span", {"class": "argument"}).text
            elif "Двигун" in item.text:
                result["car_engine"] = item.find("span", {"class": "argument"}).text
            elif "Колір" in item.text:
                result["car_color"] = item.find("span", {"class": "argument"}).text
            elif "Привід" in item.text:
                result["car_drive"] = item.find("span", {"class": "argument"}).text
            elif "Коробка передач" in item.text:
                result["car_gearbox"] = item.find("span", {"class": "argument"}).text
            elif "Технічний стан" in item.text:
                result["car_condition"] = item.find("span", {"class": "argument"}).text
    return result




class CSVWriter:
    def __init__(self, filename, headers):
        self.filename = filename

        with open(filename, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

    def write(self, data):
        with open(self.filename, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data)


class StdOutWriter:
    @staticmethod
    def write(data):
        print(data)


def main() -> None:
    current_page = 0
    unique_cars = set()

    csv_headers = ["car_id", "car_manufacturer", "car_model", "car_year", "car_modification", "link_to_page"]
    writers = (
        CSVWriter('cars.csv', csv_headers),
        StdOutWriter(),
    )

    while True:
        time.sleep(random.randint(1, 3))

        print(f"PAGE: {current_page+1}")

        page_html = get_page(BASE_URL, page=current_page)
        soup = BeautifulSoup(page_html, "html.parser")

        search_content = soup.find("div", {"id": "searchResults"})
        content = search_content.find_all("section", {"class": "ticket-item"})

        current_page += 1

        if not content:
            break

        for item in content:
            car_details = item.find("div", {"class": "hide"})
            car_id = car_details["data-id"]
            link_to_page = car_details["data-link-to-view"]
            car_manufacturer = car_details["data-mark-name"]
            car_model = car_details["data-model-name"]
            car_modification = car_details["data-modification-name"]
            car_year = car_details["data-year"]

            unique_cars.add(car_id)

            data = [
                car_id,
                car_manufacturer,
                car_model, car_year,
                car_modification,
                link_to_page
            ]

            for writer in writers:
                writer.write(data)

    print("PARSING COMPLETED")


if __name__ == "__main__":
    # main()
    detailed_page = get_card_detailed_page('/auto_porsche_cayenne_35113189.html')
    get_car_detailed_data(detailed_page)