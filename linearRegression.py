class LinearRegressionModel:
    def __init__(self):
        self.slope = None
        self.intercept = None

    def fit(self, X, y):
        x_mean = X.mean()
        y_mean = y.mean()
        xy_mean = (X * y).mean()
        x_squared_mean = (X ** 2).mean()
        self.slope = (x_mean * y_mean - xy_mean) / (x_mean ** 2 - x_squared_mean)
        self.intercept = y_mean - self.slope * x_mean

    def predict(self, X):
        return self.intercept + self.slope * X