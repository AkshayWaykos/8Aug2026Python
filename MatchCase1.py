print("============Match Case ==================")
print("MC means match the condition with multiple case,it use when multiple option are there to match with single case")

fruit = "AAAA"

match fruit:
    case "apple":
         print("Fruit Match with demanded fruit = :", fruit)
    case "mango":
         print("Fruit Match with demanded fruit = :", fruit)
    case "Banana":
         print("Fruit Match with demanded fruit = :", fruit)
    case _:
        print("Fruit Not Match with demanded fruit")