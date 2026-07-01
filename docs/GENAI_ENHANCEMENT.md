# Optional GenAI Enhancement

A practical AI enhancement for this project is an AI-assisted release summary.

The script can summarize:

- Recent Git commits
- Changed application components
- CI/CD validation results
- Security scan notes
- Deployment risk summary

This can be connected later to Amazon Bedrock, Azure OpenAI, or OpenAI using a secure pipeline secret. The current version supports offline summary mode so the repo stays safe for GitHub.
