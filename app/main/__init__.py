from flask import Blueprint
from decorators import admin_required, permisson_required
from .models import Permisson

main = Blueprint('main', __name__)

from . import views, errors

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)

