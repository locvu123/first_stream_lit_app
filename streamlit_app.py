import streamlit
streamlit.title('My Mum\'s New Healthy diners')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Bluebery')
streamlit.text('🥗 Spinach & Kale')
streamlit.text('🐔 Hard boiled egg - free range')
streamlit.text('🥑🍞 Avocado & Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# new section to display api response
streamlit.header("Fruityvice Fruit Advice!")

# New section
import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
