from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from backend.services.catalogue_service import (
    add_catalogue_service, get_catalogues_service, delete_catalogue_service
)
from backend.exception.exceptions import ValidationError

app = Flask(
    __name__,
    template_folder='frontend/templates',
    static_folder='frontend/static'        
)

CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalogues', methods=['POST'])
def add_catalogue():
    data = request.get_json()
    try:
        return add_catalogue_service(data)
    except ValidationError as ve:
        return jsonify({"status": "error", "message": str(ve)}), 400

@app.route('/getCatalogues', methods=['GET'])
def get_catalogues():
    return jsonify(get_catalogues_service())

@app.route('/deleteCatalogue', methods=['POST'])
def delete_catalogue():
    data = request.get_json()
    return delete_catalogue_service(data.get('id'))

if __name__ == '__main__':
    app.run(debug=True)
