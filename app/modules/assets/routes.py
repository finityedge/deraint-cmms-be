from flask import jsonify, request
from . import assets
from ...models.asset import Asset
from ...extensions import db

@assets.route('/assets', methods=['GET'])
def get_assets():
    assets = Asset.query.all()
    return jsonify([{'id': a.id, 'name': a.name, 'status': a.status} for a in assets])

@assets.route('/assets', methods=['POST'])
def create_asset():
    data = request.json
    new_asset = Asset(name=data['name'], description=data.get('description'), location=data.get('location'), status=data.get('status'))
    db.session.add(new_asset)
    db.session.commit()
    return jsonify({'id': new_asset.id, 'name': new_asset.name}), 201