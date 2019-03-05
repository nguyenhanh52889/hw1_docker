FROM python:3.6-alpine
ADD . /app
WORKDIR /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["python", "consumer.py"]
