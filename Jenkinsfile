pipeline {
    agent { label 'vinod' }
    environment{
        DOCKERHUB_CREDENTIALS = credentials('practice-webhook-id')
        IMAGE_NAME = 'kuldeepsharmaks1/practicewebhook'
        CONTAINER_NAME = 'practicewebhookcont'
        
    }
    stages{
        stage("Cloning"){
            steps{
                git "https://github.com/kuldeepsharma100/webhook-flask-app.git"
            }
        }
        stage("Building"){
            steps{
                sh 'docker build -t $IMAGE_NAME .'
            }
        }
        stage("Push to Docker Hub"){
            steps{
                sh '''echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                docker push $IMAGE_NAME
                '''
            }
        }
        
        stage("Deploy to ec2"){
            steps{
                sh '''
                docker stop $CONTAINER_NAME || true &&
                docker rm $CONTAINER_NAME || true &&
                docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME
                '''
            }
        }
    }
}
