# For local testing replace with 127.0.0.1,
# for production deployment use your actual domain
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# If set to 'LOCAL', it will use daphne dev server to handle
# both HTTP and websocket connections
ENVIRONMENT = 'LOCAL'
