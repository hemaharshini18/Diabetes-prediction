function predict() {
    const pregnancies = document.getElementById('pregnancies').value;
    const glucose = document.getElementById('glucose').value;
    const bloodPressure = document.getElementById('bloodPressure').value;
    const bmi = document.getElementById('bmi').value;
    const dpf = document.getElementById('dpf').value;
    const age = document.getElementById('age').value;

    if (!pregnancies || !glucose || !bloodPressure || !bmi || !dpf || !age) {
        alert('Please fill in all fields');
        return;
    }

    const data = {
        features: [
            Number(pregnancies),
            Number(glucose),
            Number(bloodPressure),
            0, // Skin thickness
            0, // Insulin
            Number(bmi),
            Number(dpf),
            Number(age)
        ]
    };

    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        const resultElement = document.getElementById('result');
        const resultContainer = document.getElementById('resultContainer');
        resultContainer.classList.add('visible');

        resultElement.textContent = data.prediction === "Diabetic" 
            ? "Warning! You show symptoms of diabetes. Please consult a doctor." 
            : "No need to fear! You have no dangerous symptoms of the disease.";
        
        resultElement.className = data.prediction === "Diabetic" ? "result negative" : "result positive";
    })
    .catch(error => alert('An error occurred. Please try again.'));
}
