default_prompt = """
    I need a $LANG selenium page object class for the following HTML code.
    The class should have no WebElement attributes.
    All selectors should be stored in class attributes as By instances.
    All methods should be commented with $COMMENT_STYLE.
    """

form_prompt = default_prompt + """
    For all input text fields I need methods for getting their current value, methods for clearing their value and methods for entering a value.
    For all checkboxes I need methods for checking if they are checked, and for checking and unchecking them.
    For all selects and radios I need methods for getting the available options as a list of strings, a method for selecting an option and a method for getting the current value.
    There should be a method for clearing the complete form and a method for submitting the form.
    """

menu_prompt = default_prompt + """
    I need a method that extracts all menu item texts as a list of strings.
    For each menu item I need a method that clicks on it.
    I need a method that gets the menu item text of the currently active menu item.
"""


def prepare_prompt(prompt, additional_prompt, lang, code, comment_style):
    prompt = prompt.replace("$LANG", lang)
    prompt = prompt.replace("$COMMENT_STYLE", comment_style)
    prompt += "\n" + additional_prompt
    prompt += "\nI need no explanations, only the code."
    prompt += "\n" + code
    return prompt


def build_default_prompt(additional_prompt, code, lang, comment_style):
    return prepare_prompt(
        prompt=default_prompt,
        additional_prompt=additional_prompt,
        code=code,
        lang=lang,
        comment_style=comment_style
    )


def build_form_prompt(additional_prompt, code, lang, comment_style):
    return prepare_prompt(
        prompt=form_prompt,
        additional_prompt=additional_prompt,
        code=code,
        lang=lang,
        comment_style=comment_style
    )


def build_menu_prompt(additional_prompt, code, lang, comment_style):
    return prepare_prompt(
        prompt=menu_prompt,
        additional_prompt=additional_prompt,
        code=code,
        lang=lang,
        comment_style=comment_style
    )
