pipeline {
    agent any

    environment {
        DOCKER_HUB = credentials('dockerhub-credentials')
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
                // Note: On installe ici pour flake8 ou l'IDE, mais les tests tourneront dans Docker
                sh """
                python3 -m venv venv 
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Nettoyage et lancement des tests dans Docker...'
                sh """
                # 1. Arrêt complet pour libérer le port 8000 et 5432
                docker compose down --remove-orphans
                
                # 2. Lancement des services en arrière-plan
                docker compose up -d --build
                
                # 3. Attendre que la DB soit prête (Healthcheck)
                echo "Waiting for database..."
                sleep 15
                
                # 4. Exécuter les commandes DANS le conteneur (Réseau interne 'db' OK)
                docker compose exec -T backend python manage.py migrate
                docker compose exec -T backend python manage.py test
                
                # 5. Nettoyage après tests
                docker compose down
                """
            }
        }

        stage('Build & Push Docker Hub') {
            steps {
                echo '🐳 Push vers Docker Hub...'
                // Utilisation de sh au lieu de powershell
                sh """
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                echo "${DOCKER_HUB_PSW}" | docker login -u "${DOCKER_HUB_USR}" --password-stdin
                docker push ${IMAGE_NAME}:${IMAGE_TAG}
                docker logout
                """
            }
        }
    }

    post {
        always {
            sh 'docker compose down'
            echo 'Pipeline terminé ✅'
        }
        failure {
            echo '❌ Le pipeline a échoué'
        }
    }
}
