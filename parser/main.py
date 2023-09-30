import requests
from bs4 import BeautifulSoup

BASE_URL = "https://auto.ria.com/uk/search/"


def get_page(url: str) -> str:
    query_parameters = {
        "indexName": "auto,order_auto,newauto_search",
        "categories.main.id": 1,
        "brand.id[0]": 59,
        "country.import.usa.not": -1,
        "price.currency": 1,
        "abroad.not": 0,
        "custom.not": 1,
        "page=0&size": 100,
    }

    response = requests.get(url=url, params=query_parameters)
    response.raise_for_status()
    html_page = response.text
    return html_page


def main(page: str) -> None:
    soup = BeautifulSoup(page, "html.parser")

    search_content = soup.find("div", {"id": "searchResults"})
    all_content = search_content.find_all("section", {"class": "ticket-item"})

    for item in all_content:
        car_details = item.find("div", {"class": "hide"})
        car_id = car_details["data-id"]
        link_to_page = car_details["data-link-to-view"]
        car_manufacturer = car_details["data-mark-name"]
        car_model = car_details["data-model-name"]
        car_modification = car_details["data-modification-name"]
        car_year = car_details["data-year"]

        print(car_id, link_to_page, car_year, car_modification, car_model, car_manufacturer)


if __name__ == "__main__":
    main(get_page(BASE_URL))
