pipeline {
    agent none
    environment {
       DEP_COLOR = "GREEN"
    }
    options {
        skipDefaultCheckout()      // Don't checkout automatically
    }
    stages {
        stage("Test, Build, & Archive") {
            agent { label "linuxagent1" }
            steps {
                
                script {
                    RESULTS1 = sh (script: "git log -1 | grep '\\[BLUE\\]'", returnStatus: true)
                    RESULTS2 = sh (script: "git log -1 | grep '\\[CI SKIP\\]'", returnStatus: true)

                    echo "RESULTS1=${RESULTS1} and RESULTS2=${RESULTS2}"

                    if (RESULTS1 == 1) {
                        DEP_COLOR = "BLUE"
                    }
                    
                    checkout scm
                    sh "pip3 install -r ./src/requirements.txt"
                    sh "python3 -m pytest ./src/app-test.py"
                    sh "sudo docker build . -t chamoo334/p2official:${DEP_COLOR}"
                    sh "sudo docker push chamoo334/p2official:${DEP_COLOR}"
                    
                }
                    
            }
        }
        stage("Deploy to EKS") {
            agent { label "linuxagent2" }
            steps {
                checkout scm

                script {
                    RESULTS3 = sh (script: "git log -1 | grep '\\[SWITCH VERSION\\]'", returnStatus: true)

                    if (RESULTS3 == 0) {
                        sh "kubectl apply -f kubernetes/nginx-ingress/flask-service.yaml"
                        echo "updating flask-app-stable service to switch to the new version"
                    } else {
                        echo "updating deployments, services, and ingress"
                        sh "kubectl apply -f kubernetes/nginx-ingress/flask-deployment.yaml"
                        sh "kubectl apply -f kubernetes/nginx-ingress/flask-service.yaml"
                        sh "kubectl apply -f kubernetes/nginx-ingress/nginx-ingress.yaml"
                    }

                }
            }
        }
    }
}
