
output = ['0.8', 'lbs', 'of', 'meat', '#', '1', 'pint', 'of', 'beer', '#', '0.25', 'cup', 'plain', 'yogurt', '#', '2', 'Tbsp.', 'unsalted', 'butter', '(melted)', '#', '2', 'Tbsp.', 'pure', 'maple', 'syrup', '#', '0.5', 'tsp.', 'pure', 'vanilla', 'extract', '#', '1', '0.5', 'cups', 'blanched', 'almond', 'flour', '#', '0.5', 'tsp.', 'baking', 'soda', '#', '0.25', 'tsp.', 'sea', 'salt', '#', '2', 'eggs', '#', '1', 'egg', 'whites', '#', '0.33', 'cup', 'berries']


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

for i in output:
    print(is_number(i))

a = []

for i in range(len(output)-1):
    if is_number(output[i]) and i < len(output) - 1 and is_number(output[i+1]):
            # Sum the current and next number if they are both numeric
            x = float(float(output[i]) + float(output[i + 1]))
            a.append(str(x))
    elif is_number(output[i]) and is_number(output[i-1]):
            # Skip if the previous and current elements are numbers
            pass
    else:
        # Append the current element if it is not a number
        a.append(output[i])
    
    
print(a)
