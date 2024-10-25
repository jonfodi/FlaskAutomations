pipeline {
    agent any
    environment {
        FLASK_EC2 = 'ec2-user@18.191.170.49' // Update with your Flask EC2 IP if necessary
        SSH_CREDENTIALS_ID = 'pem_key' // Use the pem_key credential
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/jonfodi/FlaskAutomations.git', branch: 'main'
            }
        }
        stage('Deploy to Flask EC2 Instance') {
            steps {
                sshagent(credentials: [SSH_CREDENTIALS_ID]) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no $FLASK_EC2 '
                        cd /home/ec2-user/FlaskAutomations &&
                        git pull origin main &&
                        
                        nohup python3 app.py &'
                    '''
                }
            }
        }
    }
}
