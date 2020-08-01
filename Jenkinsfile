pipeline {
    agent any 
    parameters {
         text(defaultValue:"https://i.imgur.com/n7bk8jC.jpg\nhttps://memegenerator.net/img/instances/67301987/work-work.jpg", description: "New line separated list of images", name: 'imgList')
    }
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
               sh '${WORKSPACE}/pull.sh'
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
