import streamlit as st
import requests

# Title of the app
st.title('Taxi Fare Prediction')

# Subtitle
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

# Add Streamlit input fields
pickup_datetime = st.text_input('Pickup Date and Time (YYYY-MM-DD HH:MM:SS)', '2022-01-01 00:00:00')
pickup_longitude = st.number_input('Pickup Longitude', -73.985428)
pickup_latitude = st.number_input('Pickup Latitude', 40.748817)
dropoff_longitude = st.number_input('Dropoff Longitude', -73.985428)
dropoff_latitude = st.number_input('Dropoff Latitude', 40.748817)
passenger_count = st.number_input('Passenger Count', 1, step=1)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

# Define the URL for the API
url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':
    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''
2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

# Button to get prediction
if st.button('Get Fare Prediction'):
    # Step 2: Build the dictionary of parameters
    params = {
        'pickup_datetime': pickup_datetime,
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }

    # Step 3: Call the API using the requests package
    response = requests.get(url, params=params)

    # Step 4: Retrieve the prediction from the JSON returned by the API
    if response.status_code == 200:
        prediction = response.json()
        fare = prediction['fare']
        # Display the prediction to the user
        st.write(f'The predicted fare is ${fare:.2f}')
    else:
        st.write('Error in API call')
