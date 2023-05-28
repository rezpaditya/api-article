FROM python:3.10.11-slim-buster

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /src/requirements.txt && \
    pip cache purge && rm -rf ~/.cache/pip

COPY ./app/ /src/app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]