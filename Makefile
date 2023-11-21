#!make
SHELL := /bin/bash

build-docker:
	docker build -t checkweb:latest -f ./Dockerfile .