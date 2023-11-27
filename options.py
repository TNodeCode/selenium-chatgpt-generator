from chat import Models

# Given a dictionary and a value get the corresponding key that belongs to the value
def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]

# Define the sidebar menu items
menu_items = {
    'Page Objects': 'page_objects',
    'Entity Class': 'entity_class'
}

model_types = {
    Models.GPT35: "GPT 3.5 4k",
    Models.GPT35_16k: "GPT 3.5 16k",
    Models.GPT4: "GPT 4 8k",
    Models.GPT4_32k: "GPT 4 32k",
}