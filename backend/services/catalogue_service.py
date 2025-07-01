from backend.dto.catalogue import Catalogue
from backend.repository.catalogue_repository import CatalogueRepository
from backend.util.validators import validate_catalogue_data
from backend.util.response_utils import success_response, error_response
from backend.exception.exceptions import ValidationError
from flask import jsonify

class CatalogueService:

    @staticmethod
    def add_catalogue(data):
        valid, msg = validate_catalogue_data(data)
        if not valid:
            raise ValidationError(msg)
        catalogue = Catalogue(
            name=data['name'],
            start_date=data['start_date'],
            end_date=data['end_date']
        )
        CatalogueRepository.add_catalogue(catalogue)
        return success_response("Catalogue added successfully", 201)

    @staticmethod
    def get_all_catalogues():
        try:
            print("Fetching catalogues...")  
            catalogues = CatalogueRepository.get_all_catalogues()
            print("Fetched:", catalogues)    
            return jsonify(catalogues), 200
        except Exception as e:
            print("Error:", e)               
            return error_response(str(e), 500)

    @staticmethod
    def delete_catalogue(catalogue_id):
        if not catalogue_id:
            return error_response("Catalogue ID is required", 400)
        deleted = CatalogueRepository.delete_catalogue(catalogue_id)
        if deleted:
            return success_response("Catalogue deleted successfully")
        else:
            return error_response("Catalogue not found", 404)