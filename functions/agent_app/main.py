from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent_app.agents.orchestrator_agent import OrchestratorAgent
from agent_app.memory.session_store import session_service
import uvicorn
import os

app = FastAPI(title="Lumos API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Orchestrator
orchestrator = OrchestratorAgent()

class ChatRequest(BaseModel):
    user_id: str
    message: str

class PriceWatchRequest(BaseModel):
    user_id: str
    destination: str
    target_price: float

@app.post("/chat")
async def chat(request: ChatRequest):
    # Get or create session
    # For simplicity, we just use user_id as session key in this prototype or create new
    session_id = request.user_id # In real app, manage session IDs properly
    
    # Log user message
    session_service.add_history(session_id, {"role": "user", "content": request.message})
    
    # Process with Orchestrator
    response = await orchestrator.process_request(request.message)
    
    # Log agent response
    session_service.add_history(session_id, {"role": "agent", "content": response})
    
    return {"response": response}

@app.post("/start-price-watch")
async def start_price_watch(request: PriceWatchRequest, background_tasks: BackgroundTasks):
    # Start a long-running operation
    op_id = session_service.start_operation("price_watch", request.dict())
    
    # Simulate the background task
    background_tasks.add_task(simulate_price_check, op_id, request)
    
    return {"operation_id": op_id, "status": "started"}

async def simulate_price_check(op_id: str, request: PriceWatchRequest):
    import asyncio
    # Simulate waiting and checking
    print(f"Starting price watch {op_id} for {request.destination}")
    await asyncio.sleep(5) # Simulate time passing
    # Update status
    session_service.update_operation(op_id, "completed", {"found_price": request.target_price - 10})
    print(f"Price watch {op_id} completed. Found cheaper price!")

if __name__ == "__main__":
    uvicorn.run("agent_app.main:app", host="0.0.0.0", port=8000, reload=True)
