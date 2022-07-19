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

                    echo "RESULTS1=${RESULTS1} and s RESULTS2=${RESULTS2}"

                    result = sh (script: "git log -1 | grep '\\[ci skip\\]'", returnStatus: true)
                    echo "${result}"
                    if (result == 1) {
                        echo "performing build...creating green"
                    } else {
                        echo "not running...staying with blue"
                    }

                    // if (RESULTS1 != 0) {
                    //     DEP_COLOR = "BLUE"
                    // }

                    // echo "DEP_COLOR=${DEP_COLOR}"
                    // if (RESULTS2 == 1) {
                    //     echo "test, build, archive"
                    //     // checkout scm
                    //     // sh "pip3 install -r ./src/requirements.txt"
                    //     // sh "python3 -m pytest ./src/app-test.py"
                    //     // sh "sudo docker build . -t chamoo334/p2official:${DEP_COLOR}"
                    //     // sh "sudo docker push chamoo334/p2official:${DEP_COLOR}"
                    // } else {
                    //     echo "skipping ci"
                    // }
                    
                }
                    
            }
        }
        stage("Deploy to EKS") {
            agent { label "linuxagent2" }
            steps {
                // checkout scm
                echo "updating deployments, services, and ingress"
                // sh "kubectl apply -f kubernetes/nginx-ingress/flask-deployment.yaml"
                // sh "kubectl apply -f kubernetes/nginx-ingress/flask-service.yaml"
                // sh "kubectl apply -f kubernetes/nginx-ingress/nginx-ingress.yaml"
            }
        }
    }
}
