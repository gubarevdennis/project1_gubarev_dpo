PYTHON = python3
PIP = pip3

install:
	poetry install

build:
    poetry build

publish:
    poetry publish --dry-run

package-install:
    $(PIP) install dist/*.whl # Используем переменную PIP для большей гибкости