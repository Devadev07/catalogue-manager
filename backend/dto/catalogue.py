class Catalogue:
    def __init__(self, name, start_date, end_date, catalogue_id=None):
        self.catalogue_id = catalogue_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    def to_dict(self):
        return {
            "catalogue_id": self.catalogue_id,
            "catalogue_name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
