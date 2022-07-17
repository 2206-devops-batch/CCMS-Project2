pipeline {
    agent none
    environment {
       DEP_COLOR = 'BLUE'
    }
    options {
        skipDefaultCheckout()      // Don't checkout automatically
    }
    stages {
        stage('Test, Build, & Archive') {
            agent { label 'linuxagent1' }
            steps {
                checkout scm
                
                script {
                    RESULTS = sh (script: "git log -1 | grep '\\[GREEN\\]'", returnStatus: true)

                    if (RESULTS == 0) {
                        DEP_COLOR = "GREEN"
                    }
                }

                echo 'Configure '

                // dir("src") {
                //     sh 'pip3 install -r requirements.txt'
                //     sh 'python3 -m pytest app-test.py'
                //     sh 'sudo docker build . -t chamoo334/p2official'
                //     sh 'sudo docker push chamoo334/p2official'
                // }
                // stash name: "flask-yaml", includes: "flask-dep-serv.yaml"
            }
        }
        stage('Deploy to EKS') {
            agent { label 'linuxagent2' }
            steps {
                echo "DEP_COLOR is '${DEP_COLOR}'"
                withKubeConfig([credentialsId: 'mykubeconfig', serverUrl: "${EKS}"]) {
                    sh "kubectl cluster-info"
                }
            }
        }
    }
}