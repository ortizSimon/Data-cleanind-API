from flask import Flask, jsonify
import pandas as pd
import os
from utils.data_processing import clean_data, get_summary, get_correlations

app = Flask(__name__)

SAMPLE_DATA_PATH = os.path.join('data', 'sample.csv')


@app.route('/clean', methods=['GET'])
def clean():
    try:
        df = pd.read_csv(SAMPLE_DATA_PATH)
        cleaned_df = clean_data(df)
        
        # Return cleaned data as JSON
        result = {
            "original_rows": len(df),
            "cleaned_rows": len(cleaned_df),
            "duplicates_removed": len(df) - len(cleaned_df),
            "data": cleaned_df.to_dict(orient='records')
        }
        
        return jsonify(result)
    
    except FileNotFoundError:
        return jsonify({"error": "Sample data file not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/summary', methods=['GET'])
def summary():
    try:
        df = pd.read_csv(SAMPLE_DATA_PATH)
        cleaned_df = clean_data(df)
        stats = get_summary(cleaned_df)
        return jsonify(stats)
    
    except FileNotFoundError:
        return jsonify({"error": "Sample data file not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/correlation', methods=['GET'])
def correlation():
    try:
        df = pd.read_csv(SAMPLE_DATA_PATH)
        cleaned_df = clean_data(df)
        corr = get_correlations(cleaned_df)
        return jsonify(corr)
    
    except FileNotFoundError:
        return jsonify({"error": "Sample data file not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "service": "Data Cleaning & Summary API",
        "endpoints": {
            "/clean": "Cleans sample data and returns JSON",
            "/summary": "Returns summary statistics",
            "/correlation": "Returns correlation matrix"
        }
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)

