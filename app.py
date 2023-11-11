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
   
    if month is not None:
        try:
            month = int(month)
            df =  dp.processData('data_daily.csv')
            xTrain, yTrain = dp.splittingData(df)
            model = lp.LinearRegressionModel()
            model.fit(xTrain, yTrain)
            pred = int(model.predict(month))
            plt.scatter(xTrain, yTrain, label='Data Points')
            plt.plot(xTrain, model.predict(xTrain), color='red', label='Linear Regression')
            plt.scatter(month, pred, color='green', label=f'Predicted Value for Month {month}')
            plt.xlabel('Month')
            plt.ylabel('Receipt Count')
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.savefig('static\plot.png', format='png')
            plt.close()
                    
        except ValueError:  
            
            pred = "Invalid input. Please enter a valid month."
        
        return render_template('index.html', month=month, pred = pred)
 


















if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug = True)