from agent_app.agents.base_agent import BaseAgent
from agent_app.tools.mock_tools import FlightSearchTool, HotelSearchTool

class TravelAgent(BaseAgent):
    def __init__(self):
        super().__init__(tools=[FlightSearchTool().search_flights, HotelSearchTool().search_hotels])
        self.system_instruction = """
        You are a Travel Planner Agent.
        Your goal is to build trip itineraries including flights and hotels.
        You have access to FlightSearchTool and HotelSearchTool.
        """

    async def plan_trip(self, destination: str, dates: str, budget: float) -> str:
        prompt = f"""
        {self.system_instruction}
        Destination: {destination}
        Dates: {dates}
        Budget: {budget}
        Please find flights and hotels and build an itinerary.
        """
        return await self.send_message(prompt)
