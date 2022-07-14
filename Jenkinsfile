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
        stage('Deploy on EKS') {
            agent { label 'linuxdeploy' }
            steps {
                checkout scm
                sh 'pwd'
                sh 'ls'
                sshagent(['fcea763b-a663-437e-992b-c6733e3b0a56']) {
                    sh 'scp -o StrictHostKeyChecking=no /home/ubuntu/workspace/cm_kube_test_pipeline/flask-dep-serv.yaml ec2-user@ec2-3-145-60-217.us-east-2.compute.amazonaws.com:'
                }
            }
        }
    }
}