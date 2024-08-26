def register_modules(app):
    from .assets import assets
    # from .work_orders import work_orders
    # Import and register other modules

    url_prefix = '/api/v1'

    app.register_blueprint(assets, url_prefix=url_prefix)
    # app.register_blueprint(work_orders, url_prefix='/api/v1')
    # Register other blueprints