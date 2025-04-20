lines = []

with open("README.md", "r") as file:
    is_first_non_table = True

    for line in file:
        line = line.strip()
        if not line or line[0] in "#| " or line.startswith("Что есть в хакспейсе"):
            lines.append(line)
            is_first_non_table = True
        else:
            if is_first_non_table:
                is_first_non_table = False
                lines.append("| Item | Qty | Owner | Notes |")
                lines.append("|------|-----|-------|-------|")
            
            lines.append("| " + line[0].upper() + line[1:] + " ||||")

with open("README.md", "w") as file:
    file.write("\n".join(lines))