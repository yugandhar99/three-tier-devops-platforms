# Known Issues

- Cloud deployment requires AWS account setup, EKS cluster access, ECR registry configuration, and ArgoCD installation.
- Advanced workflows are disabled by default to avoid failing GitHub Actions checks before credentials are configured.
- Terraform under `infra/` is a clean portfolio-safe skeleton and can be expanded into a full EKS platform later.
