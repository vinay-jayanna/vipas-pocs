FROM python:3.9-slim
WORKDIR /usr/src/app
RUN pip install devpi-server
COPY entrypoint.sh /usr/src/app/entrypoint.sh
EXPOSE 3141
ENTRYPOINT ["./entrypoint.sh"]

