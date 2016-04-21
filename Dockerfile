FROM ubuntu:14.04
MAINTAINER Zack Dever <zackdever@gmail.com>

RUN apt-get update && apt-get install -y \
  build-essential \
  wget \
  && apt-get build-dep imagemagick -y

RUN wget http://www.imagemagick.org/download/releases/ImageMagick-6.9.3-8.tar.gz
RUN tar xzvf ImageMagick-6.9.3-8.tar.gz
WORKDIR ImageMagick-6.9.3-8/
RUN ./configure && make
RUN make install
WORKDIR /

RUN apt-get update && apt-get install -y \
  python3-pip \
  tesseract-ocr

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
COPY app.py .

EXPOSE 5000
COPY ticket.jpg .

ENTRYPOINT ["python3", "app.py"]


