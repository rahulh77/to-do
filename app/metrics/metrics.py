from app import metrics
from prometheus_client.registry import CollectorRegistry
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
from prometheus_flask_exporter import Counter, Gauge, Histogram
from flask import request


http_request_size_bytes = Histogram('http_request_size_bytes', 'HTTP request size in bytes',
                                    ['method', 'endpoint'])

http_response_size_bytes = Histogram('http_response_size_bytes', 'HTTP response size in bytes',
                                        ['method', 'endpoint'])

http_request_count = Counter('http_request_count', 'HTTP Request Count', ['method', 'endpoint', 'http_status'])
http_concurrent_request_count = Gauge('http_concurrent_request_count', 'Flask Concurrent Request Count')


def init_metrics(app):
    myapp = GunicornInternalPrometheusMetrics(app, registry=CollectorRegistry())
    # app.before_request(before_request)
    # app.after_request(after_request)
    

