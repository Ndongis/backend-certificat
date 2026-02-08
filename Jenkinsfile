pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub-credentials')
        IMAGE_NAME = 'ndongis/backend-certificat'
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
                sh """ python3 -m venv venv 
                . venv/bin/activate
                 pip install --upgrade pip
                 pip install -r requirements.txt """
            }
        }

      stage('Run Tests') {
    steps {
        sh """
        echo '🧪 Lancement des tests unitaires...'
        export POSTGRES_HOST=localhost
        export POSTGRES_PORT=5433
        export POSTGRES_DB=certificatdb
        export POSTGRES_USER=postgres
        export POSTGRES_PASSWORD=n
        
        . venv/bin/activate
        python manage.py test
        """
    }
}

        stage('Build Docker Image') {
            steps {
                echo '🐳 Construction de l’image Docker...'
                sh 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
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
