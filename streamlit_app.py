import streamlit

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
import pandas
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
import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)

#9
streamlit.header("Fruityvice Fruit Advice!")

#10
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json())

#11
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalized)

#12
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

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
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
