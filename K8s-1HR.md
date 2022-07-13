### Readme for the K8s in 1 hour video

#### K8s manifest files

- mongo-config.yaml
- mongo-secret.yaml
- mongo.yaml
- webapp.yaml

#### K8s commands

##### start Minikube and check status

    minikube start --vm-driver=hyperkit
    minikube status

##### get minikube node's ip address

    minikube ip

##### get basic info about k8s components

    kubectl get node
    kubectl get pod
    kubectl get svc
    kubectl get all

##### get extended info about components

    kubectl get pod -o wide
    kubectl get node -o wide

##### get detailed info about a specific component

    kubectl describe svc {svc-name}
    kubectl describe pod {pod-name}

##### get application logs

    kubectl logs {pod-name}

##### stop your Minikube cluster

    minikube stop

<br />

> :warning: **Known issue - Minikube IP not accessible**

If you can't access the NodePort service webapp with `MinikubeIP:NodePort`, execute the following command:

    minikube service webapp-service

<br />

### TechWorld with Nana

- Kubernetes Crash Course for Absolute Beginners: <https://www.youtube.com/watch?v=s_o8dwzRlu4>
- Minikube & Kubectl explained | Setup for Beginners | ...: <https://www.youtube.com/watch?v=E2pP1MOfo3g>
- Kubectl Basic Commands - Create & Debug Pod ...: <https://www.youtube.com/watch?v=azuwXALfyRg>
- AWS EKS - Create Kubernetes cluster on Amazon EKS : <https://www.youtube.com/watch?v=p6xDCz00TxU>
- DevOps Roadmap 2022 - How to become a DevOps Engineer? : <https://www.youtube.com/watch?v=9pZ2xmsSDdo>
- What is Helm in Kubernetes? Helm and Helm Charts explained : <https://www.youtube.com/watch?v=-ykwb1d0DXU>
- Kubernetes Tutorial for Beginners [FULL COURSE in 4 Hours]: <https://www.youtube.com/watch?v=X48VuDVv0do>

#### Links

- k8s official documentation: <https://kubernetes.io/docs/home/>
- mongodb image on Docker Hub: <https://hub.docker.com/_/mongo>
- webapp image on Docker Hub: <https://hub.docker.com/repository/docker/nanajanashia/k8s-demo-app>
- webapp code repo: <https://gitlab.com/nanuchi/developing-with-docker/-/tree/feature/k8s-in-hour>
- Amazon Elastic Kubernetes Service Documentation: <https://docs.aws.amazon.com/eks/index.html>

#### Other Links

- Kubectl basics for beginners | Kubernetes: <https://www.youtube.com/watch?v=feLpGydQVio>
- kubectl - 10+ tips & tricks for Kubernetes: <https://www.youtube.com/watch?v=YejOP-lawSo>
- 7 Tips and Tricks to Enjoying Your Kubernetes Journey: <https://www.youtube.com/watch?v=RRCzgVI4ptY>
- Ready-to-use commands and tips for kubectl: <https://medium.com/flant-com/kubectl-commands-and-tips-7b33de0c5476>
- Part I : Get ready with "Minikube"ernetes: <https://gochronicles.com/minikube>
- How To Use minikube for Local Kubernetes Development and Testing: <https://www.digitalocean.com/community/tutorials/how-to-use-minikube-for-local-kubernetes-development-and-testing>
- Local Kubernetes for Mac– MiniKube vs Docker Desktop: <https://codefresh.io/blog/local-kubernetes-mac-minikube-vs-docker-desktop/>

#### Even More Other

<https://github.com/jenkinsci/configuration-as-code-plugin/tree/master/demos>
<https://github.com/marcel-dempers/docker-development-youtube-series>
<https://cloud.google.com/architecture/jenkins-on-kubernetes-engine>
<https://www.jenkins.io/doc/book/installing/kubernetes/>
