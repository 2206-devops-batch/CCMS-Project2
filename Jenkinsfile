pipeline {
    options { skipDefaultCheckout() }
    agent none

    stages {
        stage("Verify Tools") {
            agent { label "linux-agent1" }
            options { timeout(time: 1, unit "MINUTES") }
            steps {
                sh '''
                docker version
                docker info
                docker compose version
                curl --version
                jq --version
                '''
            }
        }


        stage('Local Pytest') {
            agent { label "linux-agent1" }
            options { timeout(time: 2, unit "MINUTES") }
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'python3 -m pytest app-test.py'
            }
        }
        // stage('Test, Build, & Archive') {
        //     agent { label 'linux-agent1' }
        //     steps {
        //         checkout scm
        //         sh 'pip3 install -r requirements.txt'
        //         sh 'python3 -m pytest app-test.py'
        //         sh 'sudo docker build . -t chamoo334/p2official'
        //         sh 'sudo docker push chamoo334/p2official'
        //     }
        // }
        stage('Build') {
            agent { label "linux-agent1" }
            options { timeout(time: 2, unit "MINUTES") }
            steps {
                echo 'Build Docker Image & Container'
                sh 'docker build -t ccms-project2-image .'
                sh 'docker run -d -p 5000:5000 -rm --name ccms-project2-container ccms-project2-image'
                sh 'docker stop'

                sh 'sleep 10s'

                echo 'Build Docker Hub Image & Container'
                // sh 'docker pull chamoo334/p2official:latest'
                sh 'docker build -t ccms-project2-image chamoo334/p2official'
                sh 'docker run -d -p 5000:5000 -rm --name ccms-project2-container ccms-project2-image'
                sh 'docker stop'
            }
        }


        stage('Smoke Test') {
            options { timeout(time: 2, unit "MINUTES") }
            steps {
                input(message: "Run Live Tests?", ok; "Yes")
            }
        }



        stage('Prune Docker data') {
            agent { label "linux-agent2" }
            options { timeout(time: 1, unit "MINUTES") }
            steps {
                sh 'docker system prune -a --volumes -f'
            }
        }


        stage('Deploy - Start container') {
            agent { label "docker" }
            options { timeout(time: 2, unit "MINUTES") }
            steps {
                sh 'docker compose up -d --no-color --wait'
                sh 'sleep 2s'
                sh 'docker compose ps'
            }
        }
        stage('Run tests against the container') {
            agent { label "docker" }
            options { timeout(time: 2, unit "MINUTES") }
            steps {
                sh 'curl http://localhost:3000/param?query=demo | jq'
            }
        }


        stage('Accept Deployments') {
            options { timeout(time: 2, unit "MINUTES") }
            steps {
                input(message: "Approve Deploy?", ok; "Yes")
            }
        }

        // stage('Run') {
        //     agent { label 'linux-agent2' }
        //     steps {
        //         // sh 'sudo docker system prune -af'
        //         sh 'sudo docker rm -f p2_app'
        //         sh 'sudo docker pull chamoo334/p2official:latest'
        //         sh 'sudo docker run -p 5000:5000 -d --name p2_app chamoo334/p2official'
        //     }
        // }

        stage('Deploy To Staging') {
            options { timeout(time: 2, unit "MINUTES") }
            steps {
                echo 'Used To Configure Both Blue & Green Deployments'
                // sh ''
                sh 'minikube start' // Change to EKS
                sh 'kubectl network  PROD'
                sh 'kubectl apply -f flask-app-deployment.yml'  // PROD Deployment
                sh 'kubectl apply -f flask-app-service.yml'
                // sh 'docker push chamoo334/p2official:Prod'
            }
        }
        stage('Deploy To Blue Production') {
            options { timeout(time: 2, unit "MINUTES") }
            steps {
                echo 'Only Allow Deployments Tagged As A Blue-Feature'
                // sh ''
                sh 'minikube start' // Change to EKS
                sh 'kubectl network  BLUE'
                sh 'kubectl apply -f flask-app-deployment.yml'  // BLUE Deployment
                sh 'kubectl apply -f flask-app-service.yml'
                // sh 'docker push chamoo334/p2official:Blue'
            }
        }
        stage('Deploy To Green Production') {
            options { timeout(time: 2, unit "MINUTES") }
            steps {
                echo 'Only Allow Deployments Tagged As A Green-Feature'
                // sh ''
                sh 'minikube start' // Change to EKS
                sh 'kubectl network  GREEN'
                sh 'kubectl apply -f flask-app-deployment.yml'  // GREEN Deployment
                sh 'kubectl apply -f flask-app-service.yml'
                // sh 'docker push chamoo334/p2official:Green'
            }
        }

    }
    post {
        always {
            sh 'docker compose down --remove-orphans -v'
            sh 'docker compose ps'
        }
    }
}