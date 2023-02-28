.PHONY: run
run:
	pipenv run python main.py

.PHONY: test
test:
	pipenv run python -m unittest discover tests/ -v
