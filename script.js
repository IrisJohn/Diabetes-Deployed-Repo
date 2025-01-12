document.getElementById("diabetesForm").addEventListener("submit", function(event) {
    event.preventDefault();

    // Get input values from the form
    const age = document.getElementById("age").value;
    const bmi = document.getElementById("bmi").value;
    const glucose = document.getElementById("glucose").value;
    const bloodPressure = document.getElementById("bloodPressure").value;

    // Create an object with the input data
    const inputData = {
        age: age,
        bmi: bmi,
        glucose: glucose,
        bloodPressure: bloodPressure,
        pregnancies : 1,
        skinThickness : 0.02,
        insulin:0.5,
        diabetesPedigreeFunction :1

    };

    // Send data to the backend (Flask app)
    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(inputData)
    })
    .then(response => response.json())
    .then(data => {
        // Display the result from the backend
        const resultDiv = document.getElementById("result");
        resultDiv.innerHTML = data.prediction === 1 ? "High Risk of Diabetes" : "Low Risk of Diabetes";
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
