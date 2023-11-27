import streamlit as st
import os
from extract import remove_indent_spaces
from prompts.entity_class import *
from options import *
from chat import let_chatgpt_generate_code, Models

# Methods for building prompts based on the chosen page object type
handlers = {
    'entity_class': build_default_prompt,
}

# Available comment styles
comment_styles = {
    'Java': 'JavaDoc',
    'Kotlin': 'JavaDoc',
    'Groovy': 'JavaDoc',
    'Python': 'numpydoc',
    'JavaScript': 'JSDoc',
    'TypeScript': 'JSDoc',
}


def display():
    # Define the text input field and submit button
    st.markdown("# ChatGPT Entity Code Generator")

    # Show a selectbox where the user can select a language
    lang = st.selectbox('Language', ('Java', 'Kotlin', 'Groovy', 'Python', 'JavaScript', 'TypeScript'))

    # Show a selectbox where the user can select a language
    framework = st.selectbox('Framework', ('', 'Hibernate ORM', 'Sequelize ORM', 'SQLAlchemy ORM'))

    # Show a selectbox where the user can select a language
    datatype = st.selectbox('Data type', ('HTML', 'JSON', 'TEXT'))

    # Input textarea for HTML code
    data = st.text_area('Enter data:')

    # Text field for addiitonal prompt that the user wants to submit
    additional_promt = st.text_area('Enter features that the entity class should have:')

    # Show a select box for the available models
    model_type = st.selectbox('Model Type', model_types.values())

    # Get the model that was selected by the user
    selected_model = get_keys_from_value(model_types, model_type)[0]

    # SUbmit button
    submit_button = st.button('Submit')

    # Display the success message if the submit button is clicked
    if submit_button:
        data = remove_indent_spaces(data)

        prompt = handlers['entity_class'](
            data=data,
            datatype=datatype,
            framework=framework,
            additional_prompt=additional_promt,
            lang=lang,
            comment_style=comment_styles[lang]
        )

        st.markdown('##### Prompt')
        st.code(prompt)
        st.info('Generating code ...')
        generated_code = let_chatgpt_generate_code(prompt=prompt, model=selected_model)
        st.code(
            generated_code,
            language=lang.lower(),
            line_numbers=True
        )
