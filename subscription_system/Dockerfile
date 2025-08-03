FROM python:3.10

RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev gcc default-mysql-client \
    && pip install mysqlclient



ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

#  Copy the entire project (not just subscription_system/)
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Ensure staticfiles dir exists
RUN mkdir -p /app/staticfiles
RUN python manage.py collectstatic --noinput

# Start the app with Gunicorn
CMD ["gunicorn", "subscription_system.wsgi:application", "--bind", "0.0.0.0:8000"]
