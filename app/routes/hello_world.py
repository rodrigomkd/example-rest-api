
"""
Hello Word endpoint
"""

from flask_restful import Resource
from flask import jsonify
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

class HelloWorld(Resource):
    """Hello World Message"""

    def get(self):
        logger.info('HelloWordl GET method')
        return jsonify({'message': 'Hello World!'})