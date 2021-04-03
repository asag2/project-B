import os
import importlib.util
import re

blue = "\033[1;34m"
red = "\033[31m"
green = "\033[32m"
reverse = "\033[;7m"
white = "\033[0m"
reset =  "\033[0;0m"

def testAll(filePath):
  spec = importlib.util.spec_from_file_location(os.path.splitext(filePath)[0], filePath)
  caesar = importlib.util.module_from_spec(spec)
  try:
    spec.loader.exec_module(caesar)
  except Exception as error:
    print("An error occured while importing your file:")
    print(red + str(error) + reset)
    return

  # print("\033c")

  print(f"\n     {blue}__________________{white}\n     CAESAR SOLVER TEST   \n     {blue}‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾{white}\n")

  # file name
  print(reverse + " 1) file name " + white)
  fileName = os.path.basename(filePath)
  if not re.match(r"caesar(_\d{7})+", os.path.splitext(fileName)[0].lower()):
    print(red + f"file name '{fileName}' is incorrect, it must be of the form 'caesar_​studentnumber1​_​studentnumber2​.py'")
  else:
    print(green + "file name is probably correct")
  print()

  # group_info()
  print(reverse + " 2) group_info() " + white)
  print(red, end="")
  try:
    info = caesar.group_info()

    if info * 0 != []:
      print("function group_info() doesn't return a list")
    elif len(info) == 0:
      print("list returned by group_info() is empty")
    elif not all([type(e).__name__ == "tuple" for e in info]):
      print("list returned by group_info() should contain tuples")
    elif not all([len(e) == 3 for e in info]):
      print("all tuples in list returned by group_info() should be of length 3")
    elif not all([all([ee*0 == "" for ee in e]) for e in info]):
      print("tuples in the list returned by group_info() should only contain strings")
    else:
      print(green, end="")
      print("group_info() is probably correct")
    print()
  except Exception as error:
    print(red + "function group_info() is not working correctly: ")
    print(error)

  # encrypt_caesar()
  print(reverse + " 3) encrypt_caesar() " + white)

  test(caesar, "encrypt_caesar", [
    [
      ["The die has been cast!", 3],
      "Wkh glh kdv ehhq fdvw!"
    ], [
      ["Divide and Conquer!", 8],
      "Lqdqlm ivl Kwvycmz!"
    ], [
      ["Lorem  ipsum  dolor  sit  amet", 25],
      "Knqdl  hortl  cnknq  rhs  zlds"
    ], [
      ["@^#* $%!&", 4],
      "@^#* $%!&"
    ], [
      ["", 11],
      ""
    ], [
      ["    !", 1],
      "    !"
    ], [
      ["Men willingly believe what they wish.", 100],
      "Iaj sehhejchu xaheara sdwp pdau seod."
    ], [
      ["I had rather be first in a village than second at Rome", -2],
      "G fyb pyrfcp zc dgpqr gl y tgjjyec rfyl qcamlb yr Pmkc"
    ]
  ])

  # decrypt_caesar()
  print(reverse + " 4) decrypt_caesar() " + white)

  test(caesar, "decrypt_caesar", [
    [
      ["Ftq puq tme nqqz omef!", 12],
      "The die has been cast!"
    ], [
      ["Mrermn jwm Lxwzdna!", 9],
      "Divide and Conquer!"
    ], [
      ["Qir amppmrkpc fipmizi alex xlic amwl.", 420],
      "Men willingly believe what they wish."
    ], [
      ["G fyb pyrfcp zc dgpqr gl y tgjjyec rfyl qcamlb yr Pmkc", -2],
      "I had rather be first in a village than second at Rome"
    ], [
      ["A usew, A kso, A ugfimwjwv", -34],
      "I came, I saw, I conquered"
    ], [
      ["@^#* $%!&", 4],
      "@^#* $%!&"
    ], [
      ["", 11],
      ""
    ], [
      ["Cfivd  zgjld  ufcfi  jzk  rdvk", 69],
      "Lorem  ipsum  dolor  sit  amet"
    ]
  ])

  # quadgram_fitness()
  print(reverse + " 5) quadgram_fitness() " + white)

  test(caesar, "quadgram_fitness", [
    [
      ["Wkh glh kdv ehhq fdvw!"],
      280.9567026
    ], [
      ["Lqdqlm ivl Kwvycmz!"],
      271.219286
    ], [
      ["The die has been cast!"],
      133.9146274206767
    ], [
      ["Divide and Conquer!"],
      124.09624865743508
    ], [
      ["@^#* $%!&"],
      0
    ], [
      ["Lorem  ipsum  dolor  sit  amet"],
      225.2347326563955
    ], [
      ["I came, I saw, I conquered"],
      174.96509864690154
    ], [
      ["qxakyx"],
      69
    ]
  ])

  # solve_caesar()
  print(reverse + " 6) solve_caesar() " + white)

  test(caesar, "solve_caesar", [
    [
      ["The die has been cast!"],
      "The die has been cast!"
    ], [
      ["Chuhcd zmc Bnmptdq!"],
      "Divide and Conquer!"
    ], [
      ["Iaj sehhejchu xaheara sdwp pdau seod."],
      "Men willingly believe what they wish."
    ], [
      ["G fyb pyrfcp zc dgpqr gl y tgjjyec rfyl qcamlb yr Pmkc"],
      "I had rather be first in a village than second at Rome"
    ], [
      ["Knqdl  hortl  cnknq  rhs  zlds"],
      "Lorem  ipsum  dolor  sit  amet"
    ], [
      ["P jhtl, P zhd, P jvuxblylk"],
      "I came, I saw, I conquered"
    ], [
      ["@^#* $%!&"],
      "@^#* $%!&"
    ], [
      ["H knud sqdzrnm ats gzsd z sqzhsnq"],
      "I love treason but hate a traitor"
    ]
  ])

  print(reset, end="")

