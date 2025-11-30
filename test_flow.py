import asyncio
from agent_app.agents.orchestrator_agent import OrchestratorAgent

async def test_meal_plan_flow():
    print("--- Testing Meal Plan Flow ---")
    orchestrator = OrchestratorAgent()
    user_input = "Plan a vegetarian dinner for 2 people under $20"
    print(f"User Input: {user_input}")
    
    response = await orchestrator.process_request(user_input)
    print(f"Agent Response:\n{response}")
    print("------------------------------")

async def test_travel_flow():
    print("--- Testing Travel Flow ---")
    orchestrator = OrchestratorAgent()
    user_input = "I want to go to Paris next week"
    print(f"User Input: {user_input}")
    
    response = await orchestrator.process_request(user_input)
    print(f"Agent Response:\n{response}")
    print("------------------------------")

if __name__ == "__main__":
    asyncio.run(test_meal_plan_flow())
    asyncio.run(test_travel_flow())
