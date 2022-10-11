def api_response(status, type, message):
    """
    Create and return a response dictionary.

    Args:
        status (int): Restframework status code
        type (string): Resposne type from swaggerpetstore/core/constants
        message (string): Message from swaggerpetstore/core/constants
    Returns:
        response dictionary
    """
    response = {}
    response["status"] = status
    response["type"] = type
    response["message"] = message
    return response
