from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES
# from flask_comment import Comment

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.strong'


bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
# photos = Uploadset('photos',IMAGES)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    
    app = Flask(__name__)
    
    #Creating app configurations
    
    app.config.from_object(config_options[config_name])
    app.config['SECRET_KEY']='fbc3e941d1ae812c676fee4b7f0eac543d4dd747'
    
    #Initialing bootstrap
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    #Registering Blueprints
    from app.auth import auth as auth_blueprint
    from app.main import main as main_blueprint
    from app.blogs import blogs as blogs_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint,url_prefix='/auth')
    app.register_blueprint(blogs_blueprint, url_prefix = '/')
    
    # configure uploads
    # configure_uploads(app,photos)
    
    return app
