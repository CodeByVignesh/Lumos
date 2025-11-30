from typing import Dict, Any, Optional
import uuid

class InMemorySessionService:
    def __init__(self):
        self._sessions: Dict[str, Dict[str, Any]] = {}
        self._long_running_ops: Dict[str, Dict[str, Any]] = {}

    def create_session(self, user_id: str) -> str:
        session_id = str(uuid.uuid4())
        self._sessions[session_id] = {
            "user_id": user_id,
            "history": [],
            "context": {}
        }
        return session_id

    def get_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        return self._sessions.get(session_id)

    def add_history(self, session_id: str, message: Dict[str, str]):
        if session_id in self._sessions:
            self._sessions[session_id]["history"].append(message)

    def get_history(self, session_id: str):
        return self._sessions.get(session_id, {}).get("history", [])

    # Long-running operation management
    def start_operation(self, op_type: str, params: Dict[str, Any]) -> str:
        op_id = str(uuid.uuid4())
        self._long_running_ops[op_id] = {
            "type": op_type,
            "params": params,
            "status": "running",
            "result": None
        }
        return op_id

    def get_operation_status(self, op_id: str) -> Optional[Dict[str, Any]]:
        return self._long_running_ops.get(op_id)

    def update_operation(self, op_id: str, status: str, result: Any = None):
        if op_id in self._long_running_ops:
            self._long_running_ops[op_id]["status"] = status
            if result:
                self._long_running_ops[op_id]["result"] = result

session_service = InMemorySessionService()
