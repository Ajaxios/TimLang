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


with open ("output.py", "w") as f:
    f.write("# Welcome to the Compiler!\n")

for x in range(len(lines)):
    words = lines[x].split()
    py_input = ""
    variable_declaration = False

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
    
    # Variable declaration (Number or bool)
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
    
    # Variable declaration (String)
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

    # random number (roll a dice)


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
