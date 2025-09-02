pipeline {
    agent { label 'default' }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                '''
            }
        }

        stage('Run main.py') {
            steps {
                sh '''
                nohup python3 main.py > server.log 2>&1 &
                sleep 5  # espera que el server arranque
                curl --fail http://localhost:5000 || exit 1
                echo "Server is up!"
                '''
            }
        }
    }
}
