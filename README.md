# Team Dashboard

A simple web-app for showing data relevant to a team; designed to be displayed on a TV.

## Tech stack

- Flask/Gunicorn
- HTMX

## Run locally

### Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run Flask

```bash
python app.py
```

Open your browser at http://localhost:5001

### Edit data

You can either edit the data directly in the UI or in the `data/store.json` file.
