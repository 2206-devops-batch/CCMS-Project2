pipeline {
    agent none
    options {
        skipDefaultCheckout()      // Don't checkout automatically
    }
    stages {
        stage('Test, Build, & Archive') {
            agent { label 'linuxagent1' }
            steps {
                // checkout scm
                // dir("src") {
                //     sh 'pip3 install -r requirements.txt'
                //     sh 'python3 -m pytest app-test.py'
                //     sh 'sudo docker build . -t chamoo334/p2official'
                //     sh 'sudo docker push chamoo334/p2official'
                // }
                // stash name: "flask-yaml", includes: "flask-dep-serv.yaml"
                echo 'testing and whatnot'
            }
        }
        stage('Deploy to EKS') {
            agent { label 'linuxagent2' }
            steps {
                result = sh (script: "git log -1 | grep '\\[blue\\]'", returnStatus: true) 
                if (result != 0) {
                    echo "performing build..."
                } else {
                    echo "not running..."
                }
            //     withKubeConfig([credentialsId: 'mykubeconfig', serverUrl: "${EKS}"]) {
            //         sh "kubectl cluster-info"
            //     }
            }
        }
    }
}