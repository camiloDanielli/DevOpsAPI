pipeline {
    agent default

    stages {
        stage('Checkout') {
            steps {
                // Clona la rama del repositorio que disparó el build
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                // Instala dependencias si tenés un requirements.txt
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && if [ -f requirements.txt ]; then pip install -r requirements.txt; fi'
            }
        }

        stage('Run main.py') {
            steps {
                // Ejecuta tu main.py con Python3
                sh '. venv/bin/activate && python3 main.py'
            }
        }
    }
}
