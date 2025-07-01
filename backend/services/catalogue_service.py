from backend.dto.catalogue import Catalogue
from backend.repository.catalogue_repository import CatalogueRepository
from backend.util.validators import validate_catalogue_data
from backend.util.response_utils import success_response, error_response
from backend.exception.exceptions import ValidationError
from flask import jsonify


class CatalogueService:

    @staticmethod
    def get_all_catalogues():
        try:
            catalogues = CatalogueRepository.get_all_catalogues()
            return jsonify(catalogues), 200  # ✅ This is already a Response object
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
        
    @staticmethod
    def add_catalogue(data):
        is_valid, message = validate_catalogue_data(data)
        if not is_valid:
            raise ValidationError(message)
        
        try:
            catalogue = Catalogue(data['name'], data['start_date'], data['end_date'])
            CatalogueRepository.add_catalogue(catalogue)
            return success_response("Catalogue added", 201)
        except Exception as e:
            return error_response(str(e))

    @staticmethod
    def get_all_catalogues():
        try:
            catalogues = CatalogueRepository.get_all_catalogues()
            # convert DTOs to dicts for JSON response
            return [cat.to_dict() for cat in catalogues]
        except Exception as e:
            return error_response(str(e))

    @staticmethod
    def delete_catalogue(catalogue_id):
        try:
            CatalogueRepository.delete_catalogue(catalogue_id)
            return success_response("Catalogue deleted")
        except Exception as e:
            return error_response(str(e))
