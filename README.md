# CCMS Project 2

`CI/CD Pipeline` for a `Python (Flask)` web app.

- Stored in a `Docker Hub` registry & `GitHub` repository,
- Running on a `Docker (Kubernetes)` Network,
- Hosted by an `AWS EKS` cloud cluster and Integrated through `Jenkins`.
- Something `Jenkins`

![CICD Pipeline](./extras/proj2-initial-cicd.png)

## Continuous Integration

- `GitHub webhook` notifies `Jenkins` of a `push` to `main`.
- `Jenkins` then uses an `EC2 instance` agent for `testing` and `building`.
- If `unittests` pass, `docker image` is pushed to `Docker Hub`.

## Continuous Deployment

After a successful push to `Docker Hub`, `Jenkins` uses `SSH` to directs `Kubernetes` to update the `cluster`.

## Local Development

### Setup & Run:

```bash
docker build . -t ccms-project2-image

docker run -p 5000:5000 --rm --name ccms-project2-container ccms-project2-image

or

export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

<http://127.0.0.1:5000>

## Kubernetes Development:

### Initial Setup & Run

1. eksctl create cluster --name p2 --version 1.19 --region us-east-2 --nodegroup-name standard-nodes --node-type t3.small --nodes 2 --managed --node-ami-family Ubuntu2004
2. kubectl apply -f .yaml
3. kubectl apply -f .yaml
4. kubectl apply -f .yaml

### Zero Downtime Deployment

****dfsdfsdfs*****