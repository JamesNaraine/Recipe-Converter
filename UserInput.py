from conversion import main_loop
from Translator import Translating


language = "de"


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

preTranslatedOutput = main_loop(True,input_text)
print(Translating(preTranslatedOutput, language))

