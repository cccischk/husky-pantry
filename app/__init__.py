from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import blueprints, routes, etc.
    from app import routes
    app.register_blueprint(routes.bp)
    
    return app