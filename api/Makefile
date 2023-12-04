.ONESHELL:

init:
	touch local.env

container-django-shell:
	docker compose run --rm --entrypoint bash django

run:
	docker compose run --rm --service-ports django
