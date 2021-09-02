"""
Random message endpoint
"""

from flask_restful import Resource
from flask import abort, jsonify
import requests
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

API = "https://official-joke-api.appspot.com/jokes/programming/random"

class RandomMessage(Resource):
    """Random Message from API Service"""
    
    def get(self):
        logger.info(f'Getting message from Service: {API}')
        req = requests.get(API)

        if req.status_code != 200:
            logger.error(f'Service error status code: {req.status_code}, response: {req.json()}')
            abort(503, description="Failed. Service Unavailable.")
        if len(req.json()) == 0:
            logger.error(f'Service failed parsing response: {req.json()}')
            abort(500, description="Failed. Parsing service response.")

        return jsonify(req.json()[0])