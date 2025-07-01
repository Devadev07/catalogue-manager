from flask import jsonify

def success_response(message, status_code=200):
    return jsonify({"status": "success", "message": message}), status_code

def error_response(message, status_code=500):
    return jsonify({"status": "error", "message": message}), status_code
