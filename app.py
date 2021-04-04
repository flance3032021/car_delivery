import streamlit as st
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
geolocator = Nominatim(user_agent="car_price")
st.set_page_config(page_title= 'Car Delivery Price Calculation Project', initial_sidebar_state = 'auto')
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

total_price= 0

transport_type= st.selectbox('Select type of transport : ', ('Private Dyna','Dyna/bed/Dyna','Lowbed','Luxury','Motocycle'))

insurance= st.checkbox('I need insurance.')
  
if transport_type in ['Private Dyna','Luxury','Motocycle']:
  if insurance:
    price_per_km= 1.7
  else:
    price_per_km= 1
else:
  price_per_km= 0.85

col1, col2= st.beta_columns(2)
time1= col1.time_input('Order time : ')
date1= col1.date_input('Order date : ')
place1= col1.text_input('Order location : ')
time2= col2.time_input('Pickup time : ')
date2= col2.date_input('Pickup date : ')
days= (date2-date1).days
place2= col2.text_input('Pickup location : ')

try:
  loc1= geolocator.geocode(place1)
  loc2= geolocator.geocode(place2)
  lat_lon1= (loc1.latitude, loc1.longitude)
  lat_lon2= (loc2.latitude, loc2.longitude)
  distt= geodesic(lat_lon1, lat_lon2).kilometers
  st.write(f'The distance is {round(distt, 2)} kilometres.')

  if transport_type=='Private Dyna':
    if distt>50.0:
      total_price= (distt*price_per_km)+100
    else:
      total_price= 150

  if transport_type=='Dyna/bed/Dyna':
    if distt>300.0:
      total_price= (distt*price_per_km)+300
    else:
      total_price= 0

  if transport_type=='Lowbed':
    if distt>300.0:
      total_price= (distt*price_per_km)
    else:
      total_price= 0

  if transport_type=='Luxury':
    if distt>149.0:
      total_price= (distt*price_per_km)+(750,000*0.01)
    else:
      total_price= (distt*price_per_km)+(750,000*0.005)

  if transport_type=='Motocycle':
    if distt>50.0:
      total_price= (distt*price_per_km)+100
    else:
      total_price= 150

  st.subheader(f'Total cost of transportation : {total_price}')
  st.number_input('Insert your price')

except:
  pass




