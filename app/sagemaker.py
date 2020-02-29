import boto3
import json
import pandas as pd
from app.aws_credentials import AwsBuilder
from app.log import LoggerBuilder
from app.models import RedWineRequest, RedWineResponse

logger = LoggerBuilder().get_logger('main')


def query_endpoint(sagemaker_endpoint_name: str, r: RedWineRequest):
    #todo : get your credentials with the function get_credentials from the class AwsBuilder
    aws_access_key_id = "AKIAIV627KENFDP4IDSQ"
    aws_secret_access_key = "+VBvpn8PTPtN7rcNEXD2hEJ6hiJ1ueDeit6mPkVb"
    region = "eu-west-3"
    client = boto3.session.Session(aws_access_key_id=aws_access_key_id,
                                   aws_secret_access_key=aws_secret_access_key).client("sagemaker-runtime", region)

    # todo: complete the input json you are going to send to the sagemaker endpoint
    input_json = {"fixed acidity": [r.fixed_acidity], }

    query_input = pd.DataFrame(input_json).to_json(orient="split")
    response = client.invoke_endpoint(
        EndpointName=sagemaker_endpoint_name,
        Body=query_input,
        ContentType='application/json; format=pandas-split',
    )
    prediction = response['Body'].read().decode("ascii")
    prediction = json.loads(prediction)
    #todo : construct the response
    return RedWineResponse()
