from flask import Blueprint, jsonify, request
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

delivery_routes_bp = Blueprint("delivery_routes", __name__)

@delivery_routes_bp.route('/delivery/order', methods=["POST"])
def registry_order():
    http_request = HttpRequest(body= request.json)

    http_response = HttpResponse()
    return jsonify(http_response.body), http_response.status_code

