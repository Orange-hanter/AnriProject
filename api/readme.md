## Local Development

---
### Build
1. `cd api ` `cp .env.example .env`
2. `docker network create anri_main`
3. `cd docker` `docker-compose up`

### Migrations

- At docker directory run `make container-fastapi-shell`
- `alembic revision --autogenerate -m "Revision version name"`
- `alembic upgrade head`
