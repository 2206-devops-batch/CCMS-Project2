pipeline {
    agent {label 'linuxagent1'}
    options {
        skipDefaultCheckout()      // Don't checkout automatically
    }
    stages {
        stage('Currnet Branch') {
            steps {
                sh 'hostname'
                echo 'Hello, Chris'
            }
        }
        stage('Build Docker Image & Container') {
            steps {
                sh 'docker build -t ccms-project2-image .'
                sh 'docker run -d -p 5000:5000 -rm --name ccms-project2-container ccms-project2-image'
                sh 'docker stop'
            }
        }
        stage('Build Docker Hub Image & Container') {
            steps {
                // sh 'docker pull chamoo334/p2official:latest'
                sh 'docker build -t ccms-project2-image chamoo334/p2official'
                sh 'docker run -d -p 5000:5000 -rm --name ccms-project2-container ccms-project2-image'
                sh 'docker stop'
            }
        }
        stage('Pytest Local Directory or Image') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'python3 -m pytest app-test.py'
            }
        }
        stage('Deploy To Staging') {
            steps {
                echo 'Used To Configure Both Blue & Green Deployments'
                // sh ''
                // sh ''
                // sh 'docker push chamoo334/p2official:Prod'
            }
        }
        stage('Deploy To Blue Production') {
            steps {
                echo 'Only Allow Deployments Tagged As A Blue-Feature'
                // sh ''
                // sh ''
                // sh 'docker push chamoo334/p2official:Blue'
            }
        }
        stage('Deploy To Green Production') {
            steps {
                echo 'Only Allow Deployments Tagged As A Green-Feature'
                // sh ''
                // sh ''
                // sh 'docker push chamoo334/p2official:Green'
            }
        }

        // stage('Test, Build, & Archive') {
        //     agent { label 'linuxagent2' }
        //     steps {
        //         checkout scm
        //         sh 'pip3 install -r requirements.txt'
        //         sh 'python3 -m pytest app-test.py'
        //         sh 'sudo docker build . -t chamoo334/p2official'
        //         sh 'sudo docker push chamoo334/p2official'
        //     }
        // }

        // stage('Run') {
        //     agent { label 'linuxdeploy' }
        //     steps {
        //         // sh 'sudo docker system prune -af'
        //         sh 'sudo docker rm -f p2_app'
        //         sh 'sudo docker pull chamoo334/p2official:latest'
        //         sh 'sudo docker run -p 5000:5000 -d --name p2_app chamoo334/p2official'
        //     }
        // }
    }
}