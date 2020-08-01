pipeline {
    agent any 
    parameters {
         text(defaultValue:"https://i.imgur.com/n7bk8jC.jpg\nhttps://memegenerator.net/img/instances/67301987/work-work.jpg", description: "New line separated list of images", name: 'imgList')
    }
    stages {
        stage('prepare') {
            steps {
               cleanWs()
               checkout scm 
               sh 'mkdir ${WORKSPACE}/images'
               sh 'mkdir ${WORKSPACE}/flipped'
            }
        }
        stage('pull') { 
            steps {
               sh "${WORKSPACE}/pull.sh '${params.imgList}'"
            }
        }
        stage('flip') { 
            steps {
                sh '${WORKSPACE}/flip.sh'
            }
        }
        stage('push') { 
            steps {
                withAWS(credentials:'hivemapper-profile') {
                    s3Upload(bucket:"hivemapper-tmp", path:"operations-quiz-34.220.210.119/", includePathPattern:"flipped/*"
                }
            }
        }
    }
}
