all: check-style check_types unittest localtest


.PHONY: check-style
check-style:
	flake8 .
	@echo "Code style check done."

.PHONY: fix-style
fix-style:
	autopep8 --in-place --recursive --aggressive --aggressive .
	
.PHONY: check_types
check-types:
	mypy --disallow-untyped-defs --strict .
	@echo "Static type check done."

.PHONY: unittest
unittest:
	pytest --verbose  --color=yes --cov --cov-report term --cov-report html tests/
	@echo "Unittest done."


.PHONY: cleanall
localtest:
	kattis test
	@echo "Local kattis sample data test done."


.PHONY: clean
clean:
	rm -rf `find . -type d -name __pycache__`
	rm -rf `find . -type d -name .pytest_cache`
	rm -rf `find . -type d -name .mypy_cache`
	rm -rf `find . -type f -name .coverage`

