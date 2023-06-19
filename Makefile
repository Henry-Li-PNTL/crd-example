

.PHONY: install run

install:
	poetry install

run:
	kopf src/provisioner/main.py
	# poetry run uvicorn src.provisioner.main:app --host 0.0.0.0 --port 8004 --reload

