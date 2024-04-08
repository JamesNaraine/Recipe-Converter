
from Dictionary import Imperial_dictionary, Cup_conversion, Metric_dictionary 
from math import trunc

# from Conversion import find_slash, convert_fraction

def convert_fraction(x,y):
    try:
        x = float(x)
        y = float(y)
        return round(x / y, 2)
    except ValueError:
        return "Invalid input"


# print(convert_fraction(1,4))


def find_slash(string):
    index_slash = 0
    x = ""
    y = ""


    if "/" in string:
        parts = string.split("/")  # Split the string into two parts
        return str(convert_fraction(parts[0], parts[1]))
    else:
        return(string)
    

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# print("Imperial_dictionary")
# print(Imperial_dictionary)
# print("Opposite_conversion")
# print(Metric_dictionary)




# print("")
# print("This is the input")
# print("")
# print("")
# print(a)

# int = 1,2 ,3 ,4 ,68

# floats = 4.5,6.7 3.141558985




# print("")
# print("this is the output before the main loop, after the slash conversion")
# print("")
# print(output)




# for key in Oppersite_conversion:
#     unit_info = Oppersite_conversion[key]
#     print(f"{key} : {unit_info['measurement']} : {unit_info['multiplier']}")




# print("")
# print("this is the output before the main loop, after the slash conversion")
# print("")
# print(output)

Reciepe_Imperial = True

def main_loop(Reciepe_Imperial, input_text):
    global Imperial_dictionary
    global Metric_dictionary
    global Cup_conversion

    output = []
    a = []
    target_dictionary = {}
    after_replace =[]
    after_slash = []
    after_is_num =[]   



    input_text = input_text.replace("\n"," # ")
    after_replace = input_text.split(" ")

    print(f"after_replace = {after_replace}")

    for item in after_replace:
        after_slash.append(find_slash(item))

    print(f"after_slash = {after_slash}")

    for i in range(len(after_slash)-1):
        if is_number(after_slash[i]) and i < len(after_slash) - 1 and is_number(after_slash[i+1]):
                # Sum the current and next number if they are both numeric
                x = float(float(after_slash[i]) + float(after_slash[i + 1]))
                after_is_num.append(str(x))
        elif is_number(after_slash[i]) and is_number(after_slash[i-1]):
                # Skip if the previous and current elements are numbers
                pass
        else:
            # Append the current element if it is not a number
            after_is_num.append(after_slash[i])
    after_is_num.append(after_slash[-1])
        


    print(f"after_is_num = {after_is_num}")



    
    after_is_num = [item for item in after_is_num if item != ""]

    a = after_is_num


    if Reciepe_Imperial == True:
        target_dictionary = Imperial_dictionary
    else:
        target_dictionary = Metric_dictionary

    count = 0

    for word in a:
        subcount = 0
        
        count += 1
        item = str(word).lower()
        
        # print(f"current item = {item}")
        previous_value = 0
        # if it is, remove the previous entry to a and convert the value
        if item.lower() in target_dictionary.keys():
            previous_value = float(output[-1])
            # print(f"previous value = {previous_value}")
            output.pop()
            if item.lower() == "cup" or item.lower() == "cups":
                # print(f"Cup Checking {item}")
                # print(f"count number = {count}")
                for i in range(count+1,min(count+5,len(a))):
                    if subcount > 0:
                        break
                    # print(f"Checking {a[i]}")
                    if a[i] in Cup_conversion.keys():
                        output.append(trunc(round(previous_value * float(Cup_conversion[a[i]]["multiplier"]),0)))
                        output.append(Cup_conversion[a[i]]["measurement"])
                        subcount += 1
                        
                        
                if subcount == 0 :
                    output.append(round(previous_value * float(200),3))
                    output.append("g")
                                            
                
            else: 
            
                output.append(round(previous_value * float(target_dictionary[item]["multiplier"]), target_dictionary[item]["round"]))
                output.append(target_dictionary[item]["measurement"])
        else:
            output.append(item)
            # if a isn't in the receipe conversion dictionary pass

    print(f"output ={output}")
    final = ""

    for i in output:
        final += str(i) 
        final += " "
    
    final = final.replace("# ", "\n")

    return final


# print(f"current output= {output}")
    

# print("")
# print("this is the output")
# print("")

# print("this is befopre the replace \n\n")


# print(main(True, "3 lbs of ham"))



# print("\n\n this is after the replace")

# print(final)

# for i in output:
#     print(i)