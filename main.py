import requests
import streamlit as st
from pyrebase import initialize_app
from streamlit_lottie import st_lottie
from PIL import Image
import authorization
import mail
from temperature import Temperature

img = Image.open('calo.jpg')
st.set_page_config(page_title="Weather Calorie Calculator", page_icon=img)

hide_menu_style="""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
</style>
"""
st.markdown(hide_menu_style,unsafe_allow_html=True)

firebaseConfig = {
    'apiKey': "AIzaSyBLC8Y5AHHIOCxBhODj2EoHarv-wpBUHE0",
    'authDomain': "calorie2calculator.firebaseapp.com",
    'projectId': "calorie2calculator",
    'databaseURL': "https://calorie2calculator-default-rtdb.asia-southeast1.firebasedatabase.app",
    'storageBucket': "calorie2calculator.appspot.com",
    'messagingSenderId': "855828674556",
    'appId': "1:855828674556:web:c32b7bb9e7629d908da479",
    'measurementId': "G-FH0ESHZF8R"
}

firebase = initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

#Animation
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

col1, col2= st.columns([1,4])
with col1:
    lottie_animation_1 = "https://assets3.lottiefiles.com/packages/lf20_kljxfos1.json"
    lottie_anime_json = load_lottie_url(lottie_animation_1)
    st_lottie(lottie_anime_json, key="weather")

with col2:
    st.markdown("<h1 style='text-align: center; color: #F55F0E;'>Weather Calorie Calculator</h1>",
                unsafe_allow_html=True)
st.subheader("Know how much Calories you require today depending on your physique and today's weather")
st.subheader("According to many scientific studies **Weather** too plays a key role in determination of your Calorie Requirements!")
lottie_animation_1 = "https://assets1.lottiefiles.com/packages/lf20_6vltyryr.json"
lottie_anime_json = load_lottie_url(lottie_animation_1)
st_lottie(lottie_anime_json, key="calorie")

st.sidebar.markdown("<h1 style='text-align: center; color: #FFFFFF;'>WELCOME !</h1>",
unsafe_allow_html = True)
flag=1
if flag ==1:
    st.info("Login through login option in the left drop down menu to use this service")
gauth = authorization.authorize()
if gauth != 2:
    st.sidebar.write("OR")
    choice = st.sidebar.radio('Login / SignUp to Continue', ['Login', 'SignUp'])
    st.write('<style>div.row-widget.stRadio > div {flex-direction:row;}</style>', unsafe_allow_html=True)
    email = st.sidebar.text_input("Enter your email address")
    password = st.sidebar.text_input("Enter your password", type="password")


if gauth == 2:
    flag = 0
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")

    with st.sidebar:
        c1, c2, c3 = st.columns([1, 15, 1])
        with c2:
            lottie_animation_2 = "https://assets1.lottiefiles.com/packages/lf20_enlitdkl.json"
            lottie_anime_json = load_lottie_url(lottie_animation_2)
            st_lottie(lottie_anime_json, key="hello")
    name = st.text_input("Enter your name")
    emaill = st.text_input("Enter your email")
    height= st.text_input("Enter your height")
    weight=st.text_input("Enter your weight")
    age=st.text_input("Enter your age")
    country=st.text_input("Enter your country")
    city=st.text_input("Enter your city")
    result = st.button("Get Calories Required")

    if result:
        height = int(height)
        weight = int(weight)
        age = int(age)
        temp = Temperature(country=country, city=city).get()
        success = mail.send_email(name, emaill, weight,height,age,temp,city,country)
        if success:
            st.write("Calorier required Mailed Successfully!")
else:
    if choice == "SignUp":
        handle = st.sidebar.text_input("Please enter your nickname", value="CoolPanda")
        submit = st.sidebar.button('Create my Account')
        if submit:
            try:
                user = auth.create_user_with_email_and_password(email, password)
                st.sidebar.success("Your account is created successfully!")
                st.sidebar.success("Click on Login to continue")
                st.balloons()
                user = auth.sign_in_with_email_and_password(email, password)
                db.child(user['localId']).child("Handle").set(handle)
                db.child(user['localId']).child("Id").set(user['localId'])

            except:
                st.sidebar.info("This account already exists !")

    if choice == "Login":
        login = st.sidebar.checkbox('Login', key=2)
        if login:
            # try:
                user = auth.sign_in_with_email_and_password(email, password)
                flag = 0
                st.sidebar.info("You have Logged in Successfully!")
                name = st.text_input("Enter your name")
                emaill = st.text_input("Enter your email")
                height = st.text_input("Enter your height")
                weight = st.text_input("Enter your weight")
                age = st.text_input("Enter your age")
                country = st.text_input("Enter your country")
                city = st.text_input("Enter your city")
                result = st.button("Get Calories Required")
                if result:
                    height = int(height)
                    weight = int(weight)
                    age = int(age)
                    temp = Temperature(country=country, city=city).get()
                    success = mail.send_email(name, emaill, weight,height,age,temp,city,country)
                    if success:
                        st.write("Calories Required Mailed Successfully!")
                        st.balloons()

            # except:
            #      st.sidebar.info("Enter a valid email/password !")
