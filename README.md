#  Salesforce Integration - POPA Health AI

This module integrates **Salesforce** into the **POPA Health AI** platform to manage patient relationships, streamline appointment scheduling, and synchronize Electronic Health Records (EHR) data.

---

##  Features

-  **Bi-directional data sync** between POPA Health and Salesforce.
-  **Appointment management** with automatic updates in Salesforce CRM.
-  **Patient record synchronization** using FHIR standards for EHR data.
-  **Secure API connections** with OAuth 2.0 authentication.
-  **Health Cloud integration** for healthcare-specific data handling.

---

##  Project Structure

```
POPA-Health-AI/
├── salesforce-integration/
│   ├── src/
│   │   ├── auth.py              # Handles OAuth authentication with Salesforce
│   │   ├── sync_appointments.py # Synchronizes appointment data
│   │   ├── sync_patients.py     # Synchronizes patient data
│   │   └── utils.py             # Utility functions for data transformation
│   ├── requirements.txt         # Python dependencies
│   └── README.md                # This file
└── .env                         # Environment variables (Salesforce credentials)
```

---

##  Setup & Installation

### 1️ **Clone the Repository**
```bash
git clone https://github.com/Obionedonthoeme/POPA-Health-AI.git
cd POPA-Health-AI/salesforce-integration
```

### 2️ **Install Dependencies**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3️ **Configure Environment Variables**

Create a `.env` file in the `salesforce-integration/` directory with the following content:
```env
SALESFORCE_CLIENT_ID=your_client_id
SALESFORCE_CLIENT_SECRET=your_client_secret
SALESFORCE_USERNAME=your_salesforce_username
SALESFORCE_PASSWORD=your_salesforce_password
SALESFORCE_SECURITY_TOKEN=your_security_token
SALESFORCE_INSTANCE_URL=https://your-instance.salesforce.com
```
🔑 **Important:** Never commit the `.env` file. It's already in `.gitignore` for security.

---

## 4 Data Synchronization

###  **Sync Appointments**
```bash
python src/sync_appointments.py
```

###  **Sync Patient Records**
```bash
python src/sync_patients.py
```

---

##  Authentication

OAuth 2.0 is used to securely authenticate with Salesforce:

- The `auth.py` module handles token retrieval and refresh.  
- Tokens are automatically cached for efficiency and reduced API calls.

---

##  Security & Compliance

-  **OAuth 2.0** ensures secure API communications.  
-  **HIPAA compliance:** All patient data is handled securely and in compliance with regulations.  
-  **Environment variables** prevent sensitive data exposure.

---

##  Testing
To run unit tests:
```bash
pytest tests/
```
 Tests cover authentication, data synchronization, and error handling.

---

##  Troubleshooting

-  **Invalid OAuth token:**  
  Run the following to refresh tokens:  
  ```bash
  python src/auth.py
  ```

- ⚠️ **Connection errors:**  
  - Verify `SALESFORCE_INSTANCE_URL` and credentials in your `.env` file.  
  - Check Salesforce API availability.

-  **API limits reached:**  
  Salesforce enforces daily API call limits.  
  - Monitor usage in Salesforce settings.  
  - Optimize sync intervals to prevent overuse.

---

##  Roadmap

-  Initial appointment and patient data sync  
-  Real-time webhook support for instant updates  
-  Calendar event integration with Salesforce Lightning


# 📦 POPA Health AI - Kubernetes Deployment

POPA Health AI is now fully containerized and deployable using Kubernetes! The infrastructure leverages two deployment files located in the `k8s/` directory:

- **`backend-deployment.yaml`**: Deploys the FastAPI backend service.  
- **`frontend-deployment.yaml`**: Deploys the React-based frontend application.  

---

##  **Deployment Steps**

### 1️ Prerequisites
- Kubernetes cluster running on AWS EKS (or your preferred provider)  
- `kubectl` configured to access your cluster  
- Docker images built and pushed to DockerHub or AWS ECR  
- Salesforce credentials stored as Kubernetes secrets  

---

### 2️ Deploy the Backend

1. Apply the backend deployment:
   ```bash
   kubectl apply -f k8s/backend-deployment.yaml


---







