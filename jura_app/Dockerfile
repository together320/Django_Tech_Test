# syntax=docker/dockerfile:1.4

FROM python:3.7-alpine AS builder
EXPOSE 8000
WORKDIR /django-tech-test
COPY requirements.txt /django-tech-test
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /django-tech-test
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
