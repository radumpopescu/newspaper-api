FROM checksum/python-newspaper:latest

RUN apk --update add linux-headers
RUN pip install --no-cache-dir --upgrade newspaper3k
RUN pip install --no-cache-dir flask

COPY . /root

EXPOSE 38765

CMD ["python3", "/root/server.py"]