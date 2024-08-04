FROM  python:3.10-alpine
EXPOSE 8000
WORKDIR /app 
COPY requirements/prod.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY ./src/app /app 

ENTRYPOINT ["uvicorn", "presentation.rest.api:create_app", "--port", "8000"]
