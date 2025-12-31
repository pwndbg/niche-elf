#!/bin/sh

set -o errexit

uv run ruff format niche_elf
uv run ruff check --fix --output-format=full niche_elf
uv run mypy --strict niche_elf
