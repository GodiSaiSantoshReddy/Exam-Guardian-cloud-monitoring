from azure.storage.blob import BlobServiceClient
import os

def upload_to_azure(file_path, container_name="examdata"):
    connect_str = "YOUR_AZURE_STORAGE_CONNECTION_STRING"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=os.path.basename(file_path))

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)
