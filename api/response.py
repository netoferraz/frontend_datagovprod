from typing import Optional, List
import requests
import json
def parse_ementa(ementa: str) -> Optional[List[str]]:
    url = 'https://pylegalclassifier.azurewebsites.net/predict'
    payload = {"ementa" : ementa}
    r = requests.post(url, json=payload)
    if r.status_code == 200:
        response = json.loads(r.text).get('tags')
        return response
    else:
        return None