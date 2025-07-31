import os
from waitress import serve
from beta.wsgi import application
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

# Get port from environment variable or default to 8000
PORT = int(os.environ.get("PORT", 8000))

if __name__ == '__main__':
    logger.info(f"Starting server on port {PORT}")
    serve(application, host='0.0.0.0', port=PORT, threads=4)