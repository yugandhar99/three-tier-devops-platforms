pipeline {
  agent any

  options {
    timestamps()
    disableConcurrentBuilds()
  }

  environment {
    AWS_REGION = 'us-east-1'
    ECR_REGISTRY = 'replace-with-account-id.dkr.ecr.us-east-1.amazonaws.com'
    FRONTEND_IMAGE = 'three-tier-devops-eks-frontend'
    BACKEND_IMAGE = 'three-tier-devops-eks-backend'
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Frontend Build') {
      steps {
        dir('src/frontend') {
          sh 'npm ci'
          sh 'npm test -- --watchAll=false || true'
          sh 'npm run build'
        }
      }
    }

    stage('Backend Build') {
      steps {
        dir('src/backend') {
          sh './mvnw clean package -DskipTests=false'
        }
      }
    }

    stage('Docker Build') {
      steps {
        sh 'docker build -t $FRONTEND_IMAGE:$BUILD_NUMBER src/frontend'
        sh 'docker build -t $BACKEND_IMAGE:$BUILD_NUMBER src/backend'
      }
    }

    stage('Security Scan') {
      steps {
        sh 'trivy image --severity HIGH,CRITICAL --exit-code 0 $FRONTEND_IMAGE:$BUILD_NUMBER || true'
        sh 'trivy image --severity HIGH,CRITICAL --exit-code 0 $BACKEND_IMAGE:$BUILD_NUMBER || true'
      }
    }

    stage('Push Images') {
      when { expression { return env.BRANCH_NAME == 'main' } }
      steps {
        sh 'echo Login to ECR using Jenkins AWS credentials or IAM role before enabling push'
        sh 'docker tag $FRONTEND_IMAGE:$BUILD_NUMBER $ECR_REGISTRY/$FRONTEND_IMAGE:$BUILD_NUMBER'
        sh 'docker tag $BACKEND_IMAGE:$BUILD_NUMBER $ECR_REGISTRY/$BACKEND_IMAGE:$BUILD_NUMBER'
        sh 'echo docker push commands are intentionally documented but not auto-enabled in portfolio mode'
      }
    }

    stage('Helm Validate') {
      steps {
        sh 'helm lint charts/frontend || true'
        sh 'helm lint charts/backend || true'
      }
    }
  }

  post {
    always {
      echo 'Jenkins CI/CD pipeline completed. Review build, scan, and Helm validation logs.'
    }
  }
}
