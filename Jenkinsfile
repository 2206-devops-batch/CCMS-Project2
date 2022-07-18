pipeline {
  environment {
    registry='chrisbarnes2000'
    repo='ccms-project2'
    DOCKERHUB_CREDENTIALS=credentials('DOCKER_AUTH_ID')
    DOCKERHUB_REPO='${registry}/${repo}'
    TAG="${BUILD_NUMBER}" // 'latest'
  } // environment

  agent any

  stages {
    stage('ENV CHECK'){
      steps{
        // Check For Required Tools
        sh '''
          docker version
          docker info
          docker-compose version
          curl --version
          jq --version
        '''

        // Login To Docker
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'

        sh 'docker system prune -af --volumes'

        // Check The ENV Is Clean
        sh 'docker-compose ps -a'
        sh 'docker ps -a'
      }
    }
    stage('Build'){
      steps {
        echo '\n\nBUILDING... \n'
        sh "docker build -t ${DOCKERHUB_REPO} ." //:${TAG}

        echo "\n\nStarting Web Server... \n"
        sh "docker run -d -p 5000:5000 --rm --name ${repo}-container ${DOCKERHUB_REPO}"

        echo "Please Visit --> $BASE_URL:5000"
      }
    }
    stage('Test'){
      steps {
        echo '\n\nTESTING... \n'
        echo '\n\n SKIPPING TESTING... \n'
        // sh "pytest app-test.py"
      }
    }
    stage('Push'){
      steps {
        echo '\n\nPUSHING... \n'
        sh "docker push ${DOCKERHUB_REPO}" //:${TAG}
      }
    }
    stage('Pull'){
      steps {
        echo '\n\nPULLING... \n'
        sh "docker pull ${DOCKERHUB_REPO}" //:${TAG}
      }
    }
    // stage("Run Smoke Tests Against The Container") {
    //   steps {
    //     sh 'docker kill $(docker ps -q)'

    //     echo '\n\nRE-BUILD LATEST FROM DOCKER HUB... \n'
    //     sh "docker build -t ${DOCKERHUB_REPO} ." //:${TAG}

    //     echo "\n\nStarting Web Server FOR SMOKE TESTS... \n"
    //     sh "docker run -d -p 5000:5000 --rm --name ${repo}-container ${DOCKERHUB_REPO}"

    //     echo "\nPlease Visit --> $BASE_URL:5000"
    //     sh "curl ${BASE_URL}:5000 | jq"
    //   }
    // }
    stage('Deploy'){
      steps {
        echo '\n\nDEPLOYING... \n'

      }
    }
  } // stages


  post {
    always {
      // Clean Everything UP -- Docker
      // sh 'docker-compose down --remove-orphans -v'
      // sh 'docker kill $(docker ps -q)'

      // Clean The Docker ENV
      // sh 'docker rm $(docker ps -a -q)'
      // sh 'docker rmi $(docker images -q)'
      // sh 'docker rmi $(path_current_build)'
      sh 'docker system prune -af && docker logout'

      // Send Status Report To Email & Discord
      mail to: "Chris.Barnes.2000@me.com",
           subject: "Job '${JOB_NAME}' (${BUILD_NUMBER}) Was A ${currentBuild.currentResult}",
           body: "Please go to ${BUILD_URL} and verify the build"

      discordSend webhookURL: "https://discord.com/api/webhooks/998320738769588224/4akFNyQItbFvUKmbGxJ-qMCyzMefF3QP4GbyNk73wry4_WfGPuDOWUlael_WN4_Yh677",
                  enableArtifactsList: false, scmWebUrl: "",
                  image: "", thumbnail: "",
                  title: JOB_NAME, link: BUILD_URL,
                  description: "Please Visit --> ${BASE_URL}:50000",
                  footer: "Jenkins Pipeline Build was a ${currentBuild.currentResult}",
                  result: currentBuild.currentResult
    } // always
  } // post
} // pipeline
