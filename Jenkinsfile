pipeline {
    agent { label 'vinod' }

    environment {
        DOCKERHUB_CREDENTIALS = credentials('webhook-flask-app-id')
        IMAGE_NAME = 'kuldeepsharmaks1/flaskapp'
        CONTAINER_NAME = 'flaskappcont'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/kuldeepsharma100/webhook-flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh """
                    echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                    docker push $IMAGE_NAME
                """
            }
        }

        stage('Deploy to EC2') {
            steps {
                    sh '''
                        docker stop $CONTAINER_NAME || true &&
                        docker rm $CONTAINER_NAME || true &&

                        docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME'''
        
            }
        }
    }
}
