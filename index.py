import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello World AllAWS',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'eventdump': str(json.dumps(event))
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
