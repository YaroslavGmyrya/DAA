FROM ubuntu:22.04

RUN apt update && apt install -y python3 && apt install -y python3-flask

COPY server.py .

CMD ["python3", "server.py"]