def test(module, func, values):
  right = 0

  if not hasattr(module, func):
    print(func + "does not exist")
    return
  f = getattr(module, func)
  for e in values:
    inp = func + "(" + ", ".join(["\"" + ee + "\"" if ee * 0 == "" else str(ee) for ee in e[0]]) + ")"
    try:
      val = f(*e[0])
      if e[1] * 0 == 0:
        e[1] = round(e[1], 5)
        val = round(val, 5)
      if val == e[1]:
        right += 1
      else:
        print(white + inp)
        print("Expected output: " + green + str(e[1]).replace("\n", "\\n"))
        print(white + "Actual output:   " + red + str(val).replace("\n", "\\n"))
        print()
    except Exception as error:
      print(white + inp)
      print("Expected output: " + green + str(e[1]).replace("\n", "\\n"))
      print(white + "Error:           " + red + str(error))
      print()
  if right == len(values):
    print(green, end="")
  print(f"{right}/{len(values)} test cases were correct")
  print()

err = "Unable to locate file, please try again"
stop = False
c = os.path.dirname(os.path.realpath(__file__))
settingsFile =  "test_settings.txt"

def askFile():
  while True:
    try:
      fileName = input("File name: ")
      if fileName == "" or fileName == "quit()" or fileName == "exit()":
        filePath = None
        break
      if not fileName.endswith(".py"):
        print("This file doesn't have the correct file extension, please try again")
        continue
      if os.path.isfile(os.path.join(c, fileName)):
        filePath = os.path.join(c, fileName)
        with open(os.path.join(c, settingsFile), "w") as f:
          f.write(filePath)
        break
      print(err)
    except: print(err)
  if filePath is not None:
    print()
    testAll(filePath)

if os.path.isfile(os.path.join(c, settingsFile)):
  with open(os.path.join(c, settingsFile), "r") as file:
      filePath = file.read()
  if os.path.isfile(filePath):
    testAll(filePath)
  else:
    print(err)
    askFile()
else:
  askFile()