from agent_app.agents.base_agent import BaseAgent
from agent_app.agents.meal_agent import MealAgent
from agent_app.agents.shopping_agent import ShoppingAgent
from agent_app.agents.travel_agent import TravelAgent
import json

class OrchestratorAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.meal_agent = MealAgent()
        self.shopping_agent = ShoppingAgent()
        self.travel_agent = TravelAgent()
        self.system_instruction = """
        You are the Orchestrator Agent.
        Your job is to analyze the user's request and decide which sub-agent to call.
        Available Agents:
        - MealAgent: For meal planning, recipes, grocery lists.
        - ShoppingAgent: For general shopping needs, recurring items.
        - TravelAgent: For trip planning, flights, hotels.

        Output a JSON object with:
        - "agent": "MealAgent" | "ShoppingAgent" | "TravelAgent" | "None"
        - "reasoning": Why you chose this agent.
        - "refined_prompt": The specific prompt to send to the sub-agent.
        
        If the user request is general chat, set "agent" to "None" and answer directly.
        """

    async def process_request(self, user_input: str) -> str:
        # 1. Decide which agent to call
        decision_prompt = f"""
        {self.system_instruction}
        User Input: {user_input}
        """
        response_text = await self.send_message(decision_prompt)
        
        # Clean up code blocks if present
        cleaned_response = response_text.replace("```json", "").replace("```", "").strip()
        
        try:
            decision = json.loads(cleaned_response)
            agent_name = decision.get("agent")
            refined_prompt = decision.get("refined_prompt", user_input)
            
            if agent_name == "MealAgent":
                return await self.meal_agent.plan_meals(refined_prompt, budget=0) # Budget extraction could be improved
            elif agent_name == "ShoppingAgent":
                return await self.shopping_agent.check_needs(refined_prompt)
            elif agent_name == "TravelAgent":
                return await self.travel_agent.plan_trip(destination="Unknown", dates="Unknown", budget=0) # Param extraction could be improved
            else:
                # Fallback or direct answer
                return f"Orchestrator: {response_text}"
                
        except json.JSONDecodeError:
            return f"Orchestrator (Direct): {response_text}"
