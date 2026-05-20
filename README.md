# python-app

Simple Flask app scaffold.

Run locally:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python application.py
```

Deploy to AWS Elastic Beanstalk:

```bash
eb init -p python-3.11 my-app
eb create my-app-env
eb deploy
```

The app includes a `Procfile` and `.ebextensions/python.config` so Elastic Beanstalk can load `application:application`.

Endpoints:
- GET / -> HTML welcome
- GET /api/health -> JSON health check
- POST /api/echo -> echoes JSON body