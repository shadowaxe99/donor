```javascript
let adventureType;
let simulationResult;
let shareContent;

window.onload = function() {
    document.getElementById('adventure-selection').addEventListener('change', selectAdventure);
    document.getElementById('share-button').addEventListener('click', shareSimulation);
}

function selectAdventure() {
    adventureType = document.getElementById('adventure-selection').value;
    fetch('/generateSimulation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ adventureType }),
    })
    .then(response => response.json())
    .then(data => {
        simulationResult = data.simulationResult;
        presentSimulation(simulationResult);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function presentSimulation(simulationResult) {
    document.getElementById('simulation-presentation').innerHTML = simulationResult;
}

function shareSimulation() {
    shareContent = simulationResult;
    fetch('/shareSimulation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ shareContent }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
```