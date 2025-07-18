from fastapi import FastAPI, Depends, Query, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Ticket(BaseModel):
    id: int
    subject: str
    status: str
    customer: str

# Simulated ticket data
TICKETS = [
    Ticket(id=1, subject="Login Issue", status="open", customer="alice"),
    Ticket(id=2, subject="Payment Issue", status="closed", customer="bob"),
    Ticket(id=3, subject="Bug Report", status="open", customer="carol"),
    Ticket(id=4, subject="Feature Request", status="pending", customer="dave"),
    Ticket(id=5, subject="Refund", status="open", customer="eve"),
    Ticket(id=6, subject="Shipping", status="closed", customer="alice"),
    Ticket(id=7, subject="Account Deletion", status="open", customer="bob"),
    Ticket(id=8, subject="Password Reset", status="pending", customer="carol"),
    Ticket(id=9, subject="App Crash", status="closed", customer="dave"),
    Ticket(id=10, subject="Slow Response", status="open", customer="eve"),
]

# Simulated dummy role-permission function (for demonstration)
def get_current_user(token: str = Depends(oauth2_scheme)):
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    return {"username": "testuser", "role": "support_agent"}

@app.get("/tickets", response_model=List[Ticket])
def get_tickets(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    status: Optional[str] = Query(None),
    current_user: dict = Depends(get_current_user),
):
    # Filter by status if specified
    filtered = TICKETS
    if status:
        filtered = [t for t in filtered if t.status == status]
    # Apply pagination
    start = offset
    end = offset + limit
    paged = filtered[start:end]
    return paged
