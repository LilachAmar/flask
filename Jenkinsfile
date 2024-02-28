pipeline {
  agent any
  stages {
    stage('docker build') {
      steps {
        sh 'docker build -t flask-app .'
      }
    }

    stage('docker images') {
      steps {
        sh 'docker images'
      }
    }

    stage('create and run container') {
      steps {
        sh 'docker run -d -p 5000:5000 --name flask-container flask-app'
      }
    }

    stage('verify container') {
      steps {
        sh 'docker ps'
      }
    }

    stage('clean') {
      steps {
        deleteDir()
      }
    }

  }
}