# Project: POPA Health AI

POPA Health AI is an AI-driven patient engagement platform that provides:
- Personalized health recommendations
- Appointment management
- Integration with wearable devices (Apple HealthKit, Fitbit, Garmin) and EHR systems (FHIR/HL7)
- Deployment on AWS with Kubernetes (EKS), Terraform for Infrastructure as Code (IaC), and a CI/CD pipeline via GitHub Actions

## 🚀 Features
- 🤖 **Conversational AI**: Utilizes Large Language Models (LLMs) for patient interactions.
- 📅 **Appointment Management**: Schedule, reschedule, and cancel appointments seamlessly.
- 🩺 **Health Data Integration**: Connects with wearables and EHR systems for comprehensive patient data.
- 🖥️ **Secure Backend**: FastAPI-powered with JWT-based authentication and HIPAA-compliant encryption.
- 📊 **Modern Frontend**: React application with animated dashboards and responsive design.
- ☁️ **Scalable Deployment**: AWS EKS orchestration with Terraform-managed infrastructure.
- 🔄 **Automated CI/CD**: GitHub Actions pipeline ensures consistent and reliable deployments.

---

## 📦 Project Structure

POPA-Health-AI/ ├── backend/ # FastAPI backend service │
├── app/ │ │ ├── main.py # FastAPI entry point │ 
│ ├── routes/ # API routes │ 
│ ├── models/ # Database models │ 
│ └── services/ # Business logic and integrations │ 
├── requirements.txt # Python dependencies │
└── Dockerfile # Backend Docker configuration
├── frontend/ # React frontend application │
├── src/ │ │ ├── components/ # Reusable UI components │
│ ├── pages/ # Page views │
│ └── services/ # API request handlers │
├── package.json # Node.js dependencies │
└── Dockerfile # Frontend Docker configuration 
├── infrastructure/ # Terraform for AWS infrastructure │
├── main.tf # Main Terraform configuration │ 
├── variables.tf # Terraform variables │ 
└── outputs.tf # Terraform outputs ├── .github/ │ 
└── workflows/ci-cd.yml # GitHub Actions CI/CD pipeline 
├── .gitignore # Git ignored files
└── README.md # Project documentation (this file)


---

## Setup & Installation

# Clone the Repository**

bash
git clone https://github.com/Obionedonthoeme/POPA-Health-AI.git
cd POPA-Health-AI



# Backend Setup

cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload


# Frontend Setup

cd ../frontend
npm install
npm run dev

# Deployment Infrastructure Provisioning (Terraform)

cd infrastructure
terraform init
terraform apply

# Containerization & Deployment
docker build -t backend:latest ./backend
docker build -t frontend:latest ./frontend

# Push Images to AWS ECR

aws ecr get-login-password | docker login --username AWS --password-stdin <account_id>.dkr.ecr.<region>.amazonaws.com

docker tag backend:latest <ecr_repo>/backend:latest
docker tag frontend:latest <ecr_repo>/frontend:latest

docker push <ecr_repo>/backend:latest
docker push <ecr_repo>/frontend:latest

# Deploy Containers to AWS EKS

kubectl apply -f k8s/backend-deployment.yml
kubectl apply -f k8s/frontend-deployment.yml


# CI/CD Pipeline
The project uses GitHub Actions for automated workflows:

 Builds Docker images
 Pushes to AWS ECR
 Deploys to AWS EKS
 Pipeline Configuration: .github/workflows/ci-cd.yml

 # Security & Compliance
 JWT-based authentication ensures secure API access.
 HIPAA-compliant encryption protects patient data.
 Regular security patches applied to infrastructure and code.
 Monitoring & Logging
 AWS CloudWatch integration for resource monitoring.
 Centralized logging ensures quick diagnostics.
 Alerts set for system health and uptime.








