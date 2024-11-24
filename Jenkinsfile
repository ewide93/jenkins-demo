pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\ewide\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
        PWD = 'C:\\Cmder\\vendor\\git-for-windows\\usr\\bin\\pwd.exe'
    }

    options {
        timeout(time: 1, unit: 'MINUTES')
    }

    stages {

        stage('Run python script') {
            steps {
                bat "${PWD}"
                bat "echo ${PYTHON}"
                bat "${PYTHON} main.py"
            }
        }

    }
}