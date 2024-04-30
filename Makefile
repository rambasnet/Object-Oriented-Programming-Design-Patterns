TEST = python -m pytest
TEST_ARGS = -s --verbose --color=yes
TYPE_CHECK = mypy --strict --allow-untyped-decorators --ignore-missing-imports
STYLE_CHECK = flake8
COVERAGE = python -m pytest
ASSIGNMENT = 'demo-assignments'

.PHONY: all
all: check-style check-type run-test-coverage clean
	@echo "All checks passed"

.PHONY: check-type
check-type:
	$(TYPE_CHECK) $(ASSIGNMENT)/A0/hello
	$(TYPE_CHECK) $(ASSIGNMENT)/A0-OOP/hello
	$(TYPE_CHECK) $(ASSIGNMENT)/A1/cold
	$(TYPE_CHECK) $(ASSIGNMENT)/A1-OOP/cold

.PHONY: check-style
check-style:
	$(STYLE_CHECK) $(ASSIGNMENT)/A0/hello
	$(STYLE_CHECK) $(ASSIGNMENT)/A0-OOP/hello
	$(STYLE_CHECK) $(ASSIGNMENT)/A1/cold
	$(STYLE_CHECK) $(ASSIGNMENT)/A1-OOP/cold

# discover and run all tests
.PHONY: run-test
run-test:
	$(TEST) $(TEST_ARGS) $(ASSIGNMENT)/A0/hello/tests
	$(TEST) $(TEST_ARGS) $(ASSIGNMENT)/A0-OOP/hello/tests
	$(TEST) $(TEST_ARGS) $(ASSIGNMENT)/A1/cold/tests
	$(TEST) $(TEST_ARGS) $(ASSIGNMENT)/A1-OOP/cold/tests

.PHONY: run-test-coverage
run-test-coverage:
	$(COVERAGE) -v --cov-report=html:$(ASSIGNMENT)/A0/hello/htmlcov --cov-report=term --cov=$(ASSIGNMENT)/A0/hello $(ASSIGNMENT)/A0/hello/tests
	$(COVERAGE) -v --cov-report=html:$(ASSIGNMENT)/A0-OOP/hello/htmlcov --cov-report=term --cov=$(ASSIGNMENT)/A0-OOP/hello $(ASSIGNMENT)/A0-OOP/hello/tests
	$(COVERAGE) -v --cov-report=html:$(ASSIGNMENT)/A1/cold/htmlcov --cov-report=term --cov=$(ASSIGNMENT)/A1/cold $(ASSIGNMENT)/A1/cold/tests
	$(COVERAGE) -v --cov-report=html:$(ASSIGNMENT)/A1-OOP/cold/htmlcov --cov-report=term --cov=$(ASSIGNMENT)/A1-OOP/cold $(ASSIGNMENT)/A1-OOP/cold/tests

.PHONY: clean
clean:
	# remove all caches recursively
	rm -rf `find . -type d -name __pycache__` # remove all pycache
	rm -rf `find . -type d -name .pytest_cache` # remove all pytest cache
	rm -rf `find . -type d -name .mypy_cache` # remove all mypy cache
	rm -rf `find . -type d -name .hypothesis` # remove all hypothesis cache
	rm -rf `find . -name .coverage` # remove all coverage cache 
