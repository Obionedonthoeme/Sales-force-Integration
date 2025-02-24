from fastapi import APIRouter, HTTPException
from salesforce_integration import sf

router = APIRouter()

@router.post("/tickets/")
async def create_ticket(subject: str, description: str):
    try:
        case = sf.Case.create({
            'Subject': subject,
            'Description': description,
            'Priority': 'Medium',
            'Status': 'New'
        })
        return {"message": "Ticket created", "case_id": case['id']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
