import google.generativeai as genai
from agent_app.core.config import config
from agent_app.core.observability import trace_agent
from typing import List, Any

if config.GOOGLE_API_KEY:
    genai.configure(api_key=config.GOOGLE_API_KEY)

class BaseAgent:
    def __init__(self, model_name: str = "gemini-2.5-flash-lite", tools: List[Any] = None):
        self.model_name = model_name
        self.tools = tools or []
        self.model = genai.GenerativeModel(model_name=self.model_name, tools=self.tools)
        self.chat = self.model.start_chat(enable_automatic_function_calling=True)

    @trace_agent
    async def send_message(self, message: str) -> str:
        try:
            response = await self.chat.send_message_async(message)
            return response.text
        except Exception as e:
            return f"Error communicating with Gemini: {str(e)}"
