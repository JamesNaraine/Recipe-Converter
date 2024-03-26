
Conversion_dictionary = {
"1/4 cup"  :  "60 mL",
"1/3 cup" : "70 mL",
"1/2 cup" : "125 mL",
"2/3 cup" : "150 mL",
"3/4 cup" : "175 mL",
"1 cup" : "250 mL",
"1 1/2 cups" : "375 mL",
"2 cups" : "500 mL",
"4 cups" : "1 liter",
"25 ml" : "1 fl oz",
"50 ml" : "2 fl oz",
"75 ml" : "2 1/2 fl oz",
"100 ml" : "3 1/2 fl oz",
"125 ml" : "4 fl oz",
"150 ml" : "5 fl oz",
"175 ml" : "6 fl oz",
"200 ml" : "7 fl oz",
"225 ml" : "8 fl oz",
"250 ml" : "9 fl oz",
"300 ml" : "10 fl oz",
"350 ml" : "12 fl oz",
"400 ml" : "14 fl oz",
"425 ml" : "15 fl oz",
"450 ml" : "16 fl oz",
"500 ml" : "18 fl oz",
"600 ml" : "1 pint",
"700 ml" : "1 1/4 pints",
"850 ml" : "1 1/2 pints",
"1 litre" : "1 3/4 pints",
"1.5 litres" : "2 3/4 pints",
"2 litres" : "3 1/2 pints",
"2.5 litres" : "4 1/2 pints",
"3 litres" : "5 1/4 pints",
"110 C" : "225 F",
"120 C" : "250 F",
"140 C" : "275 F",
"150 C" : "300 F",
"160 C" : "320 F",
"170 C" : "340 F",
"180 C" : "350 F",
"190 C" : "375 F",
"200 C" : "400 F",
"220 C" : "425 F",
"230 C" : "450 F",
"15 grams" : "1/2 oz",
"25 grams" : "1 oz",
"40 grams" : "1 1/2 oz",
"55 grams" : "2 oz",
"70 grams" : "2 1/2 oz",
"85 grams" : "3 oz",
"100 grams" : "3 1/2 oz",
"115 grams" : "4 oz",
"125 grams" : "4 1/2 oz",
"140 grams" : "5 oz",
"150 grams" : "5 1/2 oz",
"175 grams" : "6 oz",
"200 grams" : "7 oz",
"225 grams" : "8 oz",
"250 grams" : "9 oz",
"280 grams" : "10 oz",
"315 grams" : "11 oz",
"350 grams" : "12 oz",
"375 grams" : "13 oz",
"400 grams" : "14 oz",
"425 grams" : "15 oz",
"450 grams" : "1 lb",
"500 grams" : "1 lb 2 oz",
"600 grams" : "1 lb 5 oz",
"700 grams" : "1 lb 9 oz",
"800 grams" : "1 lb 12 oz",
"900 grams" : "2 lbs",
"1 kg" : "2 lbs 4 oz",
"1 teaspoon": "5 mL",
"2 teaspoons": "10 mL",
"3 teaspoons": "15 mL", 
"4 teaspoons": "20 mL",
"5 teaspoons": "25 mL",
"6 teaspoons": "30 mL",
"1 tablespoon": "15 mL",
"1 tablespoon": "15 mL",
"2 tablespoons": "30 mL",
"3 tablespoons": "45 mL",
"4 tablespoons": "60 mL",  # Equivalent to 1/4 cup
"5 tablespoons": "75 mL",
"6 tablespoons": "90 mL",
"7 tablespoons": "105 mL",
"8 tablespoons": "120 mL",
}


print(Conversion_dictionary["1/4 cup"])

test_text = """1/4 cup soft white breadcrumbs
2 teaspoons Worcestershire sauce
1 tablespoon water
1 tablespoon milk
1 teaspoon seasoned salt
1 teaspoon onion powder
1/2 teaspoon freshly ground black pepper
1 1/4 pounds ground beef
4 sandwich buns, split and toasted"""


def Convert(input_text):

    split_lines = input_text.splitlines()
    split_text = ""


   

    return_text = ""
    i = 0


    converted_text = ""

    for line in split_lines:
        split_text = line.split(" ")
        i = 0
        converted_line = ""
        while i < len(split_text):
            # Check if the current and next word form a key in the dictionary
            if i < len(split_text) - 1 and " ".join(split_text[i:i+2]) in Conversion_dictionary:
                # Add the conversion to converted_line
                converted_line += Conversion_dictionary[" ".join(split_text[i:i+2])] + " "
                i += 2  # Skip the next word as it's part of the current measurement
            else:
                # If no conversion, add the word as is
                converted_line += split_text[i] + " "
                i += 1
        converted_text += converted_line + "\n"
    return converted_text

print(Convert(test_text))