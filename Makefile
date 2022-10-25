COMPOSE_BUILD_NETTEST = docker compose build nettest
COMPOSE_RUN_NETTEST = docker compose run --rm nettest
COMPOSE_RUN_BASH = docker compose run --rm nettest bash
DOCKER_CLEAN = docker compose down --remove-orphans && docker image prune && docker network prune

.PHONY: run_test
run_test: build run

.PHONY: build run bash clean

build: 
	$(COMPOSE_BUILD_NETTEST)

run:
	$(COMPOSE_RUN_NETTEST)

bash:
	$(COMPOSE_RUN_BASH)

clean:
	$(DOCKER_CLEAN)