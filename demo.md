# Stage script: Smooth project setup with mise and uv

## 1. Prepare before the room fills (not part of the live demo)

Use the same laptop, terminal and network as the talk. Complete README
[Step zero](README.md#step-zero). Open a fresh terminal outside any other
project or activated venv. Use zsh or Bash with `mise activate`, not only shims.
Run each command separately and let the prompt return: shell activation runs
at prompt boundaries.

Rehearse the clone and install once to warm the mise and uv download caches.
Keep that working checkout in another directory as a fallback. The requested
`latest` uv/Ruff selectors and Python `3.14` can resolve newer releases later;
rehearse again on Thursday. A cold install needs network access. Warm caches
reduce downloads but do not guarantee an offline install.

## 2. Show the before slide (0–5 minutes)

Show [docs/before.md](docs/before.md): pyenv, venv, pip, direnv, Makefile.
Explain that uv handles packages and mise handles the surrounding project setup.

In a fresh terminal outside any project:

```sh
which python
echo $VIRTUAL_ENV
```

Expect the machine's normal Python (or `python not found`) and a blank
`VIRTUAL_ENV`. Record this baseline; it should return when leaving the project.

## 3. Clone, trust, install (5–12 minutes)

Use a new empty parent directory for each rehearsal:

```sh
mkdir -p ~/mise-meetup
cd ~/mise-meetup
git clone https://github.com/laojala/mise-uv-demo.git
cd mise-uv-demo
cat mise.toml
mise trust
mise install
```

After clone: a small src-layout package, config, tests and lockfile. On entry,
mise may warn that the config is untrusted; this is expected. Read the config
before trusting it: trust allows its environment and hooks to execute.
`mise trust` confirms the directory. `mise install` installs/selects Python
3.14, uv and Ruff, then `uv sync --locked` installs the local package, Rich,
pytest and their dependencies. Cached tools may produce no download output.
A missing `.venv` may be created at the prompt immediately after trust.

```sh
which python
echo $VIRTUAL_ENV
mise run hello
```

Expect `.../mise-uv-demo/.venv/bin/python` and
`.../mise-uv-demo/.venv`. Hello prints:

```text
Hello from mise!
Text: "mise and uv make setup smooth"
6 words, 6 unique words, 29 characters
```

## 4. Leave, return, test (12–20 minutes)

Run these as separate commands, waiting for each prompt:

```sh
cd ..
which python
echo $VIRTUAL_ENV
```

Expect the original Python path (or `python not found`) and a blank
`VIRTUAL_ENV`: the project venv is deactivated.

```sh
cd mise-uv-demo
which python
echo $VIRTUAL_ENV
mise run test
mise run lint
```

Expect `.venv/bin/python` and the project `.venv` again, without `source`.
Tests show `8 passed` in under two seconds; lint prints `All checks passed!`.
Each task also prints the command mise runs. No test or app makes network calls.

## 5. Explain the file and CI (20–25 minutes, questions to 30)

Show the README block-to-tool table, `pyproject.toml`, `uv.lock` and
`.github/workflows/ci.yml`. The action installs with the same postinstall hook,
then runs the same test and lint tasks on Linux.

Optional final command:

```sh
mise run fmt
```

Expect the Python files to be unchanged. If anything fails on stage, switch
to the rehearsed checkout; do not troubleshoot network or shell setup live.
