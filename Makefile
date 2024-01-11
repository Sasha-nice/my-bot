lint:
	black .
	isort .
	ruff --fix