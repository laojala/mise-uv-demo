# Demo notes

Beforehand: activate mise in the shell, rehearse once to warm caches,
and keep a working checkout ready. Wait for each prompt between commands.

```sh
git clone https://github.com/laojala/mise-uv-demo.git
cd mise-uv-demo
mise trust
mise install

mise run hello                # Hello from mise! + word counts
python --version              # 3.14.x
cd older-python
python --version              # 3.13.x
echo $APP_GREETING            # inherited: Hello from mise!
cd ..
python --version              # 3.14.x

mise run test
mise run lint
```

Show `docs/before.md`, both `mise.toml` files, `uv.lock` and CI.
uv manages the ignored `.venv`; no manual activation. The child disables its
activation to show the selected Python. Keep package tasks at the root.
Cold installs need network access.
