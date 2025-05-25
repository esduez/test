
import requests
from typing import Dict, List

def analyze_package(package_name: str) -> Dict:
    """Paket bağımlılıklarını analiz eder"""
    dummy_data = {
        "flask": ["werkzeug", "jinja2", "itsdangerous"],
        "numpy": []
    }
    
    return {
        "name": package_name,
        "dependencies": dummy_data.get(package_name, []),
        "tea_rewards": len(package_name) * 0.5
    }

def get_tea_rewards(user_id: str) -> Dict:
    """Kullanıcının TEA ödüllerini getirir"""
    return {
        "user_id": user_id,
        "rewards": 42.0,
        "currency": "TEA"
