from backend.util.database_connection import get_db
from backend.dto.catalogue import Catalogue

class CatalogueRepository:

    @staticmethod
    def add_catalogue(catalogue: Catalogue):
        db = get_db()
        cursor = db.cursor()
        try:
            cursor.execute(
                "INSERT INTO catalogue (catalogue_name, start_date, end_date) VALUES (%s, %s, %s)",
                (catalogue.name, catalogue.start_date, catalogue.end_date)
            )
            db.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def get_all_catalogues():
        db = get_db()
        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute("SELECT catalogue_id, catalogue_name, start_date, end_date FROM catalogue WHERE is_deleted=0")
            rows = cursor.fetchall()
            return [
                {
                    "catalogue_id": row["catalogue_id"],
                    "catalogue_name": row["catalogue_name"],
                    "start_date": str(row["start_date"]),
                    "end_date": str(row["end_date"])
                }
                for row in rows
            ]
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def delete_catalogue(catalogue_id: int):
        db = get_db()
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM catalogue WHERE catalogue_id = %s", (catalogue_id,))
            db.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            db.close()