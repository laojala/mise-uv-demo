# Before: separate tools and setup steps

Assume Git, pyenv, direnv and Make are already installed, with pyenv and direnv
hooks configured in the shell. From a fresh clone:

```sh
pyenv install -s 3.14
pyenv local "$(pyenv latest 3.14)"
python -m venv .venv
. .venv/bin/activate
python -m pip install -e . --group dev ruff
printf 'source .venv/bin/activate\nexport APP_GREETING="Hello from mise!"\n' > .envrc
direnv allow
```

`pip --group` needs pip 25.1 or newer. These illustrative pip installs do not
consume `uv.lock`, so they do not provide the same locked dependency versions.

Then write a `Makefile` (recipe indentation is a tab):

```makefile
.PHONY: test lint fmt hello
test:
	.venv/bin/python -m pytest
lint:
	.venv/bin/ruff check .
fmt:
	.venv/bin/ruff format .
hello:
	.venv/bin/mise-uv-demo
```

```sh
make test
make lint
make hello
```

After: `mise trust` and `mise install`. One `mise.toml` supplies the tool
selection, venv activation, project environment and named commands locally
and in CI; uv supplies the locked dependency sync.
