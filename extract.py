from bs4 import BeautifulSoup


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


def remove_indent_spaces(html_content):
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Get the formatted HTML without indents and spaces
    formatted_html = soup.prettify(formatter=None)

    return formatted_html
