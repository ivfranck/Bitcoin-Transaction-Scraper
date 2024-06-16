from typing import Any

from bs4 import BeautifulSoup
import requests
import logging


class Scraper:
    def __init__(self, url: str):

        self.URL = url

    def scrape(self) -> list[dict[Any, Any]]:
        """
        Scrapes the website for unconfirmed Bitcoin transactions.


        :returns: list[dict[Any, Any]]
                    A list of dictionaries, where each dictionary contains details of an
                    unconfirmed Bitcoin transaction with the following keys:
                    - "hash_id" (str): The hash ID of the transaction.
                    - "hash_short" (str): A short version of the transaction hash.
                    - "output_value_btc" (float): The output value of the transaction in BTC.
                    - "output_value_dollars" (float): The output value of the transaction in dollars.
                    - "date" (str): The date of the transaction.
                    - "time" (str): The time of the transaction.
        """

        transactions = []

        logging.info(f"Scraping website: {self.URL}")
        try:
            req = requests.get(self.URL)
        except Exception as e:
            logging.error(f"Failed request. Error:{e}")

        soup = BeautifulSoup(req.text, "html.parser")

        div = soup.find('div', {'class': 'sc-7b53084c-1 czXdjN'})
        a_tags = div.findAll('a')

        for tag in a_tags:
            # hashid
            hash_id = tag.get('href').split("btc/")[1]

            # hash
            hash_tag = tag.find('div', {'class': 'sc-35e7dcf5-5 ozZoF'})
            hash = hash_tag.text.split(' ')[1]

            # date time
            dt = tag.find('div', {'class': 'sc-35e7dcf5-7 fFAyKv'})
            date_time = dt.text.split(', ')
            date = date_time[0]
            time = date_time[1]

            # btc
            btc_tag = tag.find('div', {'class': 'sc-35e7dcf5-13 isCUBz'})
            btc = btc_tag.text.split(' ')[0]
            if ',' in btc:
                btc = btc.replace(',', '')

            # dol
            dol_tag = tag.find('div', {'class': 'sc-35e7dcf5-14 bbQxqN'})
            dol = dol_tag.text[1:]
            if ',' in dol:
                dol = dol.replace(',', '')

            hash_obj = {
                "hash_id": hash_id,
                "hash_short": hash,
                "output_value_btc": float(btc),
                "output_value_dollars": float(dol),
                "date": date,
                "time": time
            }
            transactions.append(hash_obj)

        print(transactions[:2])
        return transactions
