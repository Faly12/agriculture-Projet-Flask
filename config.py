import os

class Config:
    SECRET_KEY = 'une_cle_secrete_longue_et_complexe'
    UPLOAD_FOLDER = 'static/uploads'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Faly@localhost/agriculture'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
