# to-do


## To run
``` bash
make init
make build
make run
make kill

./start.sh 
or
python run-app.py
```


```
localhost:5000
localhost:5000/metrics
localhost:5000/dashboard
docker run -it --rm --entrypoint /bin/sh todo_flask

kubectl port-forward svc/to-do 5001:5001
localhost:5001
```

using gunicorn multiworkers and kubernetes deployment multi replicas together:
observations - all the load was going to one pod, other two pods did not get single request.
can check pod limits for cpu and memory

or use one gunicorn worker

ApacheBench or wrk
wrk -c100 -d10s http://localhost:5001/todo

WORKER TIMEOUT - add --timeout 90
kubectl run curl-debug --rm -i --tty --restart=Never --image=radial/busyboxplus:curl -- /bin/sh

NodePort
Access using docker desktop
If workers are timing out, it may take a while to appear
localhost:<nodeport>
or <en0 ip>:<nodeport>

## NGINX Ingress Controller
### will create some resources in ingress-nginx namespace
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.41.2/deploy/static/provider/cloud/deploy.yaml

kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission

### using local docker images
# https://minikube.sigs.k8s.io/docs/handbook/pushing/
eval $(minikube docker-env)
imagePullPolicy: Never

### accessing loadbalancer service with minikube
minikube tunnel
kubectl get svc # run this on other terminal window. will get you external ip
<EXTERNAL_IP>:8080

Always use multiple threads
Try to use less workers (workers are more resource intensive)