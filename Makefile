run:
	python app/manage.py runserver

migrate:
	python app/manage.py migrate

makemigrations:
	python app/manage.py makemigrations

shell:
	python app/manage.py shell_plus --print-sql

pep:
	flake8 app/
	