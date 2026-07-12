# Three-Tier DevOps Platfor m on AWS EKS

A production-style DevOps project for deploying a **React frontend**, **Spring Boot backend**, and **MySQL database** using **Docker**, **Helm**, **ArgoCD GitOps**, and **AWS EKS**.

This project keeps the original three-tier application recipe, then adds modern DevOps practices around containerization, Kubernetes deployment, GitOps, CI/CD validation, security scanning, SBOM notes, and operational documentation.

## Architecture

Generated project visual assets and any existing snapshots are included below to make the repository clear and professional for GitHub visitors.

![EKS Architecture](static/images/eks-architecture.png)

## CI/CD and GitOps Flow

![EKS CI/CD GitOps](static/images/eks-cicd-gitops.png)


## Portfolio visuals and career progression

These visuals were added so the project looks complete even when live cloud screenshots are not available. They explain the architecture, DevOps workflow, and how this project represents a step forward in cloud/platform engineering.

![Portfolio Overview](static/images/generated/eks-portfolio-overview.png)

![Career Progression](static/images/generated/eks-career-progression.png)

## What this project demonstrates

- Three-tier application architecture
- React frontend containerization
- Spring Boot backend containerization
- MySQL database support for local development
- Docker Compose for local testing
- Helm charts for Kubernetes deployments
- ArgoCD manifests for GitOps delivery
- AWS EKS-ready deployment structure
- ECR repository Terraform skeleton
- Jenkins pipeline example
- GitHub Actions portfolio validation
- Optional Trivy, CodeQL, and SBOM workflow design
- AI-ready release summary script

## Project structure

```text
.
├── src/                    # React, Spring Boot, and local Docker Compose files
├── charts/                 # Helm charts for frontend/backend/umbrella app
├── argocd/                 # ArgoCD project and application manifests
├── infra/                  # Terraform skeleton for AWS/ECR expansion
├── .github/                # Safe portfolio validation workflow
├── docs/                   # Architecture, runbook, workflow, GenAI, screenshot notes
├── scripts/                # AI-ready release summary helper
├── Jenkinsfile             # Jenkins CI/CD pipeline example
└── README.md
```

## Local development

```bash
cd src
docker compose up --build
```

Frontend: `http://localhost:4200`

## Kubernetes deployment flow

1. Build frontend and backend images.
2. Push images to Amazon ECR.
3. Update Helm chart image tags.
4. ArgoCD syncs the desired state to EKS.
5. Ingress routes traffic to frontend/backend services.

## Jenkins pipeline

A Jenkinsfile is included to show a real CI/CD flow:

```text
Checkout → Frontend Build → Backend Build → Docker Build → Trivy Scan → Push Image → Helm Validate
```

The push/deploy stages are intentionally documented but not fully auto-enabled so the repo stays safe until AWS credentials and ECR registry names are configured.

## GitHub Actions note

Only a safe **Portfolio Validation** workflow runs automatically. Advanced production-style workflows are kept in `.github/workflows-disabled/` and can be enabled later after configuring OIDC, AWS roles, registry names, and environment variables.

## Security practices

- No `.env`, `.pem`, Terraform state, or cloud secrets committed
- Runtime values use environment variables or Kubernetes secrets
- ECR image scanning enabled in Terraform skeleton
- Trivy/SBOM workflow design documented
- ArgoCD/Helm deployment model keeps Kubernetes config version-controlled

## Future improvements

- Add full VPC + EKS Terraform module
- Enable GitHub Actions OIDC deployment
- Add Prometheus and Grafana monitoring
- Add external-secrets integration
- Add canary or blue/green release strategy

## Known issues

See [KNOWN_ISSUES.md](KNOWN_ISSUES.md).


---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:2C5364,100:00C9FF&height=120&section=footer&text=Let's%20Connect&fontColor=ffffff&fontSize=32&fontAlignY=70" />
</p>

<h2 align="center">🤝 Connect With Me</h2>

<p align="center">
  <em>
    Thanks for visiting this project! I’m continuously building hands-on DevOps, Cloud, Automation, and AI-enabled engineering projects to improve real-world deployment, monitoring, and infrastructure skills.
  </em>
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=2500&pause=800&color=00C9FF&center=true&vCenter=true&width=650&lines=DevOps+%7C+Cloud+%7C+Automation;CI%2FCD+%7C+Docker+%7C+Kubernetes+%7C+Terraform;Building+real-world+projects+one+commit+at+a+time" alt="Typing SVG" />
</p>

<p align="center">
  <a href="https://github.com/yugandhar99" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="https://www.linkedin.com/in/yugandhar-devops" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://yugandhar-portfolio-psi.vercel.app/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Portfolio-View%20My%20Work-FF5722?style=flat&logo=vercel&logoColor=white" alt="Portfolio" />
  </a>
  <a href="mailto:yugandharethamukkala1999@gmail.com">
    <img src="https://img.shields.io/badge/Email-Contact%20Me-D14836?style=flat&logo=gmail&logoColor=white" alt="Email" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Focus-DevOps%20Engineering-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Cloud-AWS%20%7C%20Azure%20%7C%20GCP-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/IaC-Terraform-purple?style=flat-square" />
  <img src="https://img.shields.io/badge/Containers-Docker%20%7C%20Kubernetes-2496ED?style=flat-square" />
</p>

---

<p align="center">
  ⭐ If this project added value, feel free to star the repository and connect with me!
</p>

<p align="center">
  <strong>Built with ❤️ using modern DevOps practices</strong>
</p>

