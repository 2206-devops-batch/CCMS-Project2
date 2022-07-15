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
                // sh 'pip3 install -r requirements.txt'
                // sh 'python3 -m pytest app-test.py'
                // sh 'sudo docker build . -t chamoo334/p2official'
                // sh 'sudo docker push chamoo334/p2official'
                // stash name: "flask-yaml", includes: "flask-dep-serv.yaml"
                sh "echo 'testing and whatnot'"
            }
        }
        stage('Run maven') {
            agent { label 'linuxagent2' }
            steps {
                // checkout scm
                // sh 'pip3 install -r requirements.txt'
                // sh 'python3 -m pytest app-test.py'
                // sh 'sudo docker build . -t chamoo334/p2official'
                // sh 'sudo docker push chamoo334/p2official'
                // stash name: "flask-yaml", includes: "flask-dep-serv.yaml"
                sh "echo 'future kubernetes stage'"
            }
        }
    }
}