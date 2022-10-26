# Global command variables
COMPOSE_BUILD_NETTEST = docker compose build nettest
COMPOSE_RUN_NETTEST = docker compose run --rm nettest
COMPOSE_RUN_BASH = docker compose run --rm --entrypoint bash nettest
DOCKER_CLEAN = docker compose down --remove-orphans && docker image prune && docker network prune

ARGUMENTS = -f csv -A

.PHONY: run_test
run_test: build run

.PHONY: build run bash clean

# Builds the docker image using docker compose.
build: 
	$(COMPOSE_BUILD_NETTEST) 

# Runs the docker images for using docker compose.
run:
	$(COMPOSE_RUN_NETTEST) net-test.py $(ARGUMENTS)

help:
	$(COMPOSE_RUN_NETTEST) net-test.py -h

servers:
	$(COMPOSE_RUN_NETTEST) net-test.py -L

# Enter a bash terminal within the docker image.
bash:
	$(COMPOSE_RUN_BASH)

# Cleans and removes old docker images and network interfaces.
clean:
	$(DOCKER_CLEAN)