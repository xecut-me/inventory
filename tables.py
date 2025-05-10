header = ["Item", "Qty", "Owner", "Notes"]
size = [70, 3, 20, 10]
spacer = "|" + "|".join("-" * (s + 2) for s in size) + "|"

def format(line):
    line = list(line)
    line[0] = line[0][0].upper() + line[0][1:]
    line[1] = "1" if line[1] == "" else line[1]
    return "| " + " | ".join([h.ljust(s) for s, h in zip(size, line)]) + " |"

lines = []

with open("README.md", "r") as file:
    for line in file:
        line = line.strip()

        if line.startswith("|-"):
            line = spacer
        elif line.startswith("| Item "):
            line = format(header)
        elif line.startswith("|"):
            line = format(e.strip() for e in line.split("|")[1:-1])
        
        lines.append(line)

with open("README.md", "w") as file:
    file.write("\n".join(lines))