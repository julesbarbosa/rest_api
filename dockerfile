FROM python:3.9-alpine

USER root

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD ["juliana_app.py"]
