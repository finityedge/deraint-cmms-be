from flask_restx import Namespace, Resource, fields
from ..models.asset import Asset
from ..extensions import db

api = Namespace('assets', description='Asset operations')

asset_model = api.model('Asset', {
    'id': fields.Integer(readonly=True, description='The asset unique identifier'),
    'name': fields.String(required=True, description='The asset name'),
    'description': fields.String(description='The asset description'),
    'location': fields.String(description='The asset location'),
    'status': fields.String(description='The asset status'),
})

@api.route('/')
class AssetList(Resource):
    @api.doc('list_assets')
    @api.marshal_list_with(asset_model)
    def get(self):
        """List all assets"""
        return Asset.query.all()

    @api.doc('create_asset')
    @api.expect(asset_model)
    @api.marshal_with(asset_model, code=201)
    def post(self):
        """Create a new asset"""
        new_asset = Asset(name=api.payload['name'],
                          description=api.payload.get('description'),
                          location=api.payload.get('location'),
                          status=api.payload.get('status'))
        db.session.add(new_asset)
        db.session.commit()
        return new_asset, 201

@api.route('/<int:id>')
@api.param('id', 'The asset identifier')
@api.response(404, 'Asset not found')
class AssetItem(Resource):
    @api.doc('get_asset')
    @api.marshal_with(asset_model)
    def get(self, id):
        """Fetch an asset given its identifier"""
        return Asset.query.get_or_404(id)

    @api.doc('update_asset')
    @api.expect(asset_model)
    @api.marshal_with(asset_model)
    def put(self, id):
        """Update an asset given its identifier"""
        asset = Asset.query.get_or_404(id)
        asset.name = api.payload['name']
        asset.description = api.payload.get('description')
        asset.location = api.payload.get('location')
        asset.status = api.payload.get('status')
        db.session.commit()
        return asset

    @api.doc('delete_asset')
    @api.response(204, 'Asset deleted')
    def delete(self, id):
        """Delete an asset given its identifier"""
        asset = Asset.query.get_or_404(id)
        db.session.delete(asset)
        db.session.commit()
        return '', 204