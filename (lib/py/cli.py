import sys
import json
from analyzer import analyze_package

def main():
    command = sys.argv[1]
    
    if command == "analyze":
        pkg = sys.argv[2]
        result = analyze_package(pkg)
        print(json.dumps(result))
        
if __name__ == "__main__":
    main()
