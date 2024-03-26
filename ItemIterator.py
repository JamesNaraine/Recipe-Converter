input_text = """4/5 lbs of meat"""

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
    }
}



print("")
print("this is the output before the main loop, after the slash conversion")
print("")
print(output)



for item in a:
    print(f"current item = {item}")
    previous_value = 0
    # if it is, remove the previous entry to a and convert the value
    if item in Reciepe_conversion.keys():
        previous_value = float(output[-1])
        print(f"previous value = {previous_value}")
        output.pop()
        output.append(round(previous_value * float(Reciepe_conversion[item]["multiplier"]),3))
        output.append(Reciepe_conversion[item]["measurement"])
    else:
        output.append(item)
        # if a isn't in the receipe conversion dictionary pass
    print(f"current output= {output}")

print("")
print("this is the output")
print("")
print(output)
    
    