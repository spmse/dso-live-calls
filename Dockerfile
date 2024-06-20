FROM python:3.12

WORKDIR /app

COPY . $WORKDIR

# RUN pip install -r requirements.txt

ENTRYPOINT ["python", "some.py"]