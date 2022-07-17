pipeline {
    agent none
    options {
        skipDefaultCheckout()      // Don't checkout automatically
    }
    stages {
        stage('Test, Build, & Archive') {
            agent { label 'linuxagent1' }
            steps {
                checkout scm
                sh 'pip3 install -r src/requirements.txt'
                sh 'python3 -m pytest src/app-test.py'
                sh 'sudo docker build ./src -t chamoo334/p2official'
                sh 'sudo docker push chamoo334/p2official'
                echo 'testing and whatnot'
            }
        }
        stage('EKS Deployment') {
            agent { label 'linuxagent2' }
            steps {
                echo "Incorporate EKS: build number ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
    }
}