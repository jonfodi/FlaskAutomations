pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/jonfodi/FlaskAutomations.git'
            }
        }

        stage('Deploy to Flask EC2 Instance') {
            steps {
                sshagent (credentials: ['your-ssh-credential-id']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ec2-user@18.191.170.49 << EOF
                    cd /home/ec2-user/FlaskAutomations
                    git pull origin main
                    sudo pkill -f app.py || true
                    nohup python3 app.py &
                    EOF
                    '''
                }
            }
        }
    }
}

