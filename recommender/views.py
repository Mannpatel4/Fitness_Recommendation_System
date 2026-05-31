from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .recommendation import *

def home(request):

    if request.method == "POST":

        age = int(
            request.POST["age"]
        )

        weight = float(
            request.POST["weight"]
        )

        height = float(
            request.POST["height"]
        )

        diet = request.POST["diet"]

        goal = request.POST["goal"]

        experience = request.POST[
            "experience"
        ]

        bmi = calculate_bmi(
            weight,
            height
        )

        calories = calculate_calories(
            weight,
            height,
            age
        )

        cluster = predict_cluster(
            age,
            weight,
            height,
            bmi,
            goal,
            diet,
            experience
        )

        exercises = (
            recommend_exercises(
                experience
            )
            .to_dict("records")
        )

        recipes = (
            recommend_recipes(
                diet
            )
            .to_dict("records")
        )
        protein = 0
        carbs = 0
        fat = 0

        for recipe in recipes:

            protein += recipe["protein(g)"]
            carbs += recipe["carbs(g)"]
            fat += recipe["fat(g)"]

        protein = round(protein / len(recipes), 2)
        carbs = round(carbs / len(recipes), 2)
        fat = round(fat / len(recipes), 2)

        # context["protein"] = protein
        # context["carbs"] = carbs
        # context["fat"] = fat
        workout_minutes = [60,45,60,45,60,30,0]

        context = {
            "bmi": bmi,
            "calories": calories,
            "cluster": cluster,

            "goal": goal,
            "diet": diet,
            "experience": experience,

            "exercises": exercises,
            "recipes": recipes,

            "protein": protein,
            "carbs": carbs,
            "fat": fat,

            "workout_minutes": workout_minutes,

        }

        return render(
            request,
            "result.html",
            context
        )

    return render(
        request,
        "home.html"
    )