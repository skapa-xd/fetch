import dataProcessing as dp
import linearRegression as lp
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template, request
from flask import send_file


app = Flask(__name__)

    

@app.route('/', methods=['GET', 'POST'])
def index():
    
    month = request.form.get('month')
    pred = None
    plot = None
   
  # If the user has submitted the form, predict the receipt count and plot the scatterplot.
    if month is not None:
        try:
            month = int(month)
            df =  dp.processData('data_daily.csv')
            xTrain, yTrain = dp.splittingData(df)
            model = lp.LinearRegressionModel()
            model.fit(xTrain, yTrain)
            pred = int(model.predict(month))
            dp.plot(xTrain, yTrain, month, pred, model)
            
        except ValueError:  
            
            pred = "Invalid input. Please enter a valid month."
        

    # Render the main page template.
    return render_template('index.html', month=month, pred = pred)
 


















if __name__ == "__main__":
    app.run(debug = True)