# Smooth project setup with mise and uv

A tiny word counter for a 20–30 minute meetup demo. Python tools, a virtual
environment, environment variables and commands live in `mise.toml`;
uv manages the package and locked dependencies.

## Step zero

Install [mise](https://mise.jdx.dev/getting-started.html) once. On macOS:

```sh
brew install mise
```

Add the activation line to your shell config, then open a new terminal:

```sh
# ~/.zshrc
eval "$(mise activate zsh)"
# For Bash, use eval "$(mise activate bash)" in ~/.bashrc instead.
```

Use mise 2026.7.0 or newer for the string form of `python.uv_venv_auto`.
Git and network access are needed for the first clone and dependency downloads.

## Two commands after cloning

```sh
git clone https://github.com/laojala/mise-uv-demo.git
cd mise-uv-demo
```

Read `mise.toml`, then:

```sh
mise trust
mise install
```

The postinstall hook runs `uv sync --locked`, including on repeat installs.
At the next shell prompt, `.venv/bin/python` is active. Try:

```sh
mise run test
mise run lint
mise run hello
mise run fmt
```

## How it works

| Block in `mise.toml` | Job | Replaces |
| --- | --- | --- |
| `[tools]` | Installs Python 3.14, uv and an isolated Ruff CLI | pyenv and manual CLI installs |
| `[settings]` | Creates/sources uv's `.venv` on entry; restores the shell on exit | `python -m venv` and manual activation |
| `[env]` | Points uv at mise's Python and sets `APP_GREETING` within the project | direnv / `.envrc` |
| `[hooks]` | Syncs the package, Rich and pytest from `uv.lock` after installation | Manual dependency installation |
| `[tasks.*]` | Names the test, lint, format and hello commands | Makefile |

uv owns application dependencies; mise owns tools and the shell environment.
Ruff runs from mise's isolated PyPI tool environment, outside the project venv.
CI uses the same config through `jdx/mise-action`, with both actions pinned to
full commit SHAs.

See [the before slide](docs/before.md) and [the stage script](demo.md).
The config follows the current [Python docs](https://mise.jdx.dev/lang/python.html)
and [Python cookbook](https://mise.jdx.dev/mise-cookbook/python.html).
