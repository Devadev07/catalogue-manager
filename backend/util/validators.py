def validate_catalogue_data(data):
    if not data.get('name') or not data.get('start_date') or not data.get('end_date'):
        return False, "All fields are required"
    return True, ""
