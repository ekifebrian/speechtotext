import http.client

def handler(request):
    task_id = request.args.get('task_id')
    if not task_id:
        return {
            'statusCode': 400,
            'body': '{"error": "task_id is required"}'
        }

    conn = http.client.HTTPSConnection("free-speech-to-text.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "6eee0a811amsh7a77be5602c86d9p17f2d0jsnb07651f3a6c0",
        'x-rapidapi-host': "free-speech-to-text.p.rapidapi.com"
    }
    conn.request("GET", f"/api/status?task_id={task_id}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return {
        'statusCode': res.status,
        'body': data.decode("utf-8")
    }
