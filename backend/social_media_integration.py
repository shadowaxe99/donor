```python
import requests

def share_simulation(shareContent):
    # This function will share the simulation result on social media platforms.
    # For the purpose of this example, we will use a mock API endpoint.
    # In a real-world application, this function would integrate with actual social media APIs.

    # Define the API endpoint
    api_endpoint = "https://mockapi.io/share"

    # Define the headers
    headers = {
        "Content-Type": "application/json"
    }

    # Define the payload
    payload = {
        "content": shareContent
    }

    # Make the POST request to the API endpoint
    response = requests.post(api_endpoint, headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        print("Simulation shared successfully!")
    else:
        print("Failed to share the simulation. Please try again.")
```
