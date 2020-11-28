
Reference:


Counter:
No. of http requests that were processed

Gauge:
no of concurrent active requests
cpu/memory usage
Current active threads

histogram:
counts no of events that fall under set of configurable bucket
used to build certain types of graphs
request duration:

Summary:
Similar to histogram - the difference is histogram has discrete values (1second, 2 second etc.) but summary has quantiles (10%, etc.) instead.

PROMQL
mobile_gateway_restarts[5m] - list of values of metric from last 5 minutes.

sum by (app, status)(flask_http_request_duration_seconds_count{app="todo",status="200"})



HTTP requests 200
sum(flask_http_request_duration_seconds_count{app="todo",status="200"})

No of pods running
sum by(app) (up{app="todo"})


Last error