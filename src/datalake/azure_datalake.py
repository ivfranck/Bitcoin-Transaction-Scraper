import logging
import json
from typing import Any

from azure.storage.filedatalake import DataLakeServiceClient, FileSystemClient, DataLakeFileClient


class AzDataLake:
    def __init__(self, conn_string, file_system, directory):
        """
        :param conn_string : The connection string for Azure Data Lake Storage.
        :param file_system : The name of the file system in the Data Lake.
        :param directory : The directory path within the file system to upload files to.
        """

        self._CONNECTION_STRING = conn_string
        self.FILE_SYSTEM = file_system
        self.DIRECTORY = directory

    def file_client(self, file_name: str) -> DataLakeFileClient:
        """
        This method establishes a connection to the Azure Data Lake Storage using the
        connection string, and then creates a file client for the specified file within the file system.

        :param file_name: The name of the file to create a client for.

        :returns: A client to interact with the specified file in Azure Data Lake Storage.
        """
        try:
            logging.info("Connecting to DataLake Client...")
            service_client = DataLakeServiceClient.from_connection_string(conn_str=self._CONNECTION_STRING)

            client = service_client.get_file_system_client(file_system=self.FILE_SYSTEM)
            logging.info(f"File System Client: {self.FILE_SYSTEM}")
            return client.get_file_client(file_name)
        except Exception as e:
            logging.error(e)

    def upload_to_datalake(self, data: list[dict[Any, Any]], checkpoint: str) -> None:
        """
        Uploads a list of dictionaries as a JSON file to Azure Data Lake Storage.

        This method converts the given data into a JSON string and uploads it to a file in the specified
        directory within the file system. The file name is derived from the given checkpoint parameter.


        :param data: The data to be uploaded, as a list of dictionaries.
        :param checkpoint: A string used to generate the file name for the uploaded data.
        """

        file_name = f"{self.DIRECTORY}/{checkpoint}.json"

        file_client = AzDataLake.file_client(self, file_name)

        json_data = json.dumps(data)

        logging.info("Uploading to datalake...")
        file_client.upload_data(json_data, overwrite=True)

