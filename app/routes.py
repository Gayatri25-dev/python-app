from flask import Blueprint, jsonify, request

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return "<h1>Simple Flask App</h1><p>Visit <a href='/api/health'>/api/health</a></p>"

@bp.route("/api/health")
def health():
    return jsonify(status="ok")

@bp.route("/api/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True)
    return jsonify(received=data or {})
