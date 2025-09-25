
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from flask import Flask, request, render_template_string

from flask import Flask, request, render_template_string
import pandas as pd
from sklearn.model_selection import train_test_split
# Add XGBoost import
from xgboost import XGBClassifier

app = Flask(__name__)

UPLOAD_FORM = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Upload CSV for ML Accuracy</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap 5 CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container py-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card shadow">
                <div class="card-body">
                    <h1 class="card-title mb-4 text-center">Upload CSV File</h1>
                    <form method="post" enctype="multipart/form-data">
                        <div class="mb-3">
                            <input class="form-control" type="file" name="file" accept=".csv" required>
                        </div>
                        <div class="d-grid">
                            <button type="submit" class="btn btn-primary">Upload</button>
                        </div>
                    </form>
                    {% if accuracies %}
                        <hr>
                        <h2 class="mt-4 mb-3 text-center">Accuracies</h2>
                        <ul class="list-group">
                        {% for name, acc in accuracies.items() %}
                            <li class="list-group-item d-flex justify-content-between align-items-center">
                                {{ name }}
                                <span class="badge bg-success rounded-pill">{{ acc }}%</span>
                            </li>
                        {% endfor %}
                        </ul>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>
'''

def preprocess_data(df):
    # Encode categorical columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))
    return df

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    accuracies = {}
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            df = pd.read_csv(file)
            df = preprocess_data(df)
            df = df.dropna()
            X = df.iloc[:, :-1]
            y = df.iloc[:, -1]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            models = {
                'Random Forest': RandomForestClassifier(),
                'Logistic Regression': LogisticRegression(max_iter=1000),
                'Decision Tree': DecisionTreeClassifier(),
                'SVM': SVC(),
                'KNN': KNeighborsClassifier(),
                'XGBoost': XGBClassifier(use_label_encoder=False, eval_metric='logloss')
            }

            for name, model in models.items():
                try:
                    model.fit(X_train, y_train)
                    y_pred = model.predict(X_test)
                    acc = accuracy_score(y_test, y_pred)
                    accuracies[name] = round(acc * 100, 2)
                except Exception as e:
                    accuracies[name] = f"Error: {e}"

    return render_template_string(UPLOAD_FORM, accuracies=accuracies)

    app.run(debug=True) 
