# CCMS Project 2

`CI/CD Pipeline` for a `Python (Flask)` web app.

- Stored in a `Docker Hub` & `Github` Repository,
- Running on a `Docker (Kubernetes)` Network,
- Hosted by an `AWS EC2 Instance` Integrated through `Jenkins`.

![CICD Pipeline](/extras/proj2-initial-cicd.png)

## Continuous Integration

- `GitHub webhook` notifies `Jenkins` of a `push` to `main`.
- `Jenkins` then spins up an `EC2 instance` for `testing` and `building`.
- If `unittests` pass, `dcoker image` is pushed to `Docker Hub`.

## Continuous Deployment

After a successful push to `Docker Hub`, `Jenkins` uses `SSH` to `pull` and `run the latest image`.

## Development

### Local

```zsh
minikube start
```

### Cloud

```zsh
eksctl create cluster \
--name ccms-project2-cluster \
--version 1.22 \
--region us-west-1 \
--nodegroup-name linux-nodes \
--node-type t2.micro \
--nodes 2
```

### Either/Both

1. Run Blue Server/Version

  docker pull chrisbarnes2000/ccms-project2 ccms-project2

  kubectl apply -f blue.yaml
  kubectl get pods

  kubectl apply -f service.yaml

  curl $(minikube service ccms-project2 -n default --url)/ping \
  or \
  curl <http://localhost:5000/ping> \
  or \
  curl <http://ec2-IP-ADDRESS-HERE.us-east-2.compute.amazonaws.com:5000/ping> \

2. Run Green Server/Version

  docker pull chrisbarnes2000/ccms-project2:2.0 ccms-project2

  kubectl apply -f green.yaml

3. After Green Server/Version has been smoke tested/verified update `service.yaml` version to green version and archive blue
4. Start Next Feature on Blue but increase is version as it's the new Green
5. Repeat

<!--
```zsh
kubectl create namespace dev && kubectl label namespace dev istio-injection=enabled
kubectl create namespace stage && kubectl label namespace stage istio-injection=enabled
kubectl create namespace prod && kubectl label namespace prod istio-injection=enabled

helm install demoapp helm-chart/demoapp/ --wait --set deployment.tag=dev --namespace dev
helm install demoappv1 helm-chart/demoapp/ --wait --set deployment.tag=v1 --namespace prod
helm install demoappv2 helm-chart/demoapp/ --wait --set deployment.tag=v2 --namespace stage

kubectl create -f istio-config/gateway.yaml
kubectl create -f istio-config/vsvc.yaml

More Info Here: <https://github.com/infinitelambda/istio-helm-deployment> & <https://www.linkedin.com/pulse/blue-green-deployment-kubernetes-itay-melamed>
```
-->

<!--
### Setup & Run:

```bash
docker build -t ccms-project2-image
docker run -p 5000:5000 --rm --name ccms-project2-container ccms-project2-image

or

export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

<http://127.0.0.1:5000>
-->
