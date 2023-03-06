.PHONY: run
run:
	pipenv run python -m pipmore.cli numpy 3.7

.PHONY: test
test:
	pipenv run python -m unittest discover tests/ -v
