
# Swagger Petstore in Django REST framework - OpenAPI 3.0

## Overview

This is an implementation of the OpenAPI 3.0 swagger pet store application in [Django REST framework](https://www.django-rest-framework.org/).

This sample is based on https://petstore3.swagger.io/ and provides an example of swagger / OpenAPI 3 petstore.

API documentation is generated with [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/index.html), which is a third-party package that generates OpenAPI 3.0 schema for Django REST framework.

Check the feature-swagger-ui branch for generating Swagger -UI with a pre-existing schema definition file.

## Features

- Check support of different drf views with drf-spectacular.
    - Function based views
    - Class based views
    - Mixins
    - Concrete View Classes
    - ViewSet
    - ModelViewSet
- Additional parameters
- Basic and Token Authentication
- MultiPartParser - Parses multipart HTML form, supports file uploads.
- Tags, Summery, Description extraction


## Requirements

**Python:** >= 3.6

**Django:** (2.2, 3.2, 4.0, 4.1)

**Django REST Framework:** (3.10.3, 3.11, 3.12, 3.13, 3.14)

**drf-spectacular:** 24.2

**Pillow:** 9.2

## Installation

The first thing to do is to clone the repository.

```shell
  $ git clone https://github.com/vsraccubits/swagger-petstore.git
  $ cd swagger-petstore
```

Create a virtual environment to install dependencies in and activate it.

```shell
  $ python3 -m venv venv
  $ source venv/bin/activate
```

Then install the dependencies.

```shell
  (env)$ pip install -r requirements.txt
```

Once pip has finished downloading the dependencies.

```shell
  (env)$ cd project
  (env)$ python manage.py runserver
```
And navigate to [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/).




## Using the UI

Once started, you can view the api documentation in Swagger-UI by pointing to [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/).

Schema serving with Redoc available at [http://localhost:8000/api/v1/redoc/](http://localhost:8000/api/v1/redoc/).

Generated shema can download at [http://localhost:8000/api/v1/schema/](http://localhost:8000/api/v1/schema/).

## Documentation

[OpenAPI 3.0](https://docs.google.com/document/d/1vtj2gmCNfnIYF3SM13QGJZD2SAFzLtGVEtpD9-uKSos/edit?usp=sharing)


## License

[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)
