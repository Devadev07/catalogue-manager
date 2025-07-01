from backend.util.database_connection import get_db
from backend.util.response_utils import success_response, error_response
from backend.util.validators import validate_catalogue_data
from backend.dto.catalogue import Catalogue
from backend.exception.exceptions import ValidationError

def add_catalogue_service(data):
    is_valid, message = validate_catalogue_data(data)
    if not is_valid:
        raise ValidationError(message)
    
    db = get_db()
    cursor = db.cursor()
    try:
        catalogue = Catalogue(data['name'], data['start_date'], data['end_date'])
        cursor.execute(
            "INSERT INTO catalogue (catalogue_name, start_date, end_date, is_deleted) VALUES (%s, %s, %s, 0)",
            (catalogue.name, catalogue.start_date, catalogue.end_date)
        )
        db.commit()
        return success_response("Catalogue added", 201)
    except Exception as e:
        return error_response(str(e))
    finally:
        cursor.close()
        db.close()

def get_catalogues_service():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM catalogue WHERE is_deleted = 0")
        result = cursor.fetchall()
        return result
    except Exception as e:
        return error_response(str(e))
    finally:
        cursor.close()
        db.close()

def delete_catalogue_service(catalogue_id):
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("UPDATE catalogue SET is_deleted = 1 WHERE catalogue_id = %s", (catalogue_id,))
        db.commit()
        return success_response("Catalogue deleted")
    except Exception as e:
        return error_response(str(e))
    finally:
        cursor.close()
        db.close()
