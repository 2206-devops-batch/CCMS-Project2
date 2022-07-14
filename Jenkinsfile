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
            agent {
                kubernetes {
                yaml '''
                    apiVersion: v1
                    kind: Pod
                    spec:
                    containers:
                    - name: maven
                      image: maven:alpine
                      command:
                      - cat
                      tty: true
                '''
                }
            }
            steps {
                container('maven') {
                    sh 'mvn -version'
                }
            }
        }
    }
}