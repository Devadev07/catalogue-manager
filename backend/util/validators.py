def validate_catalogue_data(data):
    required_fields = ['name', 'start_date', 'end_date']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"{field} is required"
    return True, ""
