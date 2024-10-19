from flask import Blueprint

bp = Blueprint('csdn', __name__)


from app.csdn import routes