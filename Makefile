.PHONY: up build test help default

default: build

help:
	@echo 'Management commands for biddersvc:'
	@echo
	@echo 'Usage:'
	@echo '    make build           Compile the project.'
	@echo '    make tidy            Prune any extraneous requirements.'
	@echo '    make up              Start the service.'
	@echo '    make clean      	    Clean project.'
	@echo '    make lint            Lint project.'
	@echo '    make test            Run tests on a compiled project.'
	@echo '    make shell           Open shell with test environment.'
	@echo '    make run cmd="cmd"   Run command inside the service.'
	@echo

build:
	docker-compose build --force-rm --parallel

up:
	docker-compose up app

cmd=go run ./cmd/biddersvc
run:
	docker-compose run --rm --service-ports app $(cmd)

run-dev:
	docker-compose run --rm --service-ports dev $(cmd)

tidy: cmd=go mod tidy
tidy: run-dev

lint:
	docker-compose run --rm lint

test: cmd=go test -cover ./...
test: run-dev

test-with-report: cmd=go test -covermode=atomic -coverprofile=coverage.out ./...
test-with-report: run-dev
test-with-report:
	go tool cover -html=coverage.out && rm coverage.out

shell: cmd=bash
shell: run-dev

down:
	docker-compose down --remove-orphans

clean: down
	docker-compose rm

compile-proto: compile-proto-go compile-proto-python

compile-proto-go:
	protoc -I proto --go_out=. --go-grpc_out=. ./proto/*.proto
	mv github.com/Buzzvil/biddersvc/buzzvil_bidder_v1/* proto
	rm -rf github.com

compile-proto-python:
	./proto/build-n-publish-python.sh