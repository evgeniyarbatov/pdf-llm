.PHONY: all venv install seed

VENV_PATH = ~/.venv/pdf-llm-seed
PYTHON = python3.12
DOCS_DIR = ./documents

all: venv install seed

venv:
	$(PYTHON) -m venv $(VENV_PATH)

install:
	source $(VENV_PATH)/bin/activate && pip install -r db/requirements.txt

seed:
	source $(VENV_PATH)/bin/activate && $(PYTHON) db/seed.py $(DOCS_DIR)
