lines = []

truebool = "ja"
falsebool = "nein"

isinloop = False

with open ("Version2\\processed.tl", "r") as f:
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

with open ("Version2\\output.py", "w") as f:
    f.write("# Welcome to the Compiler!\n")
    f.write(f"{get_packages()}\n")

for x in range(len(lines)):
    words = lines[x].split()
    py_input = ""
    variable_declaration = False

    print("Wörter:", words)

    # Is the current statement in a loop
    if isinloop:
        py_input += "\t"

    #region Variables
    for y in range(len(words)):
        # Variable declaration?
        if '?' in words[0]:
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
                py_input += f"{variable_name} = {variable_value}"
            else:
                if variable_value.lower() == truebool:
                    py_input += f"{variable_name} = True"
                else:
                    py_input += f"{variable_name} = False"
    #endregion
    
    # region Variable declaration (String)
    if (variable_declaration and is_string):
        variable_name = words[0].replace('?', '')
        # py_input += variable_name
        words.pop(0)
        string_value = ""
        for z in words:
            string_value += z + " "
        # variable_value = [word[1:] for word in words]
        py_input += f"{variable_name} = {string_value}"
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
        # breaking down /roll xdy
        dices = dice.split('d')
        amount_of_dices = dices[0]
        dice = dices[1]

        py_input += f"{variable_name} = "
        if amount_of_dices == "1":
            if dice == "4":
                py_input += f"random.randint(1, 4)"
            elif dice == "6":
                py_input += f"random.randint(1, 6)"
            elif dice == "8":
                py_input += f"random.randint(1, 8)"
            elif dice == "10":
                py_input += f"random.randint(1, 10)"
            elif dice == "12":
                py_input += f"random.randint(1, 12)"
            elif dice == "20":
                py_input += f"random.randint(1, 20)"
            elif dice == "100":
                py_input += f"random.randint(1, 100)"
            else:
                py_input += "0"
        else:
            if dice == "4":
                py_input += f"[random.randint(1, 4) for x in range({amount_of_dices})]"
            elif dice == "6":
                py_input += f"[random.randint(1, 6) for x in range({amount_of_dices})]"
            elif dice == "8":
                py_input += f"[random.randint(1, 8) for x in range({amount_of_dices})]"
            elif dice == "10":
                py_input += f"[random.randint(1, 10) for x in range({amount_of_dices})]"
            elif dice == "12":
                py_input += f"[random.randint(1, 12) for x in range({amount_of_dices})]"
            elif dice == "20":
                py_input += f"[random.randint(1, 20) for x in range({amount_of_dices})]"
            elif dice == "100":
                py_input += f"[random.randint(1, 100) for x in range({amount_of_dices})]"
            else:
                py_input += f"[0 for x in range({amount_of_dices})]"
    #endregion


    

        print("Dices:", dices, ", dice:", dice)

    #endregion

    #region printing out 
    if len(words) > 0 and words[0] == "rede":
        print_content = ""
        for y in range(1, len(words)):
            print_content += words[y]
            # Add Space but not at the end - formatting perfection skill issue
            if (y < len(words) - 1):
                print_content += " "
        py_input += f"print({print_content})"
    #endregion
    
    #region Schere
    if len(words) == 1:
        if words[0].lower() == "schere":
            py_input += "print(\"Schere\")"
    #endregion

    #region begin a Loop (under construction)
    if len(words) > 0 and words[0] == "Crashout":
        if len(words) == 2:
            if (words[1].isdigit()):
                amount = words[1]
                py_input += f"for x in range({amount}):"
                isinloop = True
    #endregion

    #region end a Loop
    if len(words) == 1:
        if words[0].lower() == "sybau":
            isinloop = False
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

    with open ("Version2\\output.py", "a") as f:
        f.write(py_input + "\n")
