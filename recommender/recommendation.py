import pandas as pd
import joblib

exercise_df = pd.read_csv("data/exercises.csv")
recipe_df = pd.read_csv("data/recipes.csv")

kmeans = joblib.load("data/model.pkl")
scaler = joblib.load("data/scaler.pkl")

goal_encoder = joblib.load("data/goal.pkl")
diet_encoder = joblib.load("data/diet.pkl")
exp_encoder = joblib.load("data/exp.pkl")


def calculate_bmi(weight,height):

    return round(
        weight / ((height/100)**2),
        2
    )


def calculate_calories(weight,height,age):

    bmr = (
        10 * weight +
        6.25 * height -
        5 * age +
        5
    )

    return round(bmr)


def predict_cluster(
    age,
    weight,
    height,
    bmi,
    goal,
    diet,
    experience
):

    goal = goal_encoder.transform(
        [goal]
    )[0]

    diet = diet_encoder.transform(
        [diet]
    )[0]

    experience = exp_encoder.transform(
        [experience]
    )[0]

    user = [[
        age,
        weight,
        height,
        bmi,
        goal,
        diet,
        experience
    ]]

    user = scaler.transform(user)

    cluster = kmeans.predict(user)

    return cluster[0]


def recommend_exercises(level):

    result = exercise_df[
        exercise_df["level"]
        .str.lower()
        ==
        level.lower()
    ]

    return result.sample(
        min(10,len(result))
    )


def recommend_recipes(diet):

    result = recipe_df[
        recipe_df["diet_type"]
        .str.lower()
        ==
        diet.lower()
    ]

    return result.sample(
        min(5,len(result))
    )

nn = joblib.load("data/nn.pkl")

def get_similar_users(user_data):

    distances, indices = nn.kneighbors(
        user_data
    )

    return indices