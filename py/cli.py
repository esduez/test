#!/usr/bin/env python3
import sys
import os
import json

# Kritik yol ayarı
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from py.analyzer import analyze_package, get_tea_rewards

def main():
    try:
        command = sys.argv[1]
        if command == "analyze":
            result = analyze_package(sys.argv[2])
        elif command == "rewards":
            result = get_tea_rewards(sys.argv[2])
        print(json.dumps(result))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
