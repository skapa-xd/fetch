import pandas as pd
import matplotlib.pyplot as plt


def processData(file):
    df = pd.read_csv(file) # read file
    
    df = df.dropna() # drop missing values
    
    df["Month"] = pd.to_datetime(df["# Date"]).dt.month # get in M format
    df = df.sort_values(by=["Month"], ascending=True)

    grouped_df = df.groupby("Month") # groupby month
    total_receipt_count_per_month = grouped_df["Receipt_Count"].sum() # get total number of count/month


    output_df = pd.DataFrame({
        "Month": total_receipt_count_per_month.index,
        "Receipt Count": total_receipt_count_per_month.values
    })
    
    return output_df

def splittingData(df):
    X = df['Month']   # feature
    Y = df['Receipt Count'] # label
    
    return X, Y

def plot(xTrain, yTrain, month, pred, model):
    plt.scatter(xTrain, yTrain, label='Data Points')
    plt.plot(xTrain, model.predict(xTrain), color='red', label='Linear Regression')
    plt.scatter(month, pred, color='green', label=f'Predicted Value for Month {month}')
    plt.xlabel('Month')
    plt.ylabel('Receipt Count')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    