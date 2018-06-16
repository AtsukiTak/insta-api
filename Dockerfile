From alpine:edge

RUN apk add --update python3 py-pip && \
    pip3 install --upgrade pip && \
    pip3 install bottle paste instalooter

WORKDIR /home/scraper

COPY . /home/scraper

ENTRYPOINT ["python3", "server.py"]
