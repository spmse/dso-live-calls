FROM python:3.12-alpine3.18

WORKDIR /app

COPY . $WORKDIR

# RUN pip install -r requirements.txt

ENTRYPOINT ["python", "some.py"]