import json
from datetime import datetime, timezone

def lambda_handler(event, context):
    print("Incoming event:", json.dumps(event))

    params = event.get("queryStringParameters") or {}
    name = params.get("name", "Unknown")

    response = {
        "message": f"Hello {name} from Python!",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(response)
    }