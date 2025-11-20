DOCS = docs
PYTHON = python3
PLANTUML = java -jar ~/plantuml.jar
UMLFILES = $(wildcard ./uml/*.plantuml)
SRC_FILES = $(wildcard src/*.py)

.PHONY: all
all: check-style fix-style check-types run-test run-test-coverage create-docs create-uml clean
	@echo "All done!"

.PHONY: check-style
check-style:
	flake8 .

.PHONY: fix-style
fix-style:
	autopep8 --in-place --recursive --aggressive --aggressive .

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

.PHONY: check-types
check-types:
# use shell command which to check if mypy is installed and is in $PATH
ifeq ($(shell which mypy), )
	@echo "mypy not found. Installing mypy..."
	pip install mypy
endif
	mypy --disallow-untyped-defs --strict .
	@echo "Type checking done."

.PHONY: create-doc-folder
create-doc-folder:
	@mkdir -p $(DOCS) # creates all folder(s) if not exists

.PHONY: create-docs
create-docs: create-doc-folder
	pdoc --output-dir $(DOCS)/code-docs $(SRC_FILES) # creates html docs
	@echo "html docs created and saved in $(DOCS)/code-docs"

.PHONY: create-uml
create-uml: create-doc-folder
# use shell command which to check if java is installed and is in the $PATH
ifeq ($(shell which java), )
	$(error "No java found in $(PATH). Install java to run plantuml")
endif
# use wildcard function to check if file exists
ifeq ($(wildcard ~/plantuml.jar), )
	@echo "Downloading plantuml.jar in home folder..."
	curl -L -o ~/plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.jar/download
	sudo apt install graphviz
endif
	@echo "Creating UML diagrams..."
	@for umlfile in $(UMLFILES); do \
		echo "Processing $$umlfile..."; \
		$(PLANTUML) $$umlfile; \
	done
	@echo "UML diagrams created and saved in uml folder"


.PHONY: clean
clean:
	# remove all caches recursively
	rm -rf `find . -type d -name __pycache__` # remove all pycache
	rm -rf `find . -type d -name .pytest_cache` # remove all pytest cache
	rm -rf `find . -type d -name .mypy_cache` # remove all mypy cache
	rm -rf `find . -type d -name .hypothesis` # remove all hypothesis cache
	rm -rf `find . -name .coverage` # remove all coverage cache 