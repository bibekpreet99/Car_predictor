from flask import Flask, request, render_template, redirect
import pickle
from numpy.core.fromnumeric import put

from numpy.lib.histograms import histogramdd
import sklearn
import numpy as np
from sklearn.preprocessing import StandardScaler



app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

# standard_to = StandardScaler()
@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('index.html', hidden = False, output = "")
    else:
        model = pickle.load(open('car.pkl', "rb"))
        fueld = 0
        manu = int(request.form.get('manu'))
        manu = 2021 - manu
        price = float(request.form.get('price'))
        dist = int(request.form.get('dist'))
        dist = np.log(dist)
        own = int(request.form.get('own'))
        fuelp = request.form.get('fuel')
        if fuelp == "Petrol":
            fuelp = 1
            fueld = 0
        else:
            fuelp = 0
            fueld = 1
        deal = request.form.get('deal')
        if deal == "Individual":
            deal = 1
        else:
            deal = 0
        trans = request.form.get('trans')
        if trans == "Manual":
            trans = 1
        else:
            trans = 0
        prediction = model.predict([[price, dist, own, manu, fueld, fuelp, deal, trans]])
        output = round(prediction[0], 2)
        if output<0:
            return render_template("index.html", hidden = True, output = 0)
        else:
            return render_template("index.html", hidden = True, output=output)