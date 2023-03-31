#---PIP PACKAGES---#
import streamlit as st

#---BUILT-IN PYTHON MODULES
from datetime import datetime, date
import calendar
import uuid


#---IMPORT THE DATABASE PYTHON FILE db.py---#
import db as db

#---STREAMLIT SETTINGS---#
page_title = "Weekly dinner and shopping app"
page_icon = ":pouch:"
layout = "centered"

#---STREAMLIT PAGE CONFIG---#
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(f"{page_title} {page_icon}")

#---STREAMLIT CONFIG HIDE---#
hide_st_style = """<style>
                #MainMenu {visibility : hidden;}
                footer {visibility : hidden;}
                header {visibility : hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

#---DICT INIT---#
shopping_list = {
    "fruit_and_veg" : {"title" : "Fruit and Veggies", "items" : []},
    "meat_and_fish" : {"title" :"Fresh meat and fish", "items" : []},
    "housekeeping" : {"title" :"Housekeeping supplies", "items" : []},
    "carbs" : {"title" : "Potatoes, rice, pasta, etc", "items" : []},
    "snacks" : {"title" : "Snacks", "items" : []},
    "dairy" : {"title" : "Dairy", "items" : []},
    "personal_care" : {"title" : "Personal care", "items" : []},
    "pets" : {"title" : "Pets", "items" : []},
    "beverages" : {"title" : "Beverages", "items" : []},
    "spices_and_cond" : {"title" : "Spices and condiments", "items" : []},
    "frozen" : {"title" : "Frozen", "items" : []}
    }


key_dict = {
    'fruit_and_veg': [],
    'meat_and_fish': [],
    'housekeeping': [],
    'carbs': [],
    'snacks': [],
    'dairy': [],
    'personal_care': [],
    'pets': [],
    'beverages': [],
    'spices_and_cond': [],
    'frozen': []
    }
ingredients_dict = {
    }

instructions_dict = {
    }

#---PERIOD VALUES---#
year = datetime.today().year
month = datetime.today().month
day = datetime.today().day+4
months = list(calendar.month_name[1:])
week_number = date(year, month, day).isocalendar()[1]
week = Week(year, week_number)
week_plus1 = Week(year, week_number+1)
