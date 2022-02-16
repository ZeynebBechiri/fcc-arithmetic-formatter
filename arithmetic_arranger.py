def arithmetic_arranger(problems, *args):

  if (len(problems) > 5):
    return ("Error: Too many problems.")

  pb = list()
  for problem in problems:
    pb.append(problem.split())
  

  numbers = list()
  operators = list()
  for p in pb:
    numbers.append(p[0])
    numbers.append(p[2])
    operators.append(p[1])
  

  for i in numbers:
    if (not (i.isdigit())):
      return ("Error: Numbers must only contain digits.")
    elif ((len(i) > 4)):
      return ("Error: Numbers cannot be more than four digits.")
  
  for j in operators:
    if (j not in ['+','-']):
      return ("Error: Operator must be '+' or '-'.")

  arranged_problems = ""
  dash_row = ""
  fst_row = ""
  snd_row = ""
  solutions = ""

  for p in pb:
    maxlen = max(len(p[0]),len(p[2]))

    fst_row += f"{p[0].rjust(maxlen+2)}    "
    snd_row += f"{p[1]} {p[2].rjust(maxlen )}    "
    dash_row += f"--{'-' * (maxlen)}    "
    if (p[1] == '+'):
      solutions += f"{str(int(p[0]) + int(p[2])).rjust(maxlen + 2)}    "
    else:
      solutions += f"{str(int(p[0]) - int(p[2])).rjust(maxlen +2)}    "


  fst_row = fst_row.rstrip()
  snd_row = snd_row.rstrip()
  dash_row = dash_row.rstrip()
  solutions = solutions.rstrip()

  if (args):
    arranged_problems += fst_row + "\n" + snd_row + "\n" + dash_row + "\n" + solutions
  else:
    arranged_problems += fst_row + "\n" + snd_row + "\n" + dash_row

  arranged_problems = arranged_problems.rstrip("\n")
  return arranged_problems