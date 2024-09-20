from flask import Flask, jsonify
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/api/ml')
def predict():
    # Load the iris dataset
    iris = datasets.load_iris()
    X = iris.data  # Features
    y = iris.target  # Target variable

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a K-Nearest Neighbors classifier
    knn = KNeighborsClassifier(n_neighbors=3)

    # Train the classifier
    knn.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = knn.predict(X_test)

    # Get the accuracy of the model
    accuracy = knn.score(X_test, y_test)

    # Return the accuracy as JSON
    return jsonify({'accuracy': accuracy})
