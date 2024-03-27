input_text = """4/5 lbs of meat
1 pint of beer
1/4 cup plain yogurt
2 Tbsp. unsalted butter (melted)
2 Tbsp. pure maple syrup
1/2 tsp. pure vanilla extract
1 1/2 cups blanched almond flour
1/2 tsp. baking soda
1/4 tsp. sea salt
2 eggs
1 egg whites
1/3 cup berries"""

input_text = input_text.replace("\n"," ")
a  = input_text.split(" ")


a = [item for item in a if item != ""]
print("")
print("This is the input")
print("")
print("")
print(a)

# int = 1,2 ,3 ,4 ,68

# floats = 4.5,6.7 3.141558985


def convert_fraction(x,y):
    x = float(x)
    y = float(y)
    return round(x / y, 2)

print(convert_fraction(1,4))


def find_slash(string):
    index_slash = 0
    x = ""
    y = ""

    if "/" in string:
        for i in range(0,len(string)):
            if string[i] == "/":
                index_slash = i
    
        x = string[:index_slash]
        y = string[index_slash+1:]

        return convert_fraction(x,y)
    else:
        return(string)

output = []

for item in a:
    output.append(find_slash(item))

print("")
print("this is the output before the main loop, after the slash conversion")
print("")
print(output)

a = output
output = []

# find_slash("144/162")

Reciepe_conversion = {
    "lbs" : {
        "measurement": "kg",
        "multiplier" : 0.45
    },
    "pint": {
        "measurement": "l",
        "multiplier": 0.473176
    },
    "lbs": {
        "measurement": "kg",
        "multiplier": 0.453592
    },
    "oz": {
        "measurement": "g",
        "multiplier": 28.3495
    },
    "tsp": {
        "measurement": "ml",
        "multiplier": 4.92892
    },
    "tbsp": {
        "measurement": "ml",
        "multiplier": 14.7868
    },

    "pint": {
        "measurement": "l",
        "multiplier": 0.473176
    },
    "quart": {
        "measurement": "l",
        "multiplier": 0.946353
    },
    "gallon": {
        "measurement": "l",
        "multiplier": 3.78541
    },
    "cup": "",
    "cups": ""
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


print("")
print("this is the output before the main loop, after the slash conversion")
print("")
print(output)

count = 0

for word in a:
    subcount = 0
    
    count += 1
    item = str(word).lower()
    
    print(f"current item = {item}")
    previous_value = 0
    # if it is, remove the previous entry to a and convert the value
    if item.lower() in Reciepe_conversion.keys():
        previous_value = float(output[-1])
        print(f"previous value = {previous_value}")
        output.pop()
        if item.lower() == "cup" or item.lower() == "cups":
            print(f"Cup Checking {item}")
            print(f"count number = {count}")
            for i in range(count+1,min(count+5,len(a))):
                if subcount > 0:
                    break
                print(f"Checking {a[i]}")
                if a[i] in Cup_conversion.keys():
                    output.append(round(previous_value * float(Cup_conversion[a[i]]["multiplier"]),3))
                    output.append(Cup_conversion[a[i]]["measurement"])
                    subcount += 1
                    
                    
            if subcount == 0 :
                output.append(round(previous_value * float(200),3))
                output.append("g")
                                        
            
        else: 
        
            output.append(round(previous_value * float(Reciepe_conversion[item]["multiplier"]),3))
            output.append(Reciepe_conversion[item]["measurement"])
    else:
        output.append(item)
        # if a isn't in the receipe conversion dictionary pass


print(f"current output= {output}")
    

print("")
print("this is the output")
print("")

final = ""

for i in output:
    final += str(i) 
    final += " "

print(final)
    
    