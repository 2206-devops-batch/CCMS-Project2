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

                    if (RESULTS1 == 0) {
                        DEP_COLOR = "BLUE"
                    }
                    
                    if (RESULTS2 == 1) {
                        echo 'ci: [ci skip not found]'
                        checkout scm
                        sh "pip3 install -r ./src/requirements.txt"
                        sh "python3 -m pytest ./src/app-test.py"
                        sh "sudo docker build . -t chamoo334/p2official:${DEP_COLOR}"
                        sh "sudo docker push chamoo334/p2official:${DEP_COLOR}"
                    }
                    
                }
                    
            }
        }
        stage("Deploy to EKS") {
            agent { label "linuxagent2" }
            steps {
                echo "DEP_COLOR=${DEP_COLOR}"
                // checkout scm
                // sh "kubectl apply -f kubernetes/flask-deployment.yaml"
                // sh "kubectl apply -f kubernetes/flask-service.yaml"
                // sh "kubectl apply -f kubernetes/nginx-ingress.yaml"
            }
        }
    }
}
