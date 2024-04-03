from mongoengine import connect

class Config:
    DEBUG = False
    TESTING = False
    DBNAME = 'ibarge'
    MONGODB_PORT = 27017
    
    MONGODB_SETTINGS = {
        'host': f'mongodb://localhost:27017/{DBNAME}',
        'authentication_source': 'admin',
        'connect': False  # برای اتصال به موقعیتی که مطمئنیم از آن استفاده می‌کنیم
    }
    HOST = '0.0.0.0'
    PORT = 8081



class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    HOST = '0.0.0.0'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

connect(**Config.MONGODB_SETTINGS)