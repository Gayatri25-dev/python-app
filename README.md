# python-app

Simple Flask app scaffold.

Run locally:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Endpoints:
- GET / -> HTML welcome
- GET /api/health -> JSON health check
- POST /api/echo -> echoes JSON body