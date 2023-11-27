default_prompt = """
I need a $LANG selenium page object class for the following HTML code.
The code should have the following style:
- no WebElement objects stored as class attributes
- no static methods
- all selectores stored in By class attributes.
- all attributes and methods commented with $COMMENT_STYLE.
Create the following methods:
"""

form_prompt = default_prompt + """
For all input and hidden fields:
- get current value
- clear value
- type value
- check if disabled
For all checkboxes:
- checking if checked, unchecking
For all selects and radios:
- get available options as list of strings
- select i-th option
- select option by its text
- get currently selected value
For form:
- clear complete form
- submit form.
"""

menu_prompt = default_prompt + """
- count number of menu items
- extract all menu item texts as a list of strings.
- get WebElement of i-th menu item
- for each menu item a method that clicks on it.
- method that gets the menu item text of the currently active menu item.
"""

card_prompt = default_prompt + """
If there are buttons for each button there should be a method for cicking on the button and one for extracting its text.
If there are image there should be a method for each image extracting its source and one for its 'alt' attribute.
If there are links there should be a method for extracting clicking on that link, extracting the text of the link and getting the href attribute of the link.
Also there should be a methods for getting all links, all buttons and all images as a list of WebElement objects.
For each text of the card there should be a method that returns that text.
"""

table_prompt = default_prompt + """
Create the following methods:
- get all header columns
- accept two integers "i" and "j" and return the WebElement of the j-th column in the i-th row
- return a list of all row WebElement objects
- count the rows
- get all columns for i-th row
- get all cells of j-th column
- if table is small one method per cell for extracting its text
"""

pagination_prompt = default_prompt + """
- get webelement of previous
- click on previous
- get webelement of next
- click on next
- get webelement of active
- click on active
- get text of active
"""

dropdown_prompt = default_prompt + """
- getter, click dropdown button
- get available options as list of strings, as list of WebElement
- click on i-th option
- click on option by text
"""

alert_prompt = default_prompt + """
- get alert text
- check if alert is of type primary, secondary, sucess, danger, warning, info
- click close button if exists
"""

modal_prompt = default_prompt + """
- get webelement of text
- get text of text
- get webelement of title
- get text of title
- get webelement of body
- get webelement of footer
- click close button if exists
- for all buttons methods for getting webelement
"""


def prepare_prompt(prompt, additional_prompt, lang, code, comment_style):
    prompt = prompt.replace("$LANG", lang)
    prompt = prompt.replace("$COMMENT_STYLE", comment_style)
    prompt += "\n" + additional_prompt
    if lang == 'Java':
        prompt += "Use the Selenide framework for the selectors.\n"
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


def build_card_prompt(additional_prompt, code, lang, comment_style):
    return prepare_prompt(
        prompt=card_prompt,
        additional_prompt=additional_prompt,
        code=code,
        lang=lang,
        comment_style=comment_style
    )


def build_table_prompt(additional_prompt, code, lang, comment_style):
    return prepare_prompt(
        prompt=table_prompt,
        additional_prompt=additional_prompt,
        code=code,
        lang=lang,
        comment_style=comment_style
    )


def build_pagination_prompt(additional_prompt, code, lang, comment_style):
    return prepare_prompt(
        prompt=pagination_prompt,
        additional_prompt=additional_prompt,
        code=code,
        lang=lang,
        comment_style=comment_style
    )


def build_dropdown_prompt(additional_prompt, code, lang, comment_style):
    return prepare_prompt(
        prompt=dropdown_prompt,
        additional_prompt=additional_prompt,
        code=code,
        lang=lang,
        comment_style=comment_style
    )


def build_alert_prompt(additional_prompt, code, lang, comment_style):
    return prepare_prompt(
        prompt=alert_prompt,
        additional_prompt=additional_prompt,
        code=code,
        lang=lang,
        comment_style=comment_style
    )


def build_modal_prompt(additional_prompt, code, lang, comment_style):
    return prepare_prompt(
        prompt=modal_prompt,
        additional_prompt=additional_prompt,
        code=code,
        lang=lang,
        comment_style=comment_style
    )
