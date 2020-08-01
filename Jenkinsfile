pipeline {
    agent any 
    stages {
        stage('prepare') {
            steps {
               checkout scm 
               sh 'mkdir ${WORKSPACE}/images'
               sh 'mkdir ${WORKSPACE}/flipped'
            }
        }
        stage('pull') { 
            steps {
               sh '${WORKSPACE}/
            }
        }
        stage('flip') { 
            steps {
                sh '${WORKSPACE}/flip.sh'
            }
        }
        stage('push') { 
            steps {
                sh 'echo hi'
            }
        }
    }
}
