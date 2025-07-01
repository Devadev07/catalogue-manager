from backend.dto.catalogue import Catalogue
from backend.repository.catalogue_repository import CatalogueRepository
from backend.util.validators import validate_catalogue_data
from backend.util.response_utils import success_response, error_response
from backend.exception.exceptions import ValidationError

class CatalogueService:

    @staticmethod
    def get_all_catalogues():
        try:
            catalogues = CatalogueRepository.get_all_catalogues()
            return success_response([cat.to_dict() for cat in catalogues])
        except Exception as e:
            return error_response(str(e))

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
    def delete_catalogue(catalogue_id):
        try:
            CatalogueRepository.delete_catalogue(catalogue_id)
            return success_response("Catalogue deleted")
        except Exception as e:
            return error_response(str(e))
