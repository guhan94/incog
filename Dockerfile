FROM python:3-slim
# Remove vulnerable packages https://snyk.io/test/docker/python:3-slim/?severity=high&severity=medium&policy=open&tab=issues
RUN apt-get --purge -y --allow-remove-essential remove libsqlite3-0 libidn2-0

COPY app /app/
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

EXPOSE 8000

RUN useradd -ms /bin/bash incog

USER incog

CMD gunicorn --bind 0.0.0.0:8000 -w $(( 2 * `nproc` + 1 )) app.wsgi:app
