build:
	pip install -e .
	python -m unittest discover tests/unit
	mypy budgxeto/ tests/
	python -m unittest discover tests/acceptance
