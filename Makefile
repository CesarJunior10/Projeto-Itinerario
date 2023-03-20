SHELL := /bin/bash

.PHONY: run install requirements help lint

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

run:
	uvicorn src.main:app --reload

install:
	pip install --upgrade pip
	pip install -r requirements.txt

requirements:
	pip freeze > requirements.txt

lint:
	black .
