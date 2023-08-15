# Helper function
import os
import requests
import json

# Summarization endpoint
# Helper function
import requests
import json

# Summarization endpoint


def get_completion(inputs, parameters=None,
                   hf_api_key=os.environ['HF_API_KEY'],
                   endpoint_url=os.environ['HF_API_SUMMARY_BASE']):
    headers = {
        "Authorization": f"Bearer {hf_api_key}",
        "Content-Type": "application/json"
    }
    data = {"inputs": inputs}
    if parameters is not None:
        data.update({"parameters": parameters})
    response = requests.request("POST",
                                endpoint_url,
                                headers=headers,
                                data=json.dumps(data)
                                )
    return json.loads(response.content.decode("utf-8"))
