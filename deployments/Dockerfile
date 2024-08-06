FROM  python:3.10-alpine

WORKDIR /src 
COPY requirements/prod.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY ./src /src 

CMD ["uvicorn", "app.presentation.rest.api:create_app", "--host", "0.0.0.0", "--port", "8000"]
