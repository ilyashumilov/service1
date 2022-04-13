FROM python:3.8
WORKDIR /service
COPY . .
EXPOSE 8000
RUN pip install -r requirements.txt
