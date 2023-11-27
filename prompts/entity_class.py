default_prompt = """
I need a $LANG $FRAMEWORK entity class for the following $DATATYPE code.
The code should have the following style:
- create getters and setters for all class attributes
- all attributes and methods commented with $COMMENT_STYLE.
"""

def prepare_prompt(prompt, additional_prompt, data, framework, lang, datatype, comment_style):
    prompt = prompt.replace("$LANG", lang)
    prompt = prompt.replace("$COMMENT_STYLE", comment_style)
    prompt = prompt.replace("$DATATYPE", datatype)
    prompt = prompt.replace("$FRAMEWORK", framework)
    prompt += "\n" + additional_prompt
    if lang == 'Java':
        prompt += "Use Lombok for the getters and setters. Also use the builder annotation and the NoArgsConstructor from Lombok.\n"
    prompt += "\nI need no explanations, only the code."
    prompt += "\n\n" + data
    return prompt

def build_default_prompt(additional_prompt, data, datatype, framework, lang, comment_style):
    return prepare_prompt(
        prompt=default_prompt,
        additional_prompt=additional_prompt,
        data=data,
        datatype=datatype,
        framework=framework,
        lang=lang,
        comment_style=comment_style
    )
