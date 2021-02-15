import logging
import cmd
import os
# from azure.keyvault.secrets import SecretClient
# from azure.identity import DefaultAzureCredential
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')
    secret = os.getenv('mysecretname', 'Could not find a secret')
    # url = 'https://test-service-function.azurewebsites.net/api/testfunction?'
    # response = requests.post(url, data=post_fields, timeout=timeout)
    # print("Response time:",response.elapsed.total_seconds())

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully .")
    else:
        return func.HttpResponse(f"This HTTP triggered function executed successfully from git source code with {secret}",

             status_code=200
        )
