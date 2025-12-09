# Data Cleaning & Summary API

Simple Flask API for cleaning datasets and getting summary statistics.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask server:
```bash
python app.py
```

The server will start on `http://localhost:5000`

## Endpoints

- `GET /` - API information
- `GET /clean` - Loads sample CSV, removes duplicates, fixes types, returns cleaned data
- `GET /summary` - Returns summary statistics (mean, min, max, etc.) for numeric columns
- `GET /correlation` - Returns correlation matrix for numeric columns

## Testing

Run tests with pytest:
```bash
pytest tests/
```

## Project Structure

```
project/
├── app.py                 # Flask application
├── data/
│   └── sample.csv        # Sample dataset
├── utils/
│   └── data_processing.py # Data cleaning and analysis functions
├── tests/
│   └── test_processing.py # Unit tests
└── requirements.txt       # Dependencies
```

