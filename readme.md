## Local Development

---

### Build docker image and up all entities

```sh
pre-commit install
```

```sh
make init && cd api && docker network create anri_main && docker-compose build && docker-compose up
```

### Migrations

```sh
cd api && make container-django-shell
python manage.py makemigrations
python manage.py migrate
```
