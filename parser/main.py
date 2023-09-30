import requests
from bs4 import BeautifulSoup

BASE_URL = ("https://auto.ria.com/uk/search/"
            "?indexName=auto,order_auto,newauto_search"
            "&categories.main.id=1"
            "&brand.id[0]=59"
            "&country.import.usa.not=-1"
            "&price.currency=1"
            "&abroad.not=0"
            "&custom.not=1"
            "&page=0&size=100")


def main(url: str) -> None:

    response = requests.get(url=url)
    response.raise_for_status()
    html_page: str = response.text

    soup = BeautifulSoup(html_page, "html.parser")

    search_content = soup.find("div", {"id": "searchResults"})
    all_content = search_content.find_all("section", {"class": "ticket-item"})

    for item in all_content:
        print(item)


if __name__ == "__main__":
    main(BASE_URL)
