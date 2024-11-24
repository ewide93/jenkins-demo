pipeline {
    agent any
    options {
        timeout(time: 1, unit: 'MINUTES')
    }
    stages {
        stage('Example') {
            steps {
                sh "python main.py"
            }
        }
    }
}