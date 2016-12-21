# Photogram
[![Build Status](https://travis-ci.org/KirovVerst/photogram.svg?branch=master)](https://travis-ci.org/KirovVerst/photogram)

Web application for photo publishing
## Installing
### Requirements
1. Python 3.5.*
2. Node 6.9.*

### Backend installation
```shell
$ pip install -r requirements.txt
$ python manage.py migrate
```
Installation all necessary python packages and applying database migrations.
### Frontend installation
```shell
$ npm install
```
Installation all necessary node modules.

### Building
Development mode
```shell
$ npm run webpack
```
Production mode
```shell
$ npm run build
```
## Features
Project has been developing on ReactJS, Django and Django Rest Framework

Rest API:
* CRUD methods for photos
* Authentication that is based on JWT

## Licensing

The code in this project is licensed under MIT license.
