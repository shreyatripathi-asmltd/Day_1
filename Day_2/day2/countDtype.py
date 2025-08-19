def count_types(data, counts):
    if isinstance(data, dict):
        counts['dict'] += 1
        for value in data.values():
            count_types(value, counts)
    elif isinstance(data, list):
        counts['list'] += 1
        for item in data:
            count_types(item, counts)
    elif isinstance(data, tuple):
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

#JSON
'''machinery_data = {
    "machine_name": "Excavator",       # string
    "id": 101,                         # integer
    "weight_tons": 21.5,               # float
    "parts": ["engine", "hydraulics", "tracks"],  # list of strings
    "maintenance_records": [           # list of dicts
        {"date": "2025-01-15", "status": "oil_changed"},
        {"date": "2025-04-10", "status": "hydraulic_fluid_checked"}
    ],
    "specs": (                         # tuple with mixed values
        "Tier-4 Engine", 
        {"horsepower": 210, "fuel_type": "diesel"}, 
        [500, 1000, 1500]              # rpm ranges
    ),
    "performance": {                   # nested dictionary
        "fuel_efficiency": [6.5, 7.0, 7.2],  # floats
        "load_capacity": (1.5, 2.0, 2.3),    # floats
        "peak_output": {"rpm": 1800, "torque_nm": 1200}
    }
}'''
machinery_data = {
    "machine_name": "Excavator",   
    "id": 101,                     
    "weight_tons": 21.5,           

    # Parts as list
    "parts": ["engine", "hydraulics", "tracks"],

    # Maintenance as list of tuples
    "maintenance_records": [
        ("2025-01-15", "oil_changed"),
        ("2025-04-10", "hydraulic_fluid_checked")
    ],

    # Specs (tuple + list)
    "specs": (
        "Tier-4 Engine", 
        (210, "diesel"),          # horsepower, fuel_type tuple
        [500, 1000, 1500]         # rpm ranges as list
    ),

    # Performance
    "fuel_efficiency": [6.5, 7.0, 7.2],  # list
    "load_capacity": (1.5, 2.0, 2.3),    # tuple
    "peak_output": (1800, 1200)          # tuple (rpm, torque_nm)
}


count_types(machinery_data, counts)


print("Data type counts:")
for dtype, count in counts.items():
    if count > 0:
        print(f"{dtype}: {count}")
