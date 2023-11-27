import streamlit as st
import os
from extract import remove_indent_spaces
from prompts.page_objects import *
from options import *
from chat import let_chatgpt_generate_code, Models

# Available page object types
page_object_types = {
    'page_objects': 'Default Page Object',
    'alerts': 'Alert',
    'cards': 'Card',
    'dropdowns': 'Dropdown',
    'forms': 'Form',
    'menus': 'Menu',
    'modals': 'Modal',
    'paginations': 'Pagination',
    'tables': 'Table',
}

# Methods for building prompts based on the chosen page object type
handlers = {
    'page_objects': build_default_prompt,
    'alerts': build_alert_prompt,
    'cards': build_card_prompt,
    'dropdowns': build_dropdown_prompt,
    'forms': build_form_prompt,
    'menus': build_menu_prompt,
    'modals': build_modal_prompt,
    'paginations': build_pagination_prompt,
    'tables': build_table_prompt,
}

def display():
    # Define the text input field and submit button
    st.markdown("# ChatGPT Selenium Page Object Code Generator")

    # Show a selectbox where the user can select a language
    lang = st.selectbox('Language', ('Java', 'Kotlin', 'Groovy', 'Python', 'JavaScript', 'TypeScript'))

    # Show a select box for the available models
    model_type = st.selectbox('Model Type', model_types.values())

    # Show a select box where the user can select a page object type
    page_object_type = st.selectbox('Page Object Type', page_object_types.values())

    # Get the model that was selected by the user
    selected_model = get_keys_from_value(model_types, model_type)[0]

    # Get the page object type that was selected by the user
    selected_page_object_type = get_keys_from_value(page_object_types, page_object_type)[0]

    # Available comment styles
    comment_styles = {
        'Java': 'JavaDoc',
        'Python': 'numpydoc',
        'JavaScript': 'JSDoc',
    }

    # Input textarea for HTML code
    html_code = st.text_area('Enter HTML code:')

    # Text field for addiitonal prompt that the user wants to submit
    additional_promt = st.text_area('Enter features that the page object class should have:')

    # SUbmit button
    submit_button = st.button('Submit')


    # Display the success message if the submit button is clicked
    if submit_button:
        html_code = remove_indent_spaces(html_code)

        prompt = handlers[selected_page_object_type](
            code=html_code,
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