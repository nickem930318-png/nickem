try:
    with open("1.txt", "r") as file:
        content = file.read()
        print(content)
except Exception as e:
    print("Ett oväntat fel uppstod: ", e)