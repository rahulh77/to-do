from app import app
from flask import Response, request, current_app
from app.errors import bp


@bp.app_errorhandler(404)
def page_not_found(error):
	current_app.logger.error('Page not found: %s', (request.path))
	return Response(status=404)

@bp.app_errorhandler(500)
def internal_server_error(error):
    current_app.logger.error('Server Error: %s', (error))
    return Response(status=500)

@bp.app_errorhandler(Exception)
def unhandled_exception(e):
    current_app.logger.error('Unhandled Exception: %s', (e))
    return Response(status=500)
