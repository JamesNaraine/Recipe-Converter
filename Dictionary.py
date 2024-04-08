

Imperial_dictionary = {
    "lbs": {
        "measurement": "kg",
        "multiplier": 0.45,
        "round": 3  
    },
    "pint": {
        "measurement": "l",
        "multiplier": 0.473176,
        "round": 1  
    },
    "oz": {
        "measurement": "g",
        "multiplier": 28.3495,
        "round": 1  
    },
    "tsp": {
        "measurement": "ml",
        "multiplier": 4.92892,
        "round": 1  
    },
    "tbsp": {
        "measurement": "ml",
        "multiplier": 14.7868,
        "round": 1  
    },
    "quart": {
        "measurement": "l",
        "multiplier": 0.946353,
        "round": 1  
    },
    "gallon": {
        "measurement": "l",
        "multiplier": 3.78541,
        "round": 1  
    },
    "cup" :"",
    
    "cups" : ""
        
    }


Cup_conversion = {
    "flour": {
        "measurement": "g",
        "multiplier": 120  # Average for all-purpose flour
    },
    "sugar": {
        "measurement": "g",
        "multiplier": 200  # Granulated sugar
    },
    "brown_sugar": {
        "measurement": "g",
        "multiplier": 220  # Packed brown sugar
    },
    "butter": {
        "measurement": "g",
        "multiplier": 227  # One cup of butter
    },
    "honey": {
        "measurement": "g",
        "multiplier": 340  # Honey is denser than water
    },
    "milk": {
        "measurement": "ml",
        "multiplier": 240  # Approximation for whole milk
    },
    "water": {
        "measurement": "ml",
        "multiplier": 237  # One cup of water
    },
    "cocoa_powder": {
        "measurement": "g",
        "multiplier": 100  # Unsweetened cocoa powder
    },
    "oats": {
        "measurement": "g",
        "multiplier": 90   # Rolled oats
    },
    "yogurt": {
        "measurement": "g",
        "multiplier": 227  # Yogurt
    }
}

Metric_dictionary = {}

for key in Imperial_dictionary:
    unit_info = Imperial_dictionary[key]
    if 'multiplier' in unit_info and unit_info['multiplier']:
        Metric_dictionary[unit_info['measurement']] = {
            "measurement": key,
            "multiplier": float(round(1/unit_info['multiplier'],2))  ,
            "round" : unit_info["round"] }