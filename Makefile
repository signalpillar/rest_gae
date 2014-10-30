.PHONY: tests

deps:
	pip install -r dev-requirements.txt

tests:
	py.test --looponfail -v rest_gae tests
