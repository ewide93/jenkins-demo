pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\ewide\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    }

    options {
        timeout(time: 1, unit: 'MINUTES')
    }

    stages {

        stage('Run python script') {
            steps {
                sh "${PYTHON} main.py"
            }
        }

    }
}