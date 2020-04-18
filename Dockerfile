FROM python:3-buster

COPY app /app/
ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

EXPOSE 8000

RUN useradd -ms /bin/bash incog

USER incog

CMD gunicorn --bind 0.0.0.0:8000 -w 4 app.wsgi:app
