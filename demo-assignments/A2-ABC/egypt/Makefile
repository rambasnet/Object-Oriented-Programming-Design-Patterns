PLANTUML = java -jar ~/plantuml.jar
UMLEXT = plantuml
UMLDIR = ./uml
UMLFILES = $(wildcard $(UMLDIR)/*.$(UMLEXT))
DOCS = docs

all: check-style check_types run-test run-test-coverage create-docs create-uml clean
	@echo "Make all done...!"

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

.PHONY: create-doc-folder
create-doc-folder:
	@mkdir -p $(DOCS) # creates all folder(s) if not exists

.PHONY: run-test
run-test:
ifeq ($(shell which pytest), ) # if pytest not found
	@echo "pytest not found. Installing..."
	pip install pytest
endif
	pytest --verbose --color=yes tests/
	@echo "All unittests passed!"

.PHONY: run-test-coverage
run-test-coverage: create-doc-folder
	pytest --verbose --color=yes --cov --cov-report term-missing --cov-report=html:$(DOCS)/htmlcov tests/
	@echo "All unittests passed!"

.PHONY: create-docs
create-docs: create-doc-folder
	pdoc --output-dir $(DOCS)/code-docs egypt.py kattis.py triangle.py # creates html docs
	@echo "html docs created and saved in $(DOCS)/code-docs"

.PHONY: create-uml
create-uml:
# use shell command which to check if java is installed and is in the $PATH
ifeq ($(shell which java), )
	$(error "No java found in $(PATH). Install java to run plantuml")
endif
# use wildcard function to check if file exists
ifeq ($(wildcard ~/plantuml.jar), )
	@echo "Downloading plantuml.jar in home folder..."
	curl -L -o ~/plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.jar/download
endif
	@echo "Creating UML diagrams..."
	@for file in $(UMLFILES); do \
		echo Processing $$file; \
		$(PLANTUML) $$file; \
	done
	@echo "UML diagrams created and saved in $(UMLDIR) folder"

.PHONY: cleanall
localtest:
	kattis test -m egypt.py
	@echo "Local kattis sample data test done."


.PHONY: clean
clean:
	rm -rf `find . -type d -name __pycache__`
	rm -rf `find . -type d -name .pytest_cache`
	rm -rf `find . -type d -name .mypy_cache`
	rm -rf `find . -type f -name .coverage`

