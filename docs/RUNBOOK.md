# Operational Runbook

## Local validation

```bash
docker compose -f src/docker-compose.yml up --build
```

## Before cloud deployment

1. Confirm cloud credentials are configured.
2. Confirm registry names and image tags.
3. Review Terraform plan output.
4. Confirm environment variables and secrets are not committed.
5. Deploy using the documented AWS EKS + ArgoCD GitOps flow.

## Rollback approach

- Revert to a previous image tag.
- Re-sync GitOps application or redeploy the previous release.
- Check application logs and health endpoints.
- Validate database connectivity.
