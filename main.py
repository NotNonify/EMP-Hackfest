from flask import Flask, request
from flask import render_template
import random

app = Flask(__name__)

foodList = []
caloriesList = []
carbonConversion = {
        "Beef":99.48,
        "Poultry":6.9,
        "Fish":5,
        "Coffee":17,
        "Cheese":21,
        "Lamb":24,
        "Chocolate": 19,
        "Prawns": 12,
        "Pork": 7,
        "Eggs": 4.5,
    }

tips = [
    "Eat More Plant-Based",
    "Local and Seasonal",
    "Reduce Food Waste",
    "Cut Down on Packaging",
    "Choose Sustainable Seafood",
    "Drink Tap Water",
    "Limit Processed Foods",
    "Use Energy-Efficient Appliances",
    "Compost",
    "Educate Yourself",
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/calculate", methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        selection = request.form.get('food')
        calories = request.form.get('calories')

        if selection != '' and calories != '':
            if selection in foodList:
                caloriesList[foodList.index(selection)] = calories
            else:
                foodList.append(selection)
                caloriesList.append(calories)

    return render_template("calculate.html", foodList=foodList, caloriesList=caloriesList, length=len(foodList))

@app.route("/displayFootprint")
def displayFootprint():
    caloriesSum = 0
    carbonSum = 0
    for i in range(len(foodList)):
        multiply = carbonConversion[foodList[i]]
        caloriesSum += int(caloriesList[i])
        co2kg = multiply * int((int(caloriesList[i])/7716))
        carbonSum += co2kg


    tipsList = random.sample(tips, 3)
   
    return render_template("displayFootprint.html", footprint=int(carbonSum), calories=caloriesSum, tips=tipsList)


@app.route("/information")
def information():
    return render_template("information.html")


if __name__ == "__main__":
    app.run(debug=True)

