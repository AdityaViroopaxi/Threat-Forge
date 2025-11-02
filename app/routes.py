from flask import Blueprint, jsonify, request, render_template
from .models import ioc_schema
from .scoring import calculate_risk_score

bp = Blueprint('main', __name__)

@bp.route('/dashboard')
def dashboard():
    # Query and render analytics
    return render_template('dashboard.html')

@bp.route('/lookup', methods=['GET', 'POST'])
def lookup():
    # IOC search
    if request.method == 'POST':
        # Validate input, query DB, return result
        pass
    return render_template('lookup.html')

@bp.route('/alerts')
def alerts():
    # Fetch high risk IOCs
    return render_template('alerts.html')

@bp.route('/api/ioc/<value>', methods=['GET'])
def api_ioc(value):
    # REST API endpoint
    pass
