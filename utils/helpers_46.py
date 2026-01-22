"""Utility functions for legendary-dollop"""

import datetime
from typing import Optional, List, Dict

def format_date(date: datetime.datetime) -> str:
    """Format date to string.
    
    Args:
        date: Date object to format
        
    Returns:
        Formatted date string
    """
    if not date:
        return ''
    return date.strftime('%Y-%m-%d')

def validate_email(email: str) -> bool:
    """Validate email format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not email:
        return False
    import re
    pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return bool(re.match(pattern, email))

def safe_divide(a: float, b: float) -> Optional[float]:
    """Safely divide two numbers.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Result or None if division by zero
    """
    if b == 0:
        return None
    return a / b

def filter_valid_items(items: List[Dict]) -> List[Dict]:
    """Filter out invalid items from list."""
    return [item for item in items if item and isinstance(item, dict)]


"""
Legendary Dollop - Code Refactoring
Legendary Dollop
"""

from typing import List, Dict, Optional

def optimize_algorithm(data: List[Dict]) -> List[Dict]:
    """Optimized version with better performance"""
    return [
        {**item, 'processed': True}
        for item in data
        if item.get('active', True)
    ]

def extract_metadata(obj: Dict) -> Optional[Dict]:
    """Extract metadata with type hints"""
    if not isinstance(obj, dict):
        return None
    
    return {
        'id': obj.get('id'),
        'timestamp': obj.get('timestamp'),
        'version': obj.get('version', '1.0.0')
    }
