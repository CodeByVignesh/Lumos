import logging
import functools
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("PersonalConcierge")

def trace_agent(func):
    """Decorator to log agent invocations and latency."""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        agent_name = args[0].__class__.__name__ if args else "UnknownAgent"
        start_time = time.time()
        logger.info(f"Starting {agent_name} operation")
        try:
            result = await func(*args, **kwargs)
            duration = (time.time() - start_time) * 1000
            logger.info(f"Finished {agent_name} operation in {duration:.2f}ms")
            return result
        except Exception as e:
            duration = (time.time() - start_time) * 1000
            logger.error(f"Error in {agent_name} after {duration:.2f}ms: {str(e)}")
            raise
    return wrapper
