# Flightly ✈️

[![CircleCI](https://circleci.com/gh/parseendavid/flightly_flight-booking-app/tree/develop.svg?style=svg)](https://circleci.com/gh/parseendavid/flightly_flight-booking-app/tree/develop)
[![Coverage Status](https://coveralls.io/repos/github/parseendavid/flightly_flight-booking-app/badge.svg?branch=develop)](https://coveralls.io/github/parseendavid/flightly_flight-booking-app?branch=develop)


Flightly is a flight booking app that aims at easing the process of booking flight by automation.

## Prerequisite

This project is built on `Python 3.7.0` but will run on all Python `3.x` versions.
For more information check the `requirements.txt` file for package names and versions used.

## Setup & Installation

N/B: It is highly recommended to use [virtual environments](https://realpython.com/python-virtual-environments-a-primer/)
To install all required packages

```bash
make install
```

or

```bash
pip install -r requirements.txt
```

Then setup appropriate environment variables as prescribed in the `.env.sample` file and save them in a `.env` in the root directory

## Database Initialization

N/B: You have to create a postgresql database and added it to the `.env` file or runtime envirionment using

```bash
export DATABASE_URI="postgres:///<database-name>"
```

Then run the command bellow if you want to create tables and populate them with dummy data.

```bash
make initdb
```

or this one if you only want to create tables in your database.

```bash
make migrate
```

## Running Local server

To run the local server use:

```bash
make serve
```

or

```bash
python manage.py runserver
```

## Using The Docs

To access the API's Documentation Web Interface run the server and navigate to `/`.

## Creating SuperUser and Using the Admin Dashboard

To create a superuser use the below command and fill in the relevant prompts:

```bash
python manage.py createsuperuser
```

To access the Admin Dashboard navigate to `/admin` url on the server ran above and login with the superuser credentials used in the above command

## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
