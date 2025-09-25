# ML Accuracy Evaluator - Flask Web Application

A simple Flask web application that automatically evaluates multiple machine learning algorithms on uploaded CSV datasets and displays their accuracy scores.

## 🚀 Features

- **Easy CSV Upload**: Upload any CSV file through a clean web interface
- **Automatic Preprocessing**: Handles categorical variables with label encoding
- **Multiple ML Algorithms**: Tests 5 different classification algorithms:
  - Random Forest Classifier
  - Logistic Regression
  - Decision Tree Classifier
  - Support Vector Machine (SVM)
  - K-Nearest Neighbors (KNN)
- **Accuracy Comparison**: Displays accuracy percentages for all models
- **Bootstrap UI**: Clean, responsive web interface using Bootstrap 5
- **Error Handling**: Graceful error handling for problematic datasets

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🛠️ Installation

1. **Clone or download the repository**
```bash
git clone <your-repo-url>
cd flask-ml-evaluator
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install required packages**
```bash
pip install flask pandas scikit-learn
```

## 📦 Dependencies

The application requires the following Python packages:
- Flask (web framework)
- pandas (data manipulation)
- scikit-learn (machine learning algorithms)

## 🗂️ File Structure

```
flask-ml-evaluator/
│
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies (create this)
└── README.md          # This file
```

Create a `requirements.txt` file with:
```
Flask==2.3.3
pandas==2.0.3
scikit-learn==1.3.0
```

## 🚀 Usage

1. **Start the Flask application**
```bash
python app.py
```

2. **Open your web browser** and navigate to:
```
http://localhost:5000
```

3. **Upload a CSV file** using the web interface:
   - Click "Choose File" and select your CSV
   - Click "Upload" to process the file
   - View accuracy results for all ML algorithms

## 📊 Data Requirements

- **CSV Format**: Upload files must be in CSV format
- **Target Column**: The application assumes the **last column** is the target variable
- **Data Types**: Mixed data types are supported (numerical and categorical)
- **Missing Values**: Rows with missing values are automatically removed
- **Classification Only**: Currently supports classification tasks only

## 🔧 How It Works

1. **Data Loading**: Reads uploaded CSV file using pandas
2. **Preprocessing**: 
   - Applies Label Encoding to all categorical columns
   - Removes rows with missing values
   - Separates features (all columns except last) and target (last column)
3. **Train-Test Split**: Uses 80% for training, 20% for testing
4. **Model Training**: Trains 5 different ML algorithms
5. **Evaluation**: Calculates accuracy score for each model
6. **Results Display**: Shows results in a clean web interface

## ⚙️ Configuration

The application uses default parameters for all ML algorithms. To customize:

- **Test Size**: Change `test_size=0.2` in the `train_test_split` function
- **Random State**: Modify `random_state=42` for different data splits
- **Model Parameters**: Add parameters to model initialization (e.g., `RandomForestClassifier(n_estimators=200)`)

## 🚨 Troubleshooting

**Common Issues:**

1. **"Module not found" error**: Ensure all dependencies are installed
2. **Upload fails**: Check file format is CSV and contains data
3. **Low accuracy**: Dataset might be too small or target column incorrect
4. **Memory errors**: Large datasets may require more RAM

**Error Messages:**
- If a model fails to train, "Error" will be displayed instead of accuracy
- Check console output for detailed error messages

## 🔒 Security Considerations

**⚠️ Important**: This is a development application. For production use:
- Add file size limits
- Validate uploaded files
- Implement proper error logging
- Use secure file upload practices
- Set up proper authentication

## 🚀 Deployment

For production deployment:

1. **Set Flask environment**:
```bash
export FLASK_ENV=production
```

2. **Use a WSGI server** like Gunicorn:
```bash
pip install gunicorn
gunicorn --bind 0.0.0.0:5000 app:app
```

3. **Deploy to cloud platforms**:
   - Heroku
   - AWS Elastic Beanstalk
   - Google Cloud Platform
   - DigitalOcean

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created for educational purposes to demonstrate Flask ML model deployment.

***

**Happy Machine Learning! 🎯**
