SHELL:=/bin/bash

create-venv:
	rm -rf .venv || true
	python -m venv .venv

create-dev-venv:
	rm -rf .venv-dev || true
	python -m venv .venv-dev

activate-venv:
	. .venv/bin/activate

activate-dev-venv:
	. .venv-dev/bin/activate

install-deps:
	@( \
		. .venv/bin/activate; \
		pip install .; \
	)

install-build-deps:
	@( \
		. .venv-dev/bin/activate; \
		pip install .[build]; \
	)

install-lint-deps:
	@( \
		. .venv-dev/bin/activate; \
		pip install .[lint]; \
	)

install-test-deps:
	@( \
		. .venv-dev/bin/activate; \
		pip install .[test]; \
	)

lint:
	@( \
		. .venv-dev/bin/activate; \
		ruff check \
	)

build:
	@( \
		. .venv-dev/bin/activate; \
		python -m build \
	)

test:
	@( \
		. .venv-dev/bin/activate; \
		pytest \
	)

semantic-release:
	docker build --progress=plain -f .dev/semantic-release/Dockerfile -t semantic-release .
	docker run --rm --name sr -e GITHUB_TOKEN=${GITHUB_TOKEN} -v "${PWD}":/app  -v ~/.ssh:/root/.ssh/ semantic-release