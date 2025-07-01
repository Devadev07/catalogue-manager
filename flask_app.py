from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from backend.services.catalogue_service import (CatalogueService)
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
        return CatalogueService.add_catalogue(data)
    except ValidationError as ve:
        return jsonify({"status": "error", "message": str(ve)}), 400

@app.route('/catalogues', methods=['GET'])
def get_catalogues():
    return CatalogueService.get_all_catalogues()

@app.route('/deleteCatalogue', methods=['POST'])
def delete_catalogue():
    data = request.get_json()
    return CatalogueService.delete_catalogue(data.get('id'))

if __name__ == '__main__':
    app.run(debug=True)
