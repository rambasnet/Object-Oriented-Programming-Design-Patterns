TEST = pytest
TEST_ARGS = -s --verbose --color=yes
TYPE_CHECK = mypy --strict --allow-untyped-decorators --ignore-missing-imports
STYLE_CHECK = flake8
COVERAGE = python -m pytest
DEMO = './demo-assignments'

.PHONY: all
all: check-style check-type run-test run-test-coverage clean
	@echo "All checks passed!"

.PHONY: check-type
check-type:
	$(TYPE_CHECK) $(DEMO)/A0/hello
	$(TYPE_CHECK) $(DEMO)/A0-OOP/hello
	$(TYPE_CHECK) $(DEMO)/A1/cold
	$(TYPE_CHECK) $(DEMO)/A1-OOP/cold
	$(TYPE_CHECK) $(DEMO)/A2-ABC/egypt

.PHONY: check-style
check-style:
	$(STYLE_CHECK) $(DEMO)/A0/hello
	$(STYLE_CHECK) $(DEMO)/A0-OOP/hello
	$(STYLE_CHECK) $(DEMO)/A1/cold
	$(STYLE_CHECK) $(DEMO)/A1-OOP/cold
	$(STYLE_CHECK) $(DEMO)/A2-ABC/egypt

# discover and run all tests
.PHONY: run-test
run-test:
	$(TEST) $(TEST_ARGS) $(DEMO)/A0/hello/tests
	$(TEST) $(TEST_ARGS) $(DEMO)/A0-OOP/hello/tests
	$(TEST) $(TEST_ARGS) $(DEMO)/A1/cold/tests
	$(TEST) $(TEST_ARGS) $(DEMO)/A1-OOP/cold/tests
	$(TEST) $(TEST_ARGS) $(DEMO)/A2-ABC/egypt/tests

.PHONY: run-test-coverage
run-test-coverage:
	$(COVERAGE) -v --cov-report=term-missing --cov=$(DEMO)/A0/hello $(DEMO)/A0/hello/tests
	$(COVERAGE) -v --cov-report=term-missing --cov=$(DEMO)/A0-OOP/hello $(DEMO)/A0-OOP/hello/tests
	$(COVERAGE) -v --cov-report=term-missing --cov=$(DEMO)/A1/cold $(DEMO)/A1/cold/tests
	$(COVERAGE) -v --cov-report=term-missing --cov=$(DEMO)/A1-OOP/cold $(DEMO)/A1-OOP/cold/tests
	$(COVERAGE) -v --cov-report=term-missing --cov=$(DEMO)/A2-ABC/egypt $(DEMO)/A2-ABC/egypt/tests

.PHONY: clean
clean:
	# remove all caches recursively
	rm -rf `find . -type d -name __pycache__` # remove all pycache
	rm -rf `find . -type d -name .pytest_cache` # remove all pytest cache
	rm -rf `find . -type d -name .mypy_cache` # remove all mypy cache
	rm -rf `find . -type d -name .hypothesis` # remove all hypothesis cache
	rm -rf `find . -name .coverage` # remove all coverage cache 
