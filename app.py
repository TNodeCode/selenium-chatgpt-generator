import streamlit as st
import os
from extract import remove_indent_spaces
from options import *
from prompts import *
from chat import let_chatgpt_generate_code, Models
from ui.page_objects import display as display_page_objects_ui
from ui.entity_class import display as display_entity_class_ui

# Set the app title
st.set_page_config(page_title='ChatGPT Page Object Generator')

# Define the sidebar
st.sidebar.title('Menu')
selected_item = st.sidebar.radio('', list(menu_items.keys()))

# Read the selected text file
active_menu_item = menu_items[selected_item]

# Show an error dialogue if API key wasn't found
if not os.getenv("OPENAI_SECRET"):
    st.error("No API key provided. Please provide an API key via the environment variable OPENAI_SECRET.")

if selected_item == 'Page Objects':
    display_page_objects_ui()

if selected_item == 'Entity Class':
    display_entity_class_ui()