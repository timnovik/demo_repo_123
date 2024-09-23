logs = open("logs/log.txt", "a")
for i in range(int(input())):
    name = input()
    print(f"hello {name}!")
    print(name, file=logs)
logs.close()
