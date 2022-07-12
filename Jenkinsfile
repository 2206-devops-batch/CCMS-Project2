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
                // sh 'sudo docker login -u ${DOCKER_USER} --password-stdin ${DOCKER_PASSWORD}'
                // sh 'sudo docker build /home/ubuntu/workspace/Monikai -t chamoo334/p2'
                // sh 'sudo docker push chamoo334/p2'
            }
        }
        stage('Run') {
            agent { label 'linuxdeploy' }
            steps {
                sh 'dig TXT +short o-o.myaddr.l.google.com @ns1.google.com'
                sh 'pwd'
                    // sh 'sudo docker system prune -af'
                    // sh 'sudo docker pull chamoo334/p2:latest'
                    // sh 'sudo docker run -p 5000:5000 -d --name p2_app chamoo334/p2'
            }
        }
    }
}