pipeline {
    agent {label ''}
    stages {
        stage('Test, Build, Archive') {
            agent { label '' }
            steps {
                sh 'pwd'
                sh 'ls'
                sh 'sudo yum –y install python3'
                sh 'sudo yum -y install docker'
                sh 'sudo yum –y install python3-pip'
                sh 'pip3 install -r requirements.txt'
                sh 'python3 -m pytest app-test.py'
                sh 'sudo docker login -u ${DOCK_USER} --password-stdin ${DOCK_PASSWORD}'
                sh 'sudo docker build /home/ec2-user/workspace/Monikai -t chamoo334/p2'
                sh 'sudo docker push chamoo334/p2'
            }
        }
        stage('Run') {
            agent {label ''}
            steps {
                sh 'sudo docker system prune -af'
                sh 'sudo docker pull chamoo334/p2:latest'
                sh 'sudo docker run -p 5000:5000 -d --name p2_app chamoo334/p2'
            }
        }
    }
}