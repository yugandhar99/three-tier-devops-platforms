variable "aws_region" { 
  description = "AWS region for the EKS platform."
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name used for tagging resources."
  type        = string
  default     = "three-tier-devops-eks"
}

variable "environment" {
  description = "Deployment environment."
  type        = string
  default     = "dev"
}
