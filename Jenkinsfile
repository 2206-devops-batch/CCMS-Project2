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
        stage('Deploy BLUE EKS') {
            agent { label 'linuxagent2' }
            when {
                changelog '.*^\\[BLUE\\] .+$'
            }
            steps {
                echo 'Found BLUE'
            //     withKubeConfig([credentialsId: 'mykubeconfig', serverUrl: "${EKS}"]) {
            //         sh "kubectl cluster-info"
            //     }
            }
        }
        stage('Deploy GREEN EKS') {
            agent { label 'linuxagent2' }
            when {
                changelog '.*^\\[GREEN\\] .+$'
            }
            steps {
                echo 'Found BLUE'
            //     withKubeConfig([credentialsId: 'mykubeconfig', serverUrl: "${EKS}"]) {
            //         sh "kubectl cluster-info"
            //     }
            }
        }
    }
}