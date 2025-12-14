<!-- Auto-generated guidance for AI coding agents working on this repo -->
# Copilot / AI agent instructions — Notes-App

Purpose
- Short, focused guidance to help AI agents be productive in this small Flask notes app.

Big picture
- Single-process Flask application implemented in `App.py`. It exposes two endpoints on `/notes` (POST to create, GET to list).
- Persistence is NOT implemented: `notes` is an in-memory Python list inside `App.py`. Any change that assumes a database must also add configuration, migration and tests.
- There are placeholder files `Dockerfile` and `nginx.conf` at repo root — both are empty. Treat them as optional/deferred unless an explicit task asks to implement containerization or webserver config.

Run / dev commands (discoverable from code)
- Run directly (quick dev):

```
python App.py
```

- Or with Flask CLI:

```
export FLASK_APP=App.py
export FLASK_ENV=development
flask run
```

- Dependencies: `App.py` imports `flask`. `requirements.txt` is currently empty; when adding deps, add `Flask` with a pinned version (e.g. `Flask>=2.0,<3`).

Key files and what they mean
- `App.py`: the entire application. Important lines/patterns:
  - `notes = []` — in-memory storage (non-persistent).
  - `@app.route("/notes", methods=["POST"])` — expects JSON body with `note` key.
  - `app.run(debug=True)` — app runs in debug mode locally.
- `requirements.txt`: present but empty. If adding libraries, update this file.
- `Dockerfile` / `nginx.conf`: present but empty placeholders. Do not assume any container or reverse-proxy behavior unless a task creates these files.

Project-specific conventions & patterns
- Single-file, minimal app: prefer small, explicit patches rather than broad refactors. If introducing new modules, update `requirements.txt` and add minimal tests.
- File name `App.py` (capital A) is part of the run pattern — keep name consistent when invoking Flask CLI.
- Avoid adding persistent storage without documenting migration and configuration: the app design currently assumes ephemeral runtime storage.

Integration points & external dependencies
- Only dependency shown by code is `flask`. There are no database connections, message queues, or external APIs.
- Because `Dockerfile` and `nginx.conf` are empty, any work that integrates Docker or NGiNX should include the new files and explicit build/run instructions in the repo or PR description.

Common tasks examples (copyable)
- Add a required dependency and make it reproducible:

```
pip install Flask
pip freeze > requirements.txt
```

- Create a new persistent notes store (example outline):
  - Add a new module `store.py` with an abstract interface.
  - Keep current in-memory store behind that interface and add a `SqliteStore` implementation.
  - Add config (e.g., `DATABASE_URL`) and a short migration / init script.

Constraints & gotchas for AI suggestions
- Do not propose changing the runtime from single-process Flask to, e.g., async frameworks, without a clear task; this repo is intentionally minimal.
- Do not assume existing CI, tests or linting — none were found. If adding them, include minimal config files and documentation in the PR.
- Because data is ephemeral, any change that claims to "persist" notes must also add the storage implementation and instructions for startup.

When editing `Dockerfile` or `nginx.conf`
- If asked to implement containerization, produce a minimal `Dockerfile` that installs `requirements.txt` and runs `python App.py` (or `gunicorn` if adding production readiness), and include build/run commands in the PR description.
- If adding `nginx.conf`, include the intended runtime topology in the PR (where nginx sits relative to Flask/gunicorn) and provide instructions to reproduce locally.

PR guidance for AI agents
- Keep changes minimal and focused — small PRs that add one capability at a time are preferred.
- Update `requirements.txt` when adding dependencies and include reproducible install commands.
- When adding persistent storage or containerization, include a short README or PR note explaining how to run locally and how new config values are provided.

If something is ambiguous, ask the repo owner for the intended direction (persisting notes, productionization, or keeping this as a learning/demo app).

---
If you'd like, I can now:
- add a minimal `requirements.txt` with `Flask`, or
- implement a basic `Dockerfile` and `nginx.conf` prototype, or
- add a tiny test harness for the `/notes` endpoints.

Please tell me which next step you prefer.
