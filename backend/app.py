```python
from flask import Flask, request, jsonify
import ai_models
import social_media_integration

app = Flask(__name__)

@app.route('/generateSimulation', methods=['POST'])
def generate_simulation():
    adventureType = request.json['adventureType']
    simulationResult = ai_models.generateSimulation(adventureType)
    return jsonify(simulationResult=simulationResult)

@app.route('/shareSimulation', methods=['POST'])
def share_simulation():
    shareContent = request.json['shareContent']
    social_media_integration.shareSimulation(shareContent)
    return jsonify(status="Shared successfully")

if __name__ == '__main__':
    app.run(debug=True)
```