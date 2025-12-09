import pytest
import pandas as pd
import numpy as np
from utils.data_processing import clean_data, get_summary, get_correlations


def test_clean_data_removes_duplicates():
    """Test that clean_data removes duplicate rows."""
    data = {
        'id': [1, 2, 3, 1, 2],
        'value': [10, 20, 30, 10, 20]
    }
    df = pd.DataFrame(data)
    
    cleaned = clean_data(df)
    
    assert len(cleaned) == 3
    assert len(df) == 5  # original has duplicates


def test_clean_data_converts_types():
    """Test that clean_data converts string numbers to numeric."""
    data = {
        'id': ['1', '2', '3'],
        'value': ['10.5', '20.3', '30.1']
    }
    df = pd.DataFrame(data)
    
    cleaned = clean_data(df)
    
    assert pd.api.types.is_numeric_dtype(cleaned['id'])
    assert pd.api.types.is_numeric_dtype(cleaned['value'])


def test_get_summary_returns_stats():
    """Test that get_summary returns correct statistics."""
    data = {
        'age': [25, 30, 35, 40, 45],
        'salary': [50000, 60000, 70000, 80000, 90000]
    }
    df = pd.DataFrame(data)
    
    summary = get_summary(df)
    
    assert 'age' in summary
    assert 'salary' in summary
    assert summary['age']['mean'] == 35.0
    assert summary['age']['min'] == 25.0
    assert summary['age']['max'] == 45.0


def test_get_summary_no_numeric():
    """Test get_summary with no numeric columns."""
    data = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'department': ['Eng', 'Sales', 'Marketing']
    }
    df = pd.DataFrame(data)
    
    summary = get_summary(df)
    
    assert 'message' in summary
    assert 'No numeric columns' in summary['message']


def test_get_correlations():
    """Test that get_correlations returns correlation matrix."""
    data = {
        'x': [1, 2, 3, 4, 5],
        'y': [2, 4, 6, 8, 10]  # perfect correlation
    }
    df = pd.DataFrame(data)
    
    corr = get_correlations(df)
    
    assert 'x' in corr
    assert 'y' in corr
    assert abs(corr['x']['y'] - 1.0) < 0.001
    assert abs(corr['y']['x'] - 1.0) < 0.001


def test_get_correlations_no_numeric():
    """Test get_correlations with no numeric columns."""
    data = {
        'name': ['Alice', 'Bob'],
        'dept': ['Eng', 'Sales']
    }
    df = pd.DataFrame(data)
    
    corr = get_correlations(df)
    
    assert 'message' in corr
    assert 'No numeric columns' in corr['message']

