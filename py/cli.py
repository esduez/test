import json
import sys
from analyzer import analyze

def main():
    if len(sys.argv) > 1:
        result = analyze(sys.argv[1])
        print(json.dumps(result))

if __name__ == "__main__":
    main()
