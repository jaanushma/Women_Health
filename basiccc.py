from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import 

app = Flask(__name__)


# Load your clustering model here (this is a placeholder)
def get_recommendations(age, bmi, exercise_frequency, health_score):
    # Placeholder logic for recommendations
    if bmi < 18.5:
        return "Consider a nutrition plan to gain weight."
    elif 18.5 <= bmi < 25:
        return "Maintain a balanced diet and regular exercise."
    elif 25 <= bmi < 30:
        return "Focus on weight management and regular physical activity."
    else:
        return "Consult a healthcare provider for a weight loss plan."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recommendations', methods=['GET','POST'])
def get_recommendations_route():
  data1=request.form['a']
  data2=request.form['b']
  data3=request.form['c']
  data4=request.form['d']
#   data4=request.form['a']
arr=np.array([[data1,data2,data3,data4]])
pred=model.predict(arr)
if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
