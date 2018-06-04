From alpine:edge

RUN apk add --update \
      udev \
      ttf-freefont \
      xvfb \
      chromium \
      chromium-chromedriver \
      python3 \
      py-pip

RUN pip3 install --upgrade pip && \
    pip3 install selenium beautifulsoup4 bottle

WORKDIR /home/scraper
