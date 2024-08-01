FROM --platform=amd64 python:3.10-slim-bookworm

WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./ca_cert.pem /usr/local/share/ca-certificates/ca_cert.crt
RUN update-ca-certificates --verbose

COPY . .

EXPOSE 80

CMD ["python3", "main.py"]