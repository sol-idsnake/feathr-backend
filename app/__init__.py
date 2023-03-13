from flask import Flask, render_template
from app.blueprints.admin import admin_bp
from app.blueprints.blog import blog_bp
from werkzeug.exceptions import InternalServerError, NotFound
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    register_blueprints(app)
    register_errors(app)

    return app


def register_blueprints(app):
    app.register_blueprint(admin_bp)
    app.register_blueprint(blog_bp)


def register_errors(app):
    @app.errorhandler(NotFound)
    def page_not_found(e):
        return render_template('errors/404.html')

    @app.errorhandler(InternalServerError)
    def internal_server_error(e):
        return render_template('errors/500.html')
