# Fitness Recommendation System

## Overview

The AI Fitness Recommendation System is a machine learning-based web application built with Django that provides personalized fitness and nutrition recommendations based on user information.

The system analyzes user inputs such as age, weight, height, diet preference, fitness goal, and experience level to generate customized workout plans, diet suggestions, and fitness insights.

---

## Features

### User Input Form

* Age
* Weight
* Height
* Diet Preference

  * Vegetarian
  * Non-Vegetarian
* Fitness Goal

  * Weight Loss
  * Muscle Gain
  * Maintenance
* Experience Level

### Fitness Analytics

* BMI Calculation
* Daily Calorie Estimation
* Fitness Cluster Prediction
* Personalized Exercise Recommendations
* Personalized Recipe Recommendations

### Interactive Dashboard

* BMI Dashboard Card
* Calories Dashboard Card
* Cluster Dashboard Card
* Nutrition Pie Chart
* BMI Analysis Chart
* Weekly Workout Chart
* Weekly Workout Schedule
* Responsive Bootstrap UI

---

## Technologies Used

### Backend

* Python
* Django

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Pickle

### Frontend

* HTML
* CSS
* Bootstrap 5
* Chart.js

---

## Project Structure

```text
FitnessProject/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── data/
│   ├── exercises.csv
│   ├── fitness.csv
│   ├── recipes.csv
│   ├── model.pkl
│   ├── scaler.pkl
│   ├── goal.pkl
│   ├── diet.pkl
│   └── exp.pkl
│
├── recommender/
│   ├── templates/
│   │   ├── home.html
│   │   └── result.html
│   │
│   ├── views.py
│   ├── recommendation.py
│   ├── models.py
│   └── urls.py
│
├── manage.py
└── README.md
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/fitness-recommendation-system.git
```

### 2. Move to Project Folder

```bash
cd fitness-recommendation-system
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Machine Learning Workflow

1. Load fitness dataset
2. Encode categorical features
3. Scale numerical features
4. Train recommendation model
5. Save model using Pickle
6. Predict user fitness cluster
7. Generate workout recommendations
8. Generate diet recommendations

---

## Dashboard Outputs

### Fitness Metrics

* BMI Score
* Daily Calories
* Fitness Cluster

### Recommendation Tables

* Exercises
* Recipes

### Charts

* BMI Analysis Chart
* Nutrition Distribution Chart
* Weekly Workout Chart

---

## Author

Mann

---

## Disclaimer

This project is created for educational and learning purposes.