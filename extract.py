def extract_code(text):
    lines = text.split("\n")
    code = ""
    line_contains_code = False

    for l in lines:
        if l[0:3] == "```":
            if not line_contains_code:
                line_contains_code = True
            else:
                line_contains_code = False
            continue
        if line_contains_code:
            code += l
            code += "\n"
    return code
