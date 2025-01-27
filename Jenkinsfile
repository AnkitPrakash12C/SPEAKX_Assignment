pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'app'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning the repository...'
                git branch: 'main', url: 'https://github.com/AnkitPrakash12C/SPEAKX_Assignment'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t app .'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo 'Pushing Docker image to DockerHub...'
                withDockerRegistry([credentialsId: 'SPEAKX', url: 'https://index.docker.io/v1/']) {
                    sh 'docker push app'
                }
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Deploying the application...'
                sh 'docker run -d -p 8000:8000 app'
            }
        }
    }
}
