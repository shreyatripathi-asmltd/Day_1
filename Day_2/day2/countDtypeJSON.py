import json
import pandas as pd

# recursive type counter
def count_types(data, counts):
    if isinstance(data, dict):
        counts['dict'] += 1
        for value in data.values():
            count_types(value, counts)
    elif isinstance(data, list):
        counts['list'] += 1
        for item in data:
            count_types(item, counts)
    elif isinstance(data, tuple):  #json converts tuple to list
        counts['tuple'] += 1
        for item in data:
            count_types(item, counts)
    elif isinstance(data, int):
        counts['int'] += 1
    elif isinstance(data, float):
        counts['float'] += 1
    elif isinstance(data, str):
        counts['str'] += 1
    elif isinstance(data, bool):
        counts['bool'] += 1
    elif data is None:
        counts['NoneType'] += 1
    else:
        counts['unknown'] += 1

def main():
    counts = {
        'int': 0,
        'float': 0,
        'str': 0,
        'bool': 0,
        'NoneType': 0,
        'list': 0,
        'tuple': 0,
        'dict': 0,
        'unknown': 0
    }

    
    with open("collection.json", "r") as f:
        data = json.load(f)

    # Count types
    count_types(data, counts)

    # Put into DataFrame
    df = pd.DataFrame(list(counts.items()), columns=["Data Type", "Count"])
    df = df[df["Count"] > 0]  # remove zeros

    # Show table
    print(df)


if __name__ == "__main__":
    main()
