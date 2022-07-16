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

> :warning: **Possible fix** - Add Minikube tune to service \

- <https://minikube.sigs.k8s.io/docs/handbook/accessing> \
- <https://shubham-singh98.medium.com/minikube-dashboard-in-aws-ec2-881143a2209e>

  STEP 1: Run minikube dashboard on EC2 instance and note down the url

  $ minikube dashboard --url

  STEP 2: Open another terminal and create an SSH Tunnel

  ssh -i <LOCATION TO SSH PRIVATE KEY> -L <LOCAL PORT>:localhost:<REMOTE PORT ON WHICH MINIKUBE DASHBOARD IS RUNNING> user-name@IP
  $ sudo ssh -i ~/.ssh/id_rsa -L 8081:localhost:36525 shubham@40.77.75.58

  Now open your browser and open this url

  <http://127.0.0.1:8081/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/#/error?namespace=_all>

<br />

### TechWorld with Nana

- Kubernetes Crash Course for Absolute Beginners: <https://www.youtube.com/watch?v=s_o8dwzRlu4>
- Minikube & Kubectl explained | Setup for Beginners | ...: <https://www.youtube.com/watch?v=E2pP1MOfo3g>
- Kubectl Basic Commands - Create & Debug Pod ...: <https://www.youtube.com/watch?v=azuwXALfyRg>
- Kubernetes Ingress Tutorial for Beginners | ...: <https://www.youtube.com/watch?v=80Ew_fsV4rM>
- AWS EKS - Create Kubernetes cluster on Amazon EKS : <https://www.youtube.com/watch?v=p6xDCz00TxU>
- DevOps Roadmap 2022 - How to become a DevOps Engineer? : <https://www.youtube.com/watch?v=9pZ2xmsSDdo>
- What is Helm in Kubernetes? Helm and Helm Charts explained : <https://www.youtube.com/watch?v=-ykwb1d0DXU>
- Kubernetes Tutorial for Beginners [FULL COURSE in 4 Hours]: <https://www.youtube.com/watch?v=X48VuDVv0do>
- Kubernetes Volumes explained | Persistent Volume, ...: <https://www.youtube.com/watch?v=0swOh5C3OVM>

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

---

# Final Steps

1. AWS EKS - Create Kubernetes cluster on Amazon EKS : <https://www.youtube.com/watch?v=p6xDCz00TxU>
2. Install Jenkins with Helm v3 on Kubernetes

   a. <https://www.jenkins.io/doc/book/installing/kubernetes>
   b. <https://cloud.google.com/architecture/jenkins-on-kubernetes-engine>
   c. <https://www.youtube.com/watch?v=-ykwb1d0DXU> & <https://www.youtube.com/watch?v=JGtJj_nAA2s>

3. Set Up Persistent Volume for Kubernetes: <https://www.youtube.com/watch?v=0swOh5C3OVM>
4. Connecting Jenkins to Minikube Kubernetes Cluster: <https://www.youtube.com/watch?v=fodA9rM5xoo>
5. Allow Minikube Tunnel To Services/Set up Ingress/Expose All Ports: <https://www.youtube.com/watch?v=80Ew_fsV4rM>
6. Add & Test Tools (Docker, Docker-Compose & Others): <https://www.youtube.com/watch?v=ZPD_PzGOvFM>
7. Use Kubernetes Pods As Jenkins Agents: <https://www.youtube.com/watch?v=ZXaorni-icg>
8. Connect to Jenkins dashboard & Create a Pipeline

---

eksctl create cluster \
--name ccms-project2-cluster \
--version 1.22 \
--region us-west-1 \
--nodegroup-name linux-nodes \
--node-type t2.micro \
--nodes 2

kubectl create namespace jenkins

<!--
kubectl create -f mongo-config.yaml -f mongo-secret.yaml -f mongo.yaml
kubectl create -f webapp.yaml or kubectl create -f finance.yaml
kubectl get deployments
-->

kubectl get node
kubectl get namespaces
kubectl get pods -w

brew install helm
helm repo add jenkins <https://charts.jenkins.io> && helm repo update && helm search repo jenkins

    ```zsh
    helm upgrade --install myjenkins jenkins/jenkins
    &
    helm upgrade --install -f values.yaml myjenkins jenkins/jenkins
    ```

    or

    ```zsh
    cat | curl https://raw.githubusercontent.com/installing-jenkins-on-kubernetes/jenkins-volume.yaml > jenkins-volume.yaml
    cat | curl https://raw.githubusercontent.com/jenkins-infra/jenkins.io/master/content/doc/tutorials/kubernetes/installing-jenkins-on-kubernetes/jenkins-sa.yaml > jenkins-sa.yaml
    cat | curl https://raw.githubusercontent.com/jenkinsci/helm-charts/main/charts/jenkins/values.yaml > jenkins-values.yaml

    kubectl apply -f jenkins-volume.yaml
    kubectl apply -f jenkins-sa.yaml

    https://aws.amazon.com/blogs/storage/deploying-jenkins-on-amazon-eks-with-amazon-efs/
    Make these modifications to jenkins-values.yaml

                                minikube           EKS
    Line 111    serviceType:    NodePort           LoadBalancer
    Line 709    storageClass:   jenkins-pv
    Line 745    create: false
    Line 747    name: jenkins

    helm install jenkins -n jenkins -f jenkins-values.yaml jenkinsci/jenkins
    ```

Then Run these to get admin password and tunnel access

    ```zsh
    kubectl exec --namespace default -it svc/myjenkins -c jenkins -- /bin/cat /run/secrets/additional/chart-admin-password && echo

    echo http://127.0.0.1:8080
    kubectl --namespace default port-forward svc/myjenkins 8080:8080

    export SERVICE_IP=$(kubectl get svc --namespace default myjenkins --template \
    "{{ range (index .status.loadBalancer.ingress 0) }}{{ . }}{{ end }}")
    echo http://$SERVICE_IP/login

    <https://octopus.com/blog/jenkins-helm-install-guide>
    <https://www.bogotobogo.com/DevOps/Docker/Docker-Kubernetes-Jenkins-Helm.php>
    <https://ncarb.github.io/eks-workshop/intermediate/210_jenkins/deploy/>
    <https://www.eksworkshop.com/intermediate/210_jenkins/deploy/>
    ```

<https://www.linkedin.com/pulse/blue-green-deployment-kubernetes-itay-melamed>
<https://github.com/infinitelambda/istio-helm-deployment>
