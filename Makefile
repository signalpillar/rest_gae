.PHONY: tests

deps:
	pip install -r dev-requirements.txt

tests:
	py.test --looponfail --pep8 rest_gae tests
