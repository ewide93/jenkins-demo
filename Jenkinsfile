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
                bat 'python will_fail.py || true'
                echo "Return value: %ERRORLEVEL%"
            }

            post {
                success {
                    echo "All's good"
                }

                failure {
                    echo "Something is shit"
                }
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

        failure {
            echo "Pipeline executeion was unsuccessful."
        }
    }
}