pipeline {
    agent any  // cualquier nodo disponible para checkout

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run main.py') {
            agent {
                docker {
                    image 'python:3.11-slim' // contenedor con Python 3
                    args '-v $WORKSPACE:$WORKSPACE' // monta el workspace
                }
            }
            steps {
                sh '''
                pip install --upgrade pip
                if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                python main.py
                '''
            }
        }
    }
}
