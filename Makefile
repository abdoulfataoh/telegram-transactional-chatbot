help:
	@echo "make mypy	    - Checks static typing with mypy"
	@echo "make flake8          - Checks flake8"
	@echo "make test            - Runs the test suite"
	

mypy:
	mypy start.py --ignore-missing-imports

flake8:
	flake8 app start.py

test: export TEST = 1
test: typecheck
	python tests
