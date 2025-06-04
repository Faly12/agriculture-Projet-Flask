import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Faly@localhost:5432/agriculture'
    SQLALCHEMY_TRACK_MODIFICATIONS = False