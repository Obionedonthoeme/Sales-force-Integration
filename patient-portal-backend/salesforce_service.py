from simple_salesforce import Salesforce
import os

def connect_to_salesforce():
    sf = Salesforce(
        username=os.getenv("SALESFORCE_USERNAME"),
        password=os.getenv("SALESFORCE_PASSWORD"),
        security_token=os.getenv("SALESFORCE_SECURITY_TOKEN")
    )
    return sf
