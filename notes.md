```zsh
#!/bin/bash
sudo yum update –y
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
sudo yum upgrade
sudo amazon-linux-extras install docker java-openjdk11 -y

sudo yum install jq jenkins -y
sudo systemctl enable jenkins
sudo systemctl start jenkins

sudo systemctl enable docker
sudo systemctl start docker

sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

curl -o kubectl https://s3.us-west-2.amazonaws.com/amazon-eks/1.22.6/2022-03-09/bin/linux/amd64/kubectl
curl -o kubectl.sha256 https://s3.us-west-2.amazonaws.com/amazon-eks/1.22.6/2022-03-09/bin/linux/amd64/kubectl.sha256
openssl sha1 -sha256 kubectl
chmod +x ./kubectl
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin
echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc

curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin

python3 -m pip install --upgrade pip
pip install -U pytest

# sudo systemctl status jenkins
# sudo systemctl status docker
# sudo systemctl status docker-compose
# kubectl version --short --client
# eksctl version
# pytest --version
```

```zsh
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

```zsh
eksctl create cluster \
--name main-cluster \
--version 1.22 \
--region us-west-1 \
--nodegroup-name master-node \
--node-type t2.micro \
--nodes 1
```

Then Login & Install Suggested Plugins
Then Go To Manage Plugins > Add Discord-Notifier & Kubernetes & Docker Pipeline
Then Go To Nodes Main > 0 Excuters & DO_NOT_USE Label
Cloud Kubernetes > EKS URL & Config
Then Create A Pipeline

<!-- -------------------------------------- -->
<!-- -------------------------------------- -->
<!-- --- APPLY SERVICE.YAML & BLUE.YAML --- -->
<!-- -------------------------------------- -->
<!-- -------------------------------------- -->

```zsh
kubectl apply -f service.yaml
kubectl apply -f blue.yaml
```

<!-- -------------------------------------- -->
<!-- -------------------------------------- -->
<!-- ---     MAKE CHANGES TO APP.PY     --- -->
<!-- -------------------------------------- -->
<!-- -------------------------------------- -->

Sawp Background Div `Blue` For `Green` in `src > Templates > index.html` Lines 10 & 11

```html:5
<!-- <div style="background: blue;"> -->
<div style="background: green;">
```

<!-- -------------------------------------- -->
<!-- -------------------------------------- -->
<!-- ---    CHANGES TO GREEN.YAML       --- -->
<!-- -------------------------------------- -->
<!-- -------------------------------------- -->
```yaml
spec:
  selector:
    matchLabels:
      app: finance-app
      version: 'v2.0.0'
  template:
    metadata:
      labels:
        app: finance-app
        version: 'v2.0.0'
    spec:
      containers:
        - name: finance-app
          env:
            - name: VERSION
              value: v2.0.0
```

```zsh
kubectl apply -f green.yaml
```
