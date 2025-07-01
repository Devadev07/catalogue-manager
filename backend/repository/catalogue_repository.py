from backend.util.database_connection import get_db
from backend.dto.catalogue import Catalogue

class CatalogueRepository:

    @staticmethod
    def add_catalogue(catalogue: Catalogue):
        db = get_db()
        cursor = db.cursor()
        try:
            cursor.execute(
                "INSERT INTO catalogue (catalogue_name, start_date, end_date, is_deleted) VALUES (%s, %s, %s, 0)",
                (catalogue.name, catalogue.start_date, catalogue.end_date)
            )
            db.commit()
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def get_all_catalogues():
        db = get_db()
        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM catalogue WHERE is_deleted = 0")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
  # returning DTO objects
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def delete_catalogue(catalogue_id: int):
        db = get_db()
        cursor = db.cursor()
        try:
            cursor.execute("UPDATE catalogue SET is_deleted = 1 WHERE catalogue_id = %s", (catalogue_id,))
            db.commit()
        finally:
            cursor.close()
            db.close()
