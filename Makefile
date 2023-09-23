run:
	python3 app/manage.py runserver

migrate:
	python3 app/manage.py migrate

makemigrations:
	python3 app/manage.py makemigrations

shell:
	python3 app/manage.py shell_plus --print-sql

celery:
	cd app && celery -A settings worker -l INFO --autoscale=0,10

beat:
	cd app && celery -A settings beat -l INFO

pytest:
	pytest ./app/tests --cov=app --cov-report html && coverage report --fail-under=75
