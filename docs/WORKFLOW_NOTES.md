# Workflow Notes

This repository keeps only a safe **Portfolio Validation** workflow active by default.

Advanced workflows are stored under `.github/workflows-disabled/`. Move one workflow at a time into `.github/workflows/` only after configuring the required cloud credentials, OIDC role, registry names, and environment variables.

This avoids the common GitHub portfolio problem where advanced production workflows fail immediately after upload because secrets or cloud roles are not configured yet.
