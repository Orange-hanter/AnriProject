![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Celery](https://img.shields.io/badge/celery-37814A.svg?style=for-the-badge&logo=celery&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white)

# What's AnriProject repository?
...

---

## How to start

### *Local Development*


- Build project
```sh
  cd api
```

```sh
  docker compose build
```

- Run migrations
```sh
    make container-django-shell
```

```sh
    python manage.py makemigrations
```
```sh
    python manage.py migrate
```


- Create superuser
```sh
    make container-django-shell
```

```sh
    python manage.py createsuperuser
```
- Create network
```sh
  docker network create anri_main
```

- Run application
```sh
  docker compose up
```

*Before you commit, set **[pre-commit](https://pre-commit.com/)**.*
```sh
  pre-commit install
```

## Usage

### Admin panel:
- http://localhost:8000/admin/

### Available API routes:
You can check all routes using swagger(http://localhost:8000/api/v1/swagger/) or redoc(http://localhost:8000/api/v1/redoc/)
