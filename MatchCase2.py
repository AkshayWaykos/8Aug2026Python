from unittest import case

print("==============Match Case Program=================")

Day=3

match 9:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
       print("Friday")
    case _:
        print("Wrong Day Number")
print("==============Match Case Program=================")

username = "WXYZ"
match username:
    case "ABCD":
        print("Match with Name", username)
    case "SSSS":
          print("Match with Name", username)
    case "WXYZ":
        print("Match with Name", username)
    case _:
        print("Not Match with UserName")