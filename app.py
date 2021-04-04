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

private_dyna= st.number_input('Enter number of Private Dyna', min_value= 0, max_value= 100, step= 1)
if st.checkbox('I need insurance.', key= '1'):
  private_dyna_price_per_km= 1.7
else:
  private_dyna_price_per_km= 1  

dyna_bed_dyna= st.number_input('Enter number of Dyna/bed/Dyna', min_value= 0, max_value= 100, step= 1)
st.checkbox('I need insurance.', key= '2')
dyna_bed_dyna_price_per_km= 0.85

lowbed= st.number_input('Enter number of Lowbed', min_value= 0, max_value= 100, step= 1)
st.checkbox('I need insurance.', key= '3')
lowbed_price_per_km= 0.85

luxury= st.number_input('Enter number of Luxury', min_value= 0, max_value= 100, step= 1)
if st.checkbox('I need insurance.', key= '4'):
  luxury_price_per_km= 1.7
else:
  luxury_price_per_km= 1  

motocycle= st.number_input('Enter number of Motocycle', min_value= 0, max_value= 100, step= 1)
if st.checkbox('I need insurance.', key= '5'):
  motocycle_price_per_km= 1.7
else:
  motocycle_price_per_km= 1  

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
  private_dyna_distt= geodesic(lat_lon1, lat_lon2).kilometers
  dyna_bed_dyna_distt= private_dyna_distt
  lowbed_distt= private_dyna_distt
  luxury_distt= private_dyna_distt
  motocycle_distt= private_dyna_distt
  
  st.write(f'The distance is {round(private_dyna_distt, 2)} kilometres.')

  if private_dyna_distt>50.0:
    total_price= total_price+(((private_dyna_distt*private_dyna_price_per_km)+100)*private_dyna)
  else:
    total_price= total_price+(150*private_dyna)

  if dyna_bed_dyna_distt>300.0:    
    total_price= total_price+(((dyna_bed_dyna_distt*dyna_bed_dyna_price_per_km)+300)*dyna_bed_dyna)    
  else:
    total_price= total_price+(0*dyna_bed_dyna)
  
  if lowbed_distt>300.0:
    total_price= total_price+(((lowbed_distt*lowbed_price_per_km)+300)*lowbed)
  else:
    total_price= total_price+(0*lowbed)

  if luxury_distt>149.0:
    total_price= total_price+((((luxury_distt*luxury_price_per_km)+(750000*0.01)))*luxury)
  else:
    total_price= total_price+(((luxury_distt*luxury_price_per_km)+(750000*0.005))*luxury)

  if motocycle_distt>50.0:
    total_price= total_price+(((motocycle_distt*motocycle_price_per_km)+100)*motocycle)
  else:
    total_price= total_price+(150*motocycle)

  st.subheader(f'Total cost of transportation : {round(total_price, 2)}')  
  st.number_input('Insert your price')

except:
  pass



