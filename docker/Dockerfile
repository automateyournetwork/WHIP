FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive

ENV DJANGO_SETTINGS_MODULE=whip.settings
ENV DJANGO_SUPERUSER_EMAIL=admin@automateyournetwork.ca
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_PASSWORD=admin

RUN echo "==> Upgrading apk and installing system utilities ...." \
 && apt -y update \
 && apt-get install -y wget \
 && apt-get -y install sudo

RUN echo "==> Installing Python3 and pip ...." \  
 && apt-get install python3 -y \
 && apt install python3-pip -y \
 && apt install openssh-client -y

RUN echo "==> Adding Django ..." \
 && pip install django

RUN echo "==> Adding Django REST Framework ..." \
 && pip install djangorestframework

RUN echo "==> Adding CORS Headers ..." \
 && pip install django-cors-headers

RUN echo "==> Adding timezone ..." \
  && pip install pytz --upgrade \
  && pip install tzdata --upgrade

RUN echo "==> Adding PostgreSQL ..." \
 && pip install psycopg2-binary

RUN echo "==> Adding Rich Click ..." \
 && pip install rich-click

RUN echo "==> Install dos2unix..." \
  && sudo apt-get install dos2unix -y 

RUN echo "==> Install django ssl server..." \
  && pip install django-sslserver

RUN echo "==> Install rquests urlib3.." \
  &&  pip install requests \
  &&  pip install urllib3 

COPY /whip /whip/
COPY /scripts /scripts/

RUN echo "==> Convert script..." \
  && dos2unix /scripts/startup.sh

CMD ["/bin/bash", "/scripts/startup.sh"]