#!/bin/sh

set -o errexit
set -o xtrace

LINT_FILES="niche_elf examples"

uv run ruff format $LINT_FILES
uv run ruff check --fix --output-format=full $LINT_FILES
uv run mypy --strict $LINT_FILES
