"""
This script scrapes unconfirmed Bitcoin transactions from a specified URL and uploads the data to Azure Data Lake Storage.

The script performs the following steps:
1. Initializes the Scraper object with the specified URL.
2. Scrapes the website to retrieve unconfirmed Bitcoin transactions.
3. Initializes the AzDataLake object with the Azure Data Lake connection details.
4. Uploads the scraped data to Azure Data Lake Storage with a timestamped filename.

:constants:

URL : The URL of the website to scrape unconfirmed Bitcoin transactions from.
_CONNECTION_STRING : The connection string for Azure Data Lake Storage.
FILE_SYSTEM : The name of the file system in the Data Lake.
DIRECTORY : The directory path within the file system to upload files to.

:modules:

Scraper : scraper.scraper
    - A module containing the Scraper class for scraping unconfirmed Bitcoin transactions.
AzDataLake : datalake.azure_datalake
    - A module containing the AzDataLake class for interacting with Azure Data Lake Storage.

"""

import datetime
import json
import logging

from constants import URL, _CONNECTION_STRING, FILE_SYSTEM, DIRECTORY
from scraper.scraper import Scraper
from datalake.azure_datalake import AzDataLake

if __name__ == "__main__":
    sc = Scraper(URL)
    checkpoint = datetime.datetime.now().isoformat().split('.')[0]
    logging.info(f"Triggered at {checkpoint}")
    data = sc.scrape()

    adl = AzDataLake(_CONNECTION_STRING, FILE_SYSTEM, DIRECTORY)
    adl.upload_to_datalake(data=data, checkpoint=checkpoint)

    with open("../data/transactions.json", "w") as jsonData:
        jsonData.write(json.dumps(data))
