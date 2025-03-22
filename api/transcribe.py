import http.client
import json

def handler(request):
    payload = request.json
    if not payload or 'url' not in payload:
        return {
            'statusCode': 400,
            'body': '{"error": "URL is required"}'
        }

    conn = http.client.HTTPSConnection("free-speech-to-text.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "6eee0a811amsh7a77be5602c86d9p17f2d0jsnb07651f3a6c0",
        'x-rapidapi-host': "free-speech-to-text.p.rapidapi.com",
        'Content-Type': "application/json"
    }
    conn.request("POST", "/api/transcribe", body=json.dumps(payload), headers=headers)
    res = conn.getresponse()
    data = res.read()
    return {
        'statusCode': res.status,
        'body': data.decode("utf-8")
    }
