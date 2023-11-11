Fetch -  Regression Model

The dataset we had at hand contained a single feature, the date, and the task was to predict a single label, the number of receipts. This falls into the category of classic regression, where we aim to predict numerical values. Given the simplicity of our dataset with only one continuous feature, I opted for a straightforward solution using a simple linear regression model.

Here's a brief rundown of the steps I followed:

Data Preprocessing: To prepare the data for modeling, I performed necessary preprocessing, ensuring it was in the correct format. This step involved checking for any missing values or anomalies in the dataset.

Data Grouping: Since we needed to work with monthly data, I grouped the dataset by month, which was a crucial step in our solution.

Feature and Label Separation: After the grouping, I divided the dataset into two parts: the feature set (X) and the label (Y).

Regression Model: I implemented a simple linear regression model using the reference from GeeksforGeeks (https://www.geeksforgeeks.org/linear-regression-python-implementation/#). This model allowed us to make predictions based on the input data.

Data Visualization: For visualization purposes, I utilized Matplotlib to create meaningful visual representations of the data.

Flask Web App: To make the model accessible and user-friendly, I developed a Flask web application. The application has a simple front-end, designed to take input in the form of a month. This input is then fed to the regression model, which predicts a value and provides a visual representation of the result.

Docker Container: I packaged the entire application into a Docker image, enabling easy deployment and running in a container. The Docker image worked successfully, ensuring that the application ran as intended.

GitHub Repository: Given the large size of the Docker image, I encountered difficulties with Docker Hub. As a result, I uploaded the code and related files to a GitHub repository for easy access.

To run this application locally, follow these steps:

1) Download and extract the provided zip folder.
2) Open your terminal and navigate to the extracted directory.
3) Execute the command pip install -r requirements.txt to install the necessary dependencies (assuming you have Python installed).
4) Run python app.py in the terminal, and you will be provided with a link to the locally hosted website.
5) Enter a month, and the application will predict a value and generate a corresponding plot.

This straightforward setup allows you to interact with the regression model and visualize the results effortlessly.
