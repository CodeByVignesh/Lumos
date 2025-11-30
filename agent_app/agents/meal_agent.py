from agent_app.agents.base_agent import BaseAgent
from agent_app.tools.mock_tools import GroceryStoreTool

class MealAgent(BaseAgent):
    def __init__(self):
        super().__init__(tools=[GroceryStoreTool().get_prices])
        self.system_instruction = """
        You are a Meal Planning Agent.
        Your goal is to plan meals based on user preferences and budget.
        You have access to a GroceryStoreTool to check prices.
        Always provide a shopping list with estimated costs.
        """
        # Note: In a real app, system instruction would be set on the model.
        # For this prototype, we'll prepend it to the first message or rely on context.

    async def plan_meals(self, preferences: str, budget: float) -> str:
        prompt = f"""
        {self.system_instruction}
        User Preferences: {preferences}
        Budget: {budget}
        Please generate a meal plan and a shopping list with prices.
        """
        return await self.send_message(prompt)
