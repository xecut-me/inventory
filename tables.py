header = ["Item", "Qty", "Owner", "Notes"]
size = [70, 3, 20, 10]
spacer = "|" + "|".join("-" * (s + 2) for s in size) + "|"

def format(line):
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