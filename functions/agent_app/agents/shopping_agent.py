from agent_app.agents.base_agent import BaseAgent
# In a real scenario, this agent might have tools to check inventory or search for deals.

class ShoppingAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.system_instruction = """
        You are a Smart Shopping Agent.
        Your goal is to track recurring needs and suggest the best time to buy.
        """

    async def check_needs(self, inventory_context: str) -> str:
        prompt = f"""
        {self.system_instruction}
        Current Inventory Context: {inventory_context}
        Identify items running low and suggest what to buy this week.
        """
        return await self.send_message(prompt)
