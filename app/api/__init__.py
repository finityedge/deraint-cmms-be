from flask_restx import Api

api = Api(
    title='CMMS API',
    version='1.0',
    description='A Computerized Maintenance Management System API',
)

# Import and add namespaces
from .assets import api as assets_ns
# from .work_orders import api as work_orders_ns
# Import other namespaces as you create them

api.add_namespace(assets_ns)
# api.add_namespace(work_orders_ns)
# Add other namespaces