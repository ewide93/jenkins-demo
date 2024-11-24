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

        stage('Python script returning -1') {
            steps {
                RV = bat 'python will_fail.py'
                echo "Return value: ${RV}"
            }
        }

    }

    post {

        always {
            bat "call ${DEACTIVATE_VENV}"
        }

        success {
            echo "Pipeline execution was successful."
        }

        unsuccessful {
            echo "Pipeline executeion was unsuccessful."
        }
    }
}