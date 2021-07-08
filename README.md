# Django example: Ticket system

## Introduction

Sample api on a simple ticket system using django.

## Requirements

- Python 3.7+
- Django 3.2

## Installation

### Local

Create a virtual environment and install dependencies:

```
python3.7 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Migrate database

```
./manage.py migrate
```

#### Run development server

```
./manage.py runserver 0:8000
```

### Docker

Create the docker image. This step generates the image that will be used to create the container. In addition, the application and all its dependencies are installed:

```
docker build -t django-ticket:latest .
```

Once this step is ready, run the container:

```
docker run -it -p 8000:8000 --rm --name django-ticket-example django-ticket:latest
```

The _--rm_ option is to remove the container once its execution stops.

### Run tests

```
./manage.py test
```

## Author

* **Juan Carlos Ramos Peroni** - Developer - [peronidev](https://bitbucket.org/peronidev)
