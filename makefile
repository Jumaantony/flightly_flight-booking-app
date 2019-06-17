install:
	pip install -r requirements.txt

migrations:
	./manage.py makemigrations

migrate:
	./manage.py migrate

set_env_vars:
	@[ -f .env ] && source .env

initdb:
	$(MAKE) migrate
	python helpers/db/db_populator.py

serve:
	$(MAKE) set_env_vars
	./manage.py runserver

.PHONY: set_env_vars