pipeline {
    agent none

    options {
        skipDefaultCheckout()      // Don't checkout automatically
    }
    stages {
        stage("Test, Build, & Archive") {
            agent { label "linuxagent1" }
            steps {
                
                script {
                    RESULTS2 = sh (script: "git log -1 | grep '\\[CI SKIP\\]'", returnStatus: true)
                    RESULTS3 = sh (script: "git log -1 | grep '\\[PROD\\]'", returnStatus: true)
                    VERSION = "GREEN"
                    
                    if (RESULTS3 != 0) {
                        VERSION = "BLUE"
                    }

                    if (RESULTS2 != 0) {
                        echo "test, build, archive ${VERSION}"
                        // checkout scm
                        // sh "pip3 install -r ./src/requirements.txt"
                        // sh "python3 -m pytest ./src/app-test.py"
                        // sh "sudo docker build . -t chamoo334/p2official:${VERSION}"
                        // sh "sudo docker push chamoo334/p2official:${VERSION}"
                    } else {
                        echo "skipping ci"
                    }
                    
                }
                    
            }
        }
        stage("Deploy to EKS") {
            agent { label "linuxagent2" }
            steps {
                checkout scm
                echo "updating deployments, services, and ingress"
                // sh "kubectl apply -f kubernetes/nginx-ingress/flask-deployment.yaml"
                // sh "kubectl apply -f kubernetes/nginx-ingress/flask-service.yaml"
                // sh "kubectl apply -f kubernetes/nginx-ingress/nginx-ingress.yaml"
            }
        }
    }
}
