import json
import sys
from analyzer import analyze_package

def main():
    try:
        command = sys.argv[1]
        if command == "analyze":
            result = analyze_package(sys.argv[2])
            print(json.dumps(result))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
