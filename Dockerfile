FROM python:3

WORKDIR /usr/src/app
RUN git clone https://github.com/pabloingino/hazelcast-python-client.git .

RUN pip install --no-cache-dir -r requirements-dev.txt

RUN pip install hazelcast-python-client

CMD [ "python", "./index.py" ]