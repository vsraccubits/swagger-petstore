
# Swagger Petstore in Django REST framework - OpenAPI 3.0

## Overview

This is an implementation of the OpenAPI 3.0 swagger pet store application in [Django REST framework](https://www.django-rest-framework.org/).

This sample is based on https://petstore3.swagger.io/ and provides an example of swagger / OpenAPI 3 petstore.

This Django REST framework application serve an existing OpenAPI schema definition by renderingusing Swagger UI and Redoc.

## Generate Documentation From Schema

- Generate schema file in yaml/json.
    ```python
    python manage.py generateschema > schema.yml
    ```
- Set schema file as a static resource.

- Integrate Swagger UI and Redoc as Django template.
    ```shell
    |-- static/
    |----- swagger/
    |-------- schema.yaml
    |-- templates/
    |----- swagger/
    |-------- swagger-ui.html
    |-------- redoc.html
    ```

## Requirements

**Python:** >= 3.6

**Django:** (2.2, 3.2, 4.0, 4.1)

**Django REST Framework:** (3.10.3, 3.11, 3.12, 3.13, 3.14)

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

## Documentation

[OpenAPI 3.0](https://docs.google.com/document/d/1vtj2gmCNfnIYF3SM13QGJZD2SAFzLtGVEtpD9-uKSos/edit?usp=sharing)


## License

[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)
