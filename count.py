with open("README.md", "r") as file:
    items = [l.split("|")[1] for l in file.readlines() if l.startswith("| ") and not l.startswith("| Item ")]

# print("\n".join(items))

print(len(set(items)))