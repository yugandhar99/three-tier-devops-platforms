#!/usr/bin/env python3
import subprocess
from datetime import datetime

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return "Unavailable"

commits = run("git log -5 --pretty=format:'- %s'")
summary = f"""# AI-Ready Release Summary

Generated: {datetime.utcnow().isoformat()}Z

## Recent changes
{commits}

## Release risk summary
- Review infrastructure changes before applying.
- Confirm image tags and environment variables.
- Validate security scan results.
- Confirm health checks after deployment.

## Next recommended action
Run CI validation and review deployment notes before promoting to production.
"""
print(summary)
