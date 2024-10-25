pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/jonfodi/FlaskAutomations.git', branch: 'main'
            }
        }
        stage('Deploy to Flask EC2 Instance') {
            steps {
                sshagent(['90df5cd1-345f-4d1b-b737-ee9d98a2a63d']) {
                    sh '''
                        ssh ec2-user@18.191.170.49 '
                        cd /home/ec2-user/FlaskAutomationss &&
                        git pull origin main &&
                        source /path/to/venv/bin/activate &&
                        nohup python3 app.py &'
                    '''
                }
            }
        }
    }
}



