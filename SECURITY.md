# Security Policy

This is a portfolio project, but it follows practical DevOps security hygiene.

## Security practices included

- No cloud access keys, passwords, `.env`, `.pem`, or Terraform state files are committed.
- Cloud authentication examples use OIDC-style federation where possible.
- Container build examples include Trivy scanning and SBOM generation notes.
- Infrastructure examples include least-privilege IAM/RBAC guidance.
- Sensitive runtime configuration is expected to come from platform secrets or environment variables.

## Reporting issues

If you find a security issue in this demo project, please open a GitHub issue with non-sensitive details.
