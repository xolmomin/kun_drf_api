migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate
	@echo "migrate boldi"

create_dummy:
	python3 manage.py create -b 100000 -c 15

create_index:
	python3 manage.py search_index --rebuild