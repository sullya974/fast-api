from fastapi import FastAPI
from app.log import LoggerBuilder
from app.config import ConfigLoader
from app.models import RedWineRequest, RedWineResponse
from app.sagemaker import query_endpoint

app_config = ConfigLoader.load()
logger = LoggerBuilder().get_logger('main')
app = FastAPI(**dict(debug=True))
logger.info('App server started successfully')


@app.get(path="/")
async def root():
    return "This is an API for request AWS Sagemaker for prediction"


#todo : Create a POST endpoint to query your sagemaker endpoint
# Look at the signature of the function query_endpoint
@app.post(path='', response_model=RedWineResponse)
def predict_red_wine_quality(request: RedWineRequest):
    return query_endpoint("sagemaker_endpoint", request)
