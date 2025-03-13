document.getElementById('healthForm').addEventListener('submit', function(event)
 {
    event.preventDefault(); // Prevent form submission

    // Get user input values
    const age = document.getElementById('age').value;
    const bmi = document.getElementById('bmi').value;
    const exercise_frequency = document.getElementById('exercise_frequency').value;
    const health_score = document.getElementById('health_score').value;

    // Get recommendations based on BMI
    const recommendations = getRecommendations(bmi);

    // Display recommendations
    document.getElementById('recommendations').innerText = recommendations;
});

function getRecommendations(bmi) 
{
    // Recommendation logic based on BMI
    if (bmi < 18.5) {
        return "Consider a nutrition plan to gain weight.";
    } else if (18.5 <= bmi && bmi < 25) {
        return "Maintain a balanced diet and regular exercise.";
    } else if (25 <= bmi && bmi < 30) {
        return "Focus on weight management and regular physical activity.";
    } else {
        return "Consult a healthcare provider for a weight loss plan.";
    }
}