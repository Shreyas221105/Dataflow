from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    
    df = pd.read_csv(file)

    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "mean": df.mean(numeric_only=True).to_dict()
    }

    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)
