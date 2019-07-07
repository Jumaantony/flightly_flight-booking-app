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

To access the API's Documentation Web Interface run the server and navigate to `/docs/`.

## Using The Schema

To access the API's Documentation Web Interface run the server and navigate to `/api/v1/`.

## Creating SuperUser and Using the Admin Dashboard

To create a superuser use the below command and fill in the relevant prompts:

```bash
python manage.py createsuperuser
```

To access the Admin Dashboard navigate to `/admin` url on the server ran above and login with the superuser credentials used in the above command

## Base Endpoints
| Endpoint                  | Function                                      | HTTP METHOD      | Required Params (Optional Params)  | Required Permissions                                  |
| ------------------------- |:---------------------------------------------:| ----------------:| ----------------------------------:| -----------------------------------------------------:|
| /docs                     | Documentation for all the API's functionality | GET              | None                               | None                                                  |
| /api/v1/                  | Schema for V1 endpoints                       | GET              | None                               | None                                                  |
| /api/v1/auth/jwt/obtain/  | JWT login                                     | POST             | email, password                     | None                                                  |
| /api/v1/auth/jwt/refresh/ | JWT refreshing                                | POST             | token                              | None                                                  |
| /api/v1/users/            | User registration                             | POST             | email, password, first_name, (last_name, photograph(upload_link)) | None                                                  |
| /api/v1/users/all         | Fetching all users                            | GET              | None                               | Authenticated & IsStaff/Superuser                     |
| /api/v1/user/\<uuid:pk\>    | Fetching single user's info                   | GET              | None                               | Authenticated & (IsStaff/Superuser or IsAccountOwner) |
| /api/v1/user/\<uuid:pk\>    | Update single user's info                     | PUT              | email, password, first_name, (last_name, photograph(upload_link)) | Authenticated & (IsStaff/Superuser or IsAccountOwner) |
| /api/v1/user/\<uuid:pk\>    | Partially Update single user's info              | PATCH            | (email, password, first_name, last_name, photograph(upload_link)) | Authenticated & (IsStaff/Superuser or IsAccountOwner) |
| /api/v1/user/\<uuid:pk\>    | Partially Update single user's info              | DELETE            | None | Authenticated & (IsStaff/Superuser or IsAccountOwner) |
| /api/v1/flights/            | List all flights                            | GET             | email, password, first_name (last_name, photograph(upload_link)) | None                                                  |
| /api/v1/flights/            | Create a Flight                             | POST             |name, departure_airport, arrival_airport, departure_datetime,	capacity,(price)| Authenticated & IsStaff/Superuser   |
| /api/v1/flight/\<uuid:pk\>    | Fetch a single flight's info                | GET             |None| None   |
| /api/v1/flight/\<uuid:pk\>    | Update a single flight's info                | PUT             |name, departure_airport, arrival_airport, departure_datetime,	capacity,(price)| Authenticated & IsStaff/Superuser   |
| /api/v1/flight/\<uuid:pk\>    | Partially update a single flight's info    | PATCH             |(name, departure_airport, arrival_airport, departure_datetime,	capacity, price)| Authenticated & IsStaff/Superuser |
| /api/v1/flight/\<uuid:pk\>    | Delete a single flight    | DELETE             |None| Authenticated & IsStaff/Superuser |
| /api/v1/reservations/    | Fetch all reservations if Admin, or Owned reservations if nonAdmin    | GET             |none| Authenticated & (IsStaff/Superuser or IsReservationOwner) |
| /api/v1/reservations/    | Create a reservation if Admin, or for self only if nonAdmin    | POST             |flight type:'flight url', traveler type:'user url'| Authenticated & (IsStaff/Superuser or IsReservationOwner) |
| /api/v1/reservation/\<uuid:pk\>    | Fetch a single reservation if Admin, or Owned reservation if nonAdmin    | GET             |none| Authenticated & (IsStaff/Superuser or IsReservationOwner) |
| /api/v1/reservation/\<uuid:pk\>    | Update a reservation if Admin, or Owned reservation if nonAdmin    | PUT             |flight type:'flight url', traveler type:'user url'| Authenticated & (IsStaff/Superuser or IsReservationOwner) |
| /api/v1/reservation/\<uuid:pk\>    | Partially update a reservation if Admin, or Owned reservation if nonAdmin    | PATCH             |(flight type:'flight url', traveler type:'user url')| Authenticated & (IsStaff/Superuser or IsReservationOwner) |
| /api/v1/reservation/\<uuid:pk\>    | Delete a reservation if Admin, or Owned reservation if nonAdmin    | DELETE             |none| Authenticated & (IsStaff/Superuser or IsReservationOwner) |


## Extra Functionality

|Endpoint Method/Function | Query Param  | Function              | Example               |
| ----------------------- | :-----------:| ----------------------| ----------------------|
|GET /list                | search       | searches passed string| /users/all?search=John|
|GET /list                | ordering     | Orders passed field use(+) for ascending & (-) for descending| /flights/?ordering=-departure_datetime|

## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
