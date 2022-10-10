def api_response(status, type, message):
    response = {}
    response["status"] = status
    response["type"] = type
    response["message"] = message
    return response
