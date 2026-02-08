pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub-credentials')
        IMAGE_NAME = 'elhadjsow/backend-certificat'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Clonage du code source...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Installation des dépendances...'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Lancement des tests unitaires...'
                bat 'python manage.py test'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Construction de l’image Docker...'
                bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo '📤 Envoi de l’image vers Docker Hub...'
                powershell '''
                echo $env:DOCKER_HUB_CREDENTIALS_PSW | docker login -u $env:DOCKER_HUB_CREDENTIALS_USR --password-stdin
                docker push $env:IMAGE_NAME:$env:IMAGE_TAG
                docker logout
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo '🚀 Déploiement avec Docker Compose...'
                powershell '''
                docker pull $env:IMAGE_NAME:$env:IMAGE_TAG
                docker-compose down
                docker-compose up -d
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline terminé ✅'
        }
        failure {
            echo '❌ Le pipeline a échoué'
        }
    }
}
