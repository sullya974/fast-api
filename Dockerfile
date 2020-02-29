# todo: Pull official fastapi image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

#upgrade pip
RUN pip install --upgrade pip

# Install all dependencies
ADD requirements.txt ./
RUN python -m pip install -r requirements.txt

# Install app and config file
COPY ./app /app/app
COPY ./config /app/config

ENTRYPOINT /app/app/startup.sh ${ENV}