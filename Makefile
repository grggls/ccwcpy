test:
	python -m unittest discover -s tests -p 'test_*.py'

run:
	python ccwc.py ./tests/test_data/test.txt

lint:
	pipenv run format
	pipenv run lint

.PHONY: test
