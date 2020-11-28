from app import app
from flask import Response, request, current_app
from app.globalhandlers import bp
from app.metrics import metrics

@app.before_request
def before_request():
    current_app.logger.debug('before request called')
    # metrics.http_concurrent_request_count.inc()
    # content_length = request.content_length
    # if (content_length):
    #     metrics.http_request_size_bytes.labels(request.method, request.path).observe(content_length)

@app.after_request
def after_request(response):
    current_app.logger.debug('after request called')
    # metrics.http_concurrent_request_count.dec()
    # metrics.http_request_count.labels(request.method, request.path, response.status_code).inc()
    # metrics.http_response_size_bytes.labels(request.method, request.path).observe(response.calculate_content_length())
    return response