from flask import jsonify


class APIResponse:
    @staticmethod
    def respond(data=None, error=None, status=200):
        response = {}
        if error is not None:
            response['error'] = error
        if data is not None:
            response['data'] = data
        return jsonify(response), status
