FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV WP_ENVIRONMENT_TYPE development


COPY wordpress_updater.py .

CMD ["python", "wordpress_updater.py"]
