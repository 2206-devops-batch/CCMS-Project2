pipeline {
    agent {label 'linuxagent1'}
    options {
        skipDefaultCheckout()      // Don't checkout automatically
    }
    stages {
        stage('Test, Build, & Archive') {
            agent { label 'linuxagent2' }
            steps {
                checkout scm
                sh 'pip3 install -r requirements.txt'
                sh 'python3 -m pytest app-test.py'
                sh 'sudo docker build . -t chamoo334/p2official'
                sh 'sudo docker push chamoo334/p2official'
            }
        }
        stage('Run') {
            agent { label 'linuxdeploy' }
            steps {
                // sh 'sudo docker system prune -af'
                sh 'sudo docker rm -f p2_app'
                sh 'sudo docker pull chamoo334/p2official:latest'
                sh 'sudo docker run -p 5000:5000 -d --name p2_app chamoo334/p2official'
            }
        }
    }
}