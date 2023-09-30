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
        CSVWriter('cars1.csv', csv_headers),
        CSVWriter('cars2.csv', csv_headers),
        # StdOutWriter(),
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

            data = [car_id, car_manufacturer, car_model, car_year, car_modification, link_to_page]

            for writer in writers:
                writer.write(data)

    print("PARSING COMPLETED")


if __name__ == "__main__":
    main()
