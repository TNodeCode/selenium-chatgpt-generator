import streamlit as st
import os
import time
from extract import extract_code
from prompts import *
from chat import let_chatgpt_generate_code


def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]


# Define the sidebar menu items
menu_items = {
    'Page Objects': 'page_objects',
}

page_object_types = {
    'page_objects': 'Default Page Object',
    'forms': 'Form Page Object',
    'menus': 'Menu Page Object',
}

handlers = {
    'page_objects': build_default_prompt,
    'forms': build_form_prompt,
    'menus': build_menu_prompt,
}

# Set the app title
st.set_page_config(page_title='ChatGPT Page Object Generator')

# Define the sidebar
st.sidebar.title('Menu')
selected_item = st.sidebar.radio('', list(menu_items.keys()))

# Read the selected text file
active_menu_item = menu_items[selected_item]

# Define the text input field and submit button
st.markdown("# ChatGPT Selenium Page Object Code Generator")

if not os.getenv("OPENAPI_SECRET"):
    st.error(
        "No API key provided. Please provide an API key via the environment variable OPENAPI_SECRET.")

lang = st.selectbox(
    'Language',
    ('Java', 'Python', 'JavaScript')
)

page_object_type = st.selectbox(
    'Page Object Type',
    page_object_types.values()
)

selected_page_object_type = get_keys_from_value(
    page_object_types, page_object_type)[0]

comment_styles = {
    'Java': 'JavaDoc',
    'Python': 'numpydoc',
    'JavaScript': 'JSDoc',
}

html_code = st.text_area('Enter HTML code:')

additional_promt = st.text_area(
    'Enter features that the page object class should have:')

submit_button = st.button('Submit')


# Display the success message if the submit button is clicked
if submit_button:
    promt = handlers[selected_page_object_type](
        code=html_code,
        additional_prompt=additional_promt,
        lang=lang,
        comment_style=comment_styles[lang]
    )
    st.info('Generating code ...')
    generated_code = let_chatgpt_generate_code(prompt=promt)
    st.code(
        generated_code,
        language=lang.lower(),
        line_numbers=True
    )
