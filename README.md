# 🧩 Salesforce Integration - POPA Health AI

This module integrates **Salesforce** into the **POPA Health AI** platform to manage patient relationships, streamline appointment scheduling, and synchronize Electronic Health Records (EHR) data.

---

## 🚀 Features

- 🔄 **Bi-directional data sync** between POPA Health and Salesforce.
- 📝 **Appointment management** with automatic updates in Salesforce CRM.
- 📊 **Patient record synchronization** using FHIR standards for EHR data.
- 🔐 **Secure API connections** with OAuth 2.0 authentication.
- 🩺 **Health Cloud integration** for healthcare-specific data handling.

---

## 📦 Project Structure

POPA-Health-AI/ ├── salesforce-integration/ │ ├── src/ │ │ ├── auth.py # Handles OAuth authentication with Salesforce │ │ ├── sync_appointments.py # Synchronizes appointment data │ │ ├── sync_patients.py # Synchronizes patient data │ │ └── utils.py # Utility functions for data transformation │ ├── requirements.txt # Python dependencies │ └── README.md # This file └── .env # Environment variables (Salesforce credentials)


---

## ⚙️ Setup & Installation

### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/Obionedonthoeme/POPA-Health-AI.git
cd POPA-Health-AI/salesforce-integration

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```env
SALESFORCE_CLIENT_ID=your_client_id
SALESFORCE_CLIENT_SECRET=your_client_secret
SALESFORCE_USERNAME=your_salesforce_username
SALESFORCE_PASSWORD=your_salesforce_password
SALESFORCE_SECURITY_TOKEN=your_security_token
SALESFORCE_INSTANCE_URL=https://your-instance.salesforce.com


```bash
python src/sync_appointments.py


```bash
python src/sync_patient.py


  Authentication
OAuth 2.0 is used to securely authenticate with Salesforce:

The auth.py module handles token retrieval and refresh.
Tokens are automatically cached for efficiency.
Security & Compliance
 OAuth 2.0 ensures secure API communications.
 All patient data is handled in compliance with HIPAA standards.
 Environment variables are used to prevent sensitive data exposure.

```bash
pytest tests/


📝 Troubleshooting
Invalid OAuth token:
Run python src/auth.py to refresh tokens.

Connection errors:
Verify your SALESFORCE_INSTANCE_URL and credentials in .env.

API limits reached:
Salesforce has daily API call limits. Monitor usage in Salesforce settings.

# Roadmap
 Initial appointment and patient data sync
 Real-time webhook support for instant updates
 Calendar event integration with Salesforce Lightning







