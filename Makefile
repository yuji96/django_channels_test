COMPOSE_LOCAL := docker-compose.yml

build-local:
	touch .env
	docker-compose -f $(COMPOSE_LOCAL) build

local:
	@make build-local
	docker-compose -f $(COMPOSE_LOCAL) up

exec:
	docker-compose -f $(COMPOSE_LOCAL) exec django bash
