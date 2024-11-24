pipeline {
    agent any

    environment {
        UV = 'C:\\Users\\ewide\\.local\\bin\\uv.exe'
    }

    options {
        timeout(time: 1, unit: 'MINUTES')
    }

    stages {

        stage('Set up venv') {
            steps {
                bat "${UV} venv --python 3.12.7"
                bat "call .venv/Scripts/activate.bat"
            }
        }

        stage('Run python script') {
            steps {
                bat "python main.py"
                archiveArtifacts artifacts: "workspace.txt"
            }
        }

        stage('Clean up venv') {
            steps {
                bat "call .venv/Scripts/deactivate.bat"
            }
        }

    }
}