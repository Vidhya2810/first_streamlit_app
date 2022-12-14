import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#2
#import pandas

#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")                
#3
#streamlit.dataframe(my_fruit_list)            

#4
# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page.
#streamlit.dataframe(my_fruit_list) 

#5
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")                
my_fruit_list = my_fruit_list.set_index('Fruit')        
# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index) ##6 down
#--streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# Display the table on the page.
#--streamlit.dataframe(my_fruit_list) 

#6
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#streamlit.dataframe(my_fruit_list)

#7
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show) 

#8
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)

#9
##
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +this_fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")

#10
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json())

#11
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalized)

#12
#old
#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalized)
#new
#adding same using nested if-else
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
    #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    #streamlit.dataframe(fruityvice_normalized)
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()

 
#streamlit.stop()

#13
import snowflake.connector
#14
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)

#15
#old
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)

#new
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        return my_cur.fetchall()

if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)
#16
#old
#add_my_fruit = streamlit.text_input('What fruit would you like to add?')
#streamlit.write('Thanks for adding ', add_my_fruit)

#17
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")

#new
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')")
        return "Thanks for adding " + new_fruit
   
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)

#18
if streamlit.button('Get Fruit List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   my_cnx.close()
   streamlit.dataframe(my_data_rows)
