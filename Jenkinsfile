pipeline {
    agent any

    environment {
        UV = 'C:\\Users\\ewide\\.local\\bin\\uv.exe'
        ACTIVATE_VENV = '.venv/Scripts/activate.bat'
        DEACTIVATE_VENV = '.venv/Scripts/deactivate.bat'
    }

    options {
        timeout(time: 1, unit: 'MINUTES')
    }

    stages {

        stage('Set up venv') {
            steps {
                bat "${UV} venv --python 3.12.7"
                bat "call ${ACTIVATE_VENV}"
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
                bat "call ${DEACTIVATE_VENV}"
            }
        }

    }
}