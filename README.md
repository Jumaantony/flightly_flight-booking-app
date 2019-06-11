# Flightly ✈️

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

## Running Local server

To run the local server use:

```bash
make serve
```

or

```bash
python manage.py runserver
```

## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
