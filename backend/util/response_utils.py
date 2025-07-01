from flask import jsonify

def success_response(message, code=200):
    return jsonify({"status": "success", "message": message}), code

def error_response(message, code=500):
    return jsonify({"status": "error", "message": message}), code
