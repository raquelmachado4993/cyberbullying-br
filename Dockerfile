FROM python:3.13.5-alpine3.22  AS python
LABEL Name=tese
LABEL Version=1.0
LABEL description="Imagem docker para detectar cyberbullying em portugu?s brasileiro"
LABEL maintainer="Raquel Moreira Machado Fernandes<raquelmachado4993@gmail.com>"

RUN apk add build-base
RUN apk add clang

RUN mkdir -p /scripts/
COPY ./  /scripts/
RUN pip install -r /scripts/requirements.txt  --root-user-action=ignore
