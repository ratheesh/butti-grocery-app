# from backend import create_app
from backend import app

celery = app.extensions["celery"]
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# End of File
