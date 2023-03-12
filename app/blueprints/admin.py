from flask import Blueprint, render_template, url_for, send_file, redirect
from os import path, getcwd
from datetime import datetime

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/flask-admin')
def adminPanel():
    # auth for demonstration purposes
    name = "admin"

    return render_template(
        "admin/index.html",
        name=name,
        date=datetime.now()
    )


@admin_bp.route('/api/water')
def water():
    SITE_ROOT = path.abspath(path.dirname(path.dirname(__file__)))
    json_url = path.join(SITE_ROOT, "static", "gru-water.pdf")

    return send_file(json_url, mimetype='application/pdf', as_attachment=True, download_name="gru-water.pdf")
