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
        stage('EKS Initial Setup') {
            agent { label 'linuxagent2' }
            steps {
                echo "Incorporate EKS: build number ${env.BUILD_ID} on ${env.JENKINS_URL} using cluster server ${EKS}"
                // withKubeConfig([credentialsId: 'mykubeconfig', serverUrl: 'https://0A1A4A8601F380D4399A007D4FC2C7E1.gr7.us-east-2.eks.amazonaws.com']) {
                //     sh "kubectl cluster-info"
                // }
            }
        }
    }
}