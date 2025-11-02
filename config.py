import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'change_this_secret')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'change_this_jwt_secret')
    MONGO_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/threatforge')
    CELERY_BROKER_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
