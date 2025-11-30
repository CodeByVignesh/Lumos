import random
from typing import List, Dict, Any

class GroceryStoreTool:
    def get_prices(self, items: List[str]) -> Dict[str, float]:
        """Mock API to get prices for a list of items."""
        prices = {}
        for item in items:
            # Generate a random price between 1.0 and 10.0
            prices[item] = round(random.uniform(1.0, 10.0), 2)
        return prices

class FlightSearchTool:
    def search_flights(self, origin: str, destination: str, date: str) -> List[Dict[str, Any]]:
        """Mock API to search for flights."""
        return [
            {"airline": "MockAir", "price": 150, "time": "10:00 AM", "duration": "2h"},
            {"airline": "CheapFly", "price": 120, "time": "06:00 AM", "duration": "2h 15m"},
        ]

class HotelSearchTool:
    def search_hotels(self, city: str, check_in: str) -> List[Dict[str, Any]]:
        """Mock API to search for hotels."""
        return [
            {"name": "Grand Mock Hotel", "price": 200, "rating": 4.5},
            {"name": "Budget Inn", "price": 80, "rating": 3.0},
        ]
