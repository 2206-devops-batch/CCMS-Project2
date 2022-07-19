pipeline {
    agent none
    stages {
        stage("Test, Build, & Archive") {
            agent { label "linuxagent1" }
            steps {
                    sh "pip3 install -r ./src/requirements.txt"
                    sh "python3 -m pytest ./src/app-test.py"
                    sh "sudo docker build . -t chamoo334/p2official:GREEN"
                    sh "sudo docker push chamoo334/p2official:GREEN"
                
                }        
        }

        stage("Deploy to EKS") {
            agent { label "linuxagent2" }
            steps {

                sh "kubectl apply -f kubernetes/nginx-ingress/flask-deployment.yaml"
                sh "kubectl apply -f kubernetes/nginx-ingress/flask-service.yaml"
                sh "kubectl apply -f kubernetes/nginx-ingress/nginx-ingress.yaml"
            }
        }
    }
}