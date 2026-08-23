
print("==if its Even no then system will display his Square ==============")
print("==if its Odd no then system will display his Cube ==============")

print("=======In normal loop=========")
for i in range(1, 10):
    if i % 2 == 0:  # even hai
        result = i * 2  # square
        print(f"{i} is Even, Square = {result}")
    else:  # odd hai
        result = i ** 3  # cube
        print(f"{i} is Odd, Cube = {result}")

print("========List Comprehension wale style me========")

result = [i**2 if i % 2 == 0 else i**3 for i in range(1, 10)]
print(result)