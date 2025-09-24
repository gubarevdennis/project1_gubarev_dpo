PYTHON = python3
PIP = pip3

project:
	poetry run project

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	$(PIP) install dist/*.whl

make lint:
	poetry run ruff check .