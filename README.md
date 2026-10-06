# srvm fixture suite

Twenty-two tiny projects, one per srvm detection family, for exercising the
full zero-config flow: detect -> provision -> arbitrate a port -> spawn ->
supervise -> announce a URL -> reap on interrupt. Each directory is a plain,
self-contained project — as if scaffolded with `cargo init`, `uv init` +
`uv add flask`, or `npm create vite` — independent of the srvm repo itself.

Use it by changing into one directory and running bare `srvm`:

```
cd 04-flask
srvm
```

`srvm --dry-run` prints what would launch without spawning or installing
anything; every row below was captured from that output.

## Core fixtures

| Dir | srvm detects | Command srvm runs | Port | Prerequisites |
| --- | --- | --- | --- | --- |
| `01-static` | `static` (root `index.html`) | built-in static server (no child process) | 8000 | none |
| `02-vite` | `package:dev` (script `vite`) | `npm run dev` + `npm install`; forwards `-- --port {port}` | 5173 | node/npm |
| `03-astro` | `package:dev` (script `astro dev`) | `npm run dev` + `npm install`; forwards `-- --port {port}` | 4321 | node/npm; largest install |
| `04-flask` | `flask` | `.venv/bin/flask --app app run` + venv bootstrap; `--port {port}` | 5000 | python3 |
| `05-django` | `django` (`manage.py`) | `.venv/bin/python manage.py runserver` + venv bootstrap; `{port}` | 8000 | python3 |
| `06-fastapi` | `uvicorn` (fastapi dep + `main.py`) | `.venv/bin/uvicorn main:app --reload` + venv bootstrap; `--port {port}` | 8000 | python3 |
| `07-go` | `go` (`go.mod` + `main.go`) | `go run .`; binds `PORT`, default 7878 | 7878 (`PORT` honored) | go |
| `08-cargo` | `cargo` (`Cargo.toml` + `src/main.rs`) | `cargo run`; binds `PORT`, default 7878 | 7878 (`PORT` honored) | cargo |
| `09-streamlit` | *(pending companion rule)* `streamlit` | `streamlit run app.py` | 8501 | srvm streamlit rule, not yet landed |
| `10-monorepo` | `flask` (`apps/api`) and `package:dev` (`apps/web`) | two apps launched on distinct ports, two labeled URLs | 5000 and 3000 (`PORT` honored) | python3 and node/npm |

Notes:

- Ports are starting hints. If one is taken srvm walks forward (up to +100),
  so the announced URL can differ from the table.
- `07`, `08`, and `10/apps/web` take their port from the environment: export
  `PORT=9999` and it is honored (verified live); otherwise they fall back to
  their own defaults (7878, 3000) and print the URL they bound, which srvm
  announces.
- On macOS, AirPlay Receiver also listens on `*:5000`; flask still binds
  `127.0.0.1:5000` successfully (verified live in `10`), so no workaround is
  needed.
- `02` and `10/apps/web` contain an `index.html`, so srvm also matches `static`
  there; statics are idled whenever a real app is in the launch set, which is
  why the dry run shows `idle static`.
- `05` uses `DEBUG=True` with an empty `ALLOWED_HOSTS` (fine on loopback) and no
  database, so no `db.sqlite3` appears.

## Optional extras

These need the tool in the second column. Without it, srvm reports "no
servable app detected" (or the fallback noted below), which is expected.

| Dir | Needs | srvm detects | Command / port |
| --- | --- | --- | --- |
| `x1-compose` | docker | `compose` | `docker compose up`; port fixed at 8081 by `compose.yaml` (srvm does not arbitrate inside a stack). Without docker: static fallback serves `site/` on 8000. |
| `x2-deno` | deno | `deno` (task `dev`) | `deno task dev`; binds `PORT`, default 8000 |
| `x3-hugo` | hugo | `hugo` | `hugo server --port {port}`; 1313 |
| `x4-procfile` | foreman, overmind, or hivemind | `procfile` | `<tool> start`; binds `PORT`, default 4000. Without any: static fallback serves the root on 8000. |
| `x5-node` | node/npm | `package:dev` (opaque script) | `npm run dev` + `npm install`; binds `PORT`, default 3000 |
| `x6-gradio` | gradio rule | *(pending)* `gradio` | `gradio` app; 7860 |
| `x7-dash` | dash rule | *(pending)* `dash` | `app.run`; 8050 |
| `x8-chainlit` | chainlit rule | *(pending)* `chainlit` | `chainlit run app.py`; 8000 |
| `x9-tensorboard` | tensorboard rule | *(pending)* `tensorboard` | `tensorboard --logdir logs`; 6006; heavy install. `python write_sample_logs.py` first populates `logs/` with real curves |
| `x10-jupyter` | jupyter rule | *(pending)* `jupyter` | JupyterLab; 8888; heavy install; `notebook.ipynb` opens in the UI |
| `x11-mlflow` | mlflow rule | *(pending)* `mlflow` | `mlflow ui`; 5000; heavy install. `python train.py` first logs a demo run into `./mlruns` |
| `x12-reflex` | reflex rule | *(pending)* `reflex` | `reflex run`; 3000. Ships `rxconfig.py` + the `srvm_fixture_x12` app module; still needs `reflex init` artifacts (frontend toolchain) to fully boot |

The pending rows come from the companion plan "srvm detection rules for Python
AI/ML frameworks" (`09` and `x6`-`x12`). Until those rules land, those
directories intentionally detect nothing.

## Cold starts

No `node_modules`, `.venv`, or `target/` is shipped. The first run in a
directory exercises the bootstrap path:

- Node fixtures: `npm install` before `npm run dev`.
- Python fixtures: `python3 -m venv .venv` then
  `.venv/bin/python -m pip install -r requirements.txt`, stamped in
  `.venv/.srvm-bootstrap` so repeat runs are cheap.
- `08-cargo` compiles on first `cargo run`.

Preview everything without side effects with `srvm --dry-run`. Interrupt with
Ctrl-C; srvm reaps every child it spawned.

## Portability

All content is ASCII with LF endings, no symlinks, no absolute paths. `x4` is
unix-leaning (`${PORT:-...}` in a Procfile); the remaining fixtures are
cross-platform.
