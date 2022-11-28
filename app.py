import streamlit as st
import pandas as pd
import random
import numpy as np
from scripts.middager import middager

#--
with open("main.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

def main():
    df = middager()
    st.title("😋 Middagsplanlegger")
    with st.expander("Middager"):
        st.write(df)
    tab1, tab2 = st.tabs(["Velg selv", "Tilfeldig"])
    with tab1:
        dinner_list = st.multiselect("Velg middager", options=df["Middag"].to_numpy().flatten())
        if len(dinner_list) > 0:
            selected_arr = []
            ingredient_list = []
            for i in range(0, len(dinner_list)):
                for j, value in enumerate(df['Middag']):
                    if value == dinner_list[i]:
                        break
                with st.expander(f"{dinner_list[i]}"):
                    st.write(df.iat[j,1])
                #--
                for index, ingredient in enumerate(df.iat[j,1]):
                    ingredient_list.append(ingredient)

            ingredient_list = list(dict.fromkeys(ingredient_list))
            c1, c2 = st.columns(2)
            with c1:
                st.caption("Middager")
                st.write(sorted(dinner_list))
            with c2:
                st.caption("Ingredienser")
                st.write(sorted(ingredient_list))
            
    with tab2:
        #--
        if st.button("Hva skal vi ha til middag?"):
            selected_arr = []
            ingredient_list = []
            dinner_list = []
            for i in range(0,7):
                selected = random.randint(0, len(df)-1)
                while selected in selected_arr:
                    selected = random.randint(0, len(df)-1)
                selected_arr.append(selected)
                dinner_list.append(df.iat[selected,0])   
                with st.expander(f"{df.iat[selected,0]}"):
                    st.write(df.iat[selected,1])
                #--
                
                for index, ingredient in enumerate(df.iat[selected,1]):
                    ingredient_list.append(ingredient)

            ingredient_list = list(dict.fromkeys(ingredient_list))
            c1, c2 = st.columns(2)
            with c1:
                st.caption("Middager")
                st.write(sorted(dinner_list))
            with c2:
                st.caption("Ingredienser")
                st.write(sorted(ingredient_list))

main()


