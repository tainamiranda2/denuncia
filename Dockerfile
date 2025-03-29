FROM python:3.8
ENV PYTHONUNBUFFERED 1


RUN apt-get update && apt-get install -y default-libmysqlclient-dev libssl-dev git


RUN pip install --trusted-host pypi.python.org --upgrade pip
ADD requirements.txt /app/
RUN pip install --trusted-host pypi.python.org -r /app/requirements.txt


WORKDIR /app
COPY . /app/


CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 intranet_multimarcas.wsgi:application