node {
    def app

    stage('Clone repository') {
      

        checkout scm
    }

    stage('Build image') {
  
       app = docker.build("sahilpahuja963/test")
    }

    stage('Test image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhublogin') {
            app.push("${env.BUILD_NUMBER}")
        }
    }
    
    stage('Deploy on K8s') {
        script {
            sh "sed -i 's+sahilpahuja963/test.*+sahilpahuja963/test:${env.BUILD_NUMBER}+g' deployment.yml"
            sh "cat deployment.yml"
            sh "kubectl apply -f deployment.yml"
        }
    }
}
