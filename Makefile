lint:
	black .
	isort .
	ruff --fix
	mypy bot utils