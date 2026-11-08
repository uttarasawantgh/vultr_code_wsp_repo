import sys
import asyncio
from core.router import CoreSwitchyardRouter

def main():
    prompt = sys.argv[1] if len(sys.argv) > 1 else "Perform routine maintenance clearance check on Cabinet B."
    
    router = CoreSwitchyardRouter()
    try:
        model_used, result = router.route(prompt)
        print(f"[ROUTING_MODEL]: {model_used}")
        print(f"[ROUTING_STATUS]: LOCAL_RESOLVED")
        print(f"[ROUTING_OUTCOME]: {result}")
    except Exception as e:
        print(f"[ROUTING_MODEL]: error")
        print(f"[ROUTING_STATUS]: FAILED")
        print(f"[ROUTING_OUTCOME]: Execution error: {str(e)}")

if __name__ == "__main__":
    main()