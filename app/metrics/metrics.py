from prometheus_client import registry
from prometheus_client.registry import CollectorRegistry
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
from prometheus_flask_exporter import Counter, Gauge, Histogram, Summary

def init_metrics(app):
    GunicornInternalPrometheusMetrics(app, registry=CollectorRegistry())

