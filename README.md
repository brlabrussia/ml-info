## Требования
- [`Traefik`](https://github.com/weirdname404/traefik-daemon "Traefik")

## Quick Start
```shell
cp .env.example .env # базовые настройки окружения
docker-compose up -d # запуск сервисов в фоне
docker-compose exec django ./manage.py createsuperuser # создание суперпользователя для админки
docker-compose logs -f # аттач к логам
```
Админка https://info.localhost/
