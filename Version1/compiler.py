lines = []

truebool = "ja"
falsebool = "nein"

with open ("Version1\\processed.tl", "r") as f:
    lines = (f.readlines())

def is_float(value):
  if value is None:
      return False
  try:
      float(value)
      return True
  except:
      return False

def get_packages():
    return "import random"

with open ("output.py", "w") as f:
    f.write("# Welcome to the Compiler!\n")
    f.write(f"{get_packages()}\n")

for x in range(len(lines)):
    words = lines[x].split()
    py_input = ""
    variable_declaration = False

    print("Wörter:", words)

    #region Variables
    for y in range(len(words)):
        # Variable declaration?
        if '?' in words[y]:
            variable_declaration = True
            break
    # String variable?
    if variable_declaration:
        is_string = False
        for y in range(len(words)):
            if '\"' in words[y]:
                is_string = True
    # Random integer?
    if variable_declaration:
        random_dice = False
        for y in range(len(words)):
            if '/roll' in words[y]:
                random_dice = True
    
    # region Variable declaration (Number or bool)
    if variable_declaration and len(words) == 2:
        if not is_string:
            variable_name = words[0].replace('?', '')
            variable_value = words[1]
            if type(variable_value) == int or is_float(variable_value):
                py_input = f"{variable_name} = {variable_value}"
            else:
                if variable_value.lower() == truebool:
                    py_input = f"{variable_name} = True"
                else:
                    py_input = f"{variable_name} = False"
    #endregion
    
    # region Variable declaration (String)
    if (variable_declaration and is_string):
        variable_name = words[0].replace('?', '')
        py_input = variable_name
        words.pop(0)
        string_value = ""
        for z in words:
            string_value += z + " "
        # variable_value = [word[1:] for word in words]
        py_input = f"{variable_name} = {string_value}"
    #endregion
    
    # region Variable declaration (random number (roll a dice))
    if (variable_declaration and random_dice):
        variable_name = words[0].replace('?', '')
        roll_index = 0
        dice = ""
        for y in range(len(words)):
            if "/roll" in words[y]:
                roll_index = y
                dice = words[y+1]
                break
        # breaking down roll xdy
        dices = dice.split('d')
        amount_of_dices = dices[0]
        dice = dices[1]

        py_input = f"{variable_name} = "
        if amount_of_dices == "1":
            if dice == "4":
                py_input += f"random.randint(1, 4)"
            if dice == "6":
                py_input += f"random.randint(1, 6)"
            if dice == "8":
                py_input += f"random.randint(1, 8)"
            if dice == "10":
                py_input += f"random.randint(1, 10)"
            if dice == "12":
                py_input += f"random.randint(1, 12)"
            if dice == "20":
                py_input += f"random.randint(1, 20)"
            if dice == "100":
                py_input += f"random.randint(1, 100)"
        else:
            if dice == "4":
                py_input += f"[random.randint(1, 4) for x in range({amount_of_dices})]"
            if dice == "6":
                py_input += f"[random.randint(1, 6) for x in range({amount_of_dices})]"
            if dice == "8":
                py_input += f"[random.randint(1, 8) for x in range({amount_of_dices})]"
            if dice == "10":
                py_input += f"[random.randint(1, 10) for x in range({amount_of_dices})]"
            if dice == "12":
                py_input += f"[random.randint(1, 12) for x in range({amount_of_dices})]"
            if dice == "20":
                py_input += f"[random.randint(1, 20) for x in range({amount_of_dices})]"
            if dice == "100":
                py_input += f"[random.randint(1, 100) for x in range({amount_of_dices})]"
    #endregion


    

        print("Dices:", dices, ", dice:", dice)

    #endregion

    

    # Variable declaration
    # if '?' in words:
    #     print("? insinde!")
    #     for y in range(len(words)):
    #         if '?' in words[y]:
    #             print("? insinde!")
    #             variable_name = x.replace("?", "")
    #         else:
    #             variable_value = words[y]
    #     py_input += f"{variable_name} = {variable_value}"
    # else:
    #     for y in words:
    #         y.replace ("#", "")
    #         py_input += y 
    #     py_input = f"# {py_input}"

    with open ("output.py", "a") as f:
        f.write(py_input + "\n")
