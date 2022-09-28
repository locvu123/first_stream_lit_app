import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Mum\'s New Healthy diners')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Bluebery')
streamlit.text('🥗 Spinach & Kale')
streamlit.text('🐔 Hard boiled egg - free range')
streamlit.text('🥑🍞 Avocado & Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import pandas
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
# import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# streamlit.text(fruityvice_response.json())

 # try:
fruit_choice = streamlit.text_input('What fruit would you like information about?')
# if not fruit_choice :
streamlit.error("Please select a FRUIT to get information.")
 else:
 # streamlit.write('The user entered ', fruit_choice)

  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# write your own comment -what does the next line do? 
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
  streamlit.dataframe(fruityvice_normalized)
  
 # except URLError as e:
 #   streamlit.error()



streamlit.stop()
# import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# add_my_fruit = my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('papaya from streamit') ")
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
# my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
# streamlit.text("Hello from Snowflake:")
streamlit.text("The fruit load list contains followings:")
# streamlit.text(my_data_row)
# streamlit.dataframe(my_data_row)
streamlit.dataframe(my_data_rows)
