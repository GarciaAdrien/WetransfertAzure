import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
storage_account_key = "YF1+wBjHT1g7JnwUyaiOBGrsNSnh2ydrpUrFEBo/vx5NxU+RiLuyMpP+lLTa3Qld1lYh+QULBEAe+AStur4KMQ=="
nom_compte_stockage = "storageaccountadrien"
connection_string = "DefaultEndpointsProtocol=https;AccountName=storageaccountadrien;AccountKey=gVKIJjA0dCYn5QFZBHk/l5dtTdu6imKpoZPScvqbuuI8TBRiy4hXeQliIESrpSsAEYrx2LNfQdq++ASt3CdpiA==;EndpointSuffix=core.windows.net"
nom_conteneur = "file-upload"

def uploadToBlobStorage(file_path,file_name): 
   blob_service_client = BlobServiceClient.from_connection_string(connection_string)
   blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
   open(file_path,"rb") 
   blob_client.upload_blob(données)
   print(f"Téléchargé {nom_fichier}.")

uploadToBlobStorage('PATH_OF_FILE_TO_UPLOAD','FILE_NAME')

