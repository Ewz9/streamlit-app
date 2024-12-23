#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:52:21 2024

@author: g16
"""

import random
import streamlit as st

# Define the menu dictionary
dict_cat = {
    'a:中餐': ['1:欣葉台菜', '2:曉鹿鳴', '3:金山客家小炒', '4:螃蟹粥', '5:鵝肉'],
    'b:西餐': ['1:牛排', '2:Fridays', '3:Hamburger', '4:Pizza', '5:Pasta'],
    'c:日式': ['1:拉麵', '2:大戶屋', '3:串燒', '4:飯糰'],
    'd:東亞': ['1:咖喱', '2:泰國菜','3:涓豆腐']
}

# Streamlit App
st.title("Uber Eat Choice 🎲")

mode = st.radio("Select an option:", ["Roll dice without constraints", "Scan the menu and set up constraints"])

roll_targets = []

if mode == "Roll dice without constraints":
    # Add all menu items from all categories
    for cat, choices in dict_cat.items():
        roll_targets.extend(choices)

elif mode == "Scan the menu and set up constraints":
    st.write("## Set up constraints:")
    for cat, choices in dict_cat.items():
        st.write(f"### {cat}")
        # User selects items to exclude
        exclude = st.multiselect(f"Exclude items from {cat}:", choices)
        roll_targets.extend([choice for choice in choices if choice not in exclude])

if st.button("Roll Dice"):
    if roll_targets:
        selected = random.choice(roll_targets)
        st.success(f"The random choice is: {selected}")
    else:
        st.error("No valid choices were selected!")
