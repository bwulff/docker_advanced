FROM python:2.7

ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

ADD app.py /

EXPOSE 5000

ENTRYPOINT python /app.py