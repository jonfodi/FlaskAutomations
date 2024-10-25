pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/jonfodi/FlaskAutomations.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('flask-app')
                }
            }
        }
        stage('Run Docker Image') {
            steps {
                script {
                    docker.image('flask-app').run('-p 5000:5000')
                }
            }
        }
    }
}
