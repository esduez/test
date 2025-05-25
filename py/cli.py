#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import json
from analyzer import analyze_package

# Kritik yol ayarları
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Command argument required"}))
        sys.exit(1)
        
    command = sys.argv[1]
    
    try:
        if command == "analyze":
            pkg_name = sys.argv[2]
            result = analyze_package(pkg_name)
            print(json.dumps(result))
        elif command == "rewards":
            user_id = sys.argv[2]
            result = get_tea_rewards(user_id)  # analyzer.py'den import edilmeli
            print(json.dumps(result))
        else:
            raise ValueError(f"Unknown command: {command}")
            
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
