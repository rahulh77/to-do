## Useful references
https://github.com/miguelgrinberg/microblog


Using Features:
- Flask
    - blueprints
    - flask config
    - error handlers
    - global handlers
    - logging (flask and gunicorn)
- Gunicorn
- MongoDB (pymongo)
- Kubernetes
    - Ingress
- Monitoring 
    - Prometheus
        - service discovery
        - promql
        - update and use new prometheus config.yml file
    - Grafana
    - Alertmanager
- load_dotenv
- Docker
    - Multistage images
    - Using local docker images (without publishing to dockerhub)
- Load generator/workbench - wrk

## Gunicorn
- using gunicorn multiworkers and kubernetes deployment multi replicas together:
- observations - all the load was going to one pod, other two pods did not get single request.
- can check pod limits for cpu and memory
- or use one gunicorn worker
- Always use multiple threads
- Try to use less workers (workers are more resource intensive)


## ApacheBench or wrk
wrk -c100 -d10s http://localhost:5001/todo


## Worker Timeout 
 add --timeout 90

## Exec to container for debug
```
kubectl run curl-debug --rm -i --tty --restart=Never --image=radial/busyboxplus:curl -- /bin/sh
```

## NodePort
Access using docker desktop
- If workers are timing out, it may take a while to appear
```
localhost:<nodeport>
or <en0 ip>:<nodeport>
```

## NGINX Ingress Controller
will create some resources in ingress-nginx namespace
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.41.2/deploy/static/provider/cloud/deploy.yaml

kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission
http://ingress-todo.info/foo
```


## Using local docker images
```
https://minikube.sigs.k8s.io/docs/handbook/pushing/
eval $(minikube docker-env)
imagePullPolicy: Never
```

## Accessing loadbalancer service with minikube
```
minikube tunnel
kubectl get svc # run this on other terminal window. will get you external ip
<EXTERNAL_IP>:8080
```

