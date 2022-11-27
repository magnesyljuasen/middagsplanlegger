import streamlit as st
import pandas as pd
import random

with open("main.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

df = pd.DataFrame({
    'Middag' : [
    "Middagspølser", 
    "Kjøttboller",
    "Kyllingvinger",
    "Wok m/kylling",
    "Wok m/svin",
    "Indisk",
    "Kylling bretagne m/ris",
    "Kylling bretagne m/potetmos",
    "Grillet kyllingspyd",
    "Kyllingsalat",
    "Taco",
    "Nachos",
    "Kebab",
    "Lasagne",
    "Pasta m/kjøttsaus",
    "Pannekaker og suppe",
    "Pasta carbonara",
    "Fiskepinner",
    "Hamburger",
    "Grøt",
    "Biffsnadder",
    "Pizza",
    "Vårruller"
    ],
    'Ingredienser' : [
    ["Potetmos", "Pølser", "Brokkoli"], 
    ["Kyllingkjøttboller", "Tomatsaus", "Pasta"],
    ["Pommes frites", "Kyllingvinger", "Ruccola", "Hvitløksbrød"],
    ["Woksaus", "Brokkoli", "Vannkastanjer", "Minimais", "Nudler", "Kyllingfilet"],
    ["Woksaus", "Brokkoli", "Vannkastanjer", "Minimais", "Ris", "Svinefilet"],
    ["Naan brød", "Kyllingfilet", "Indisk saus", "Salat"],
    ["Kyllingfilet", "Bretagnesaus", "Ris", "Hvitløksbrød"],
    ["Kyllingfilet", "Bretagnesaus", "Potetmos", "Hvitløksbrød"],
    ["Kyllingfilet", "Ottos grill-marinade", "Foccacia", "Ris", "Aioli"],
    ["Ost", "Kyllingfilet", "Hvitløksdressing", "Pasta", "Pinjekjerner", "Krutonger", "Salat"],
    ["Kjøttdeig", "Tacokrydder", "Tacolefser", "Nachochips", "Salsa", "Rømme", "Ost", "Agurk", "Avokado", "Mais"],
    ["Nachochips", "Kjøttdeig", "Salsa", "Rømme", "Ost"],
    ["Lett skummelt melk", "Fersk gjær", "Kjøttdeig", "Kebabkrydder", "Kebabdressing", "Pommes frites", "Salat", "Agurk", "Paprika"],
    ["Kjøttdeig", "Hvitløksbrød", "Lasagnemix", "Melk", "Salat"],
    ["Kjøttdeig", "Pasta", "Tomatpure", "Melk", "Hvitløksbrød", "Salat", "Parmesan"],
    ["Egg", "Melk", "Mel", "Suppe"],
    ["Pasta", "Egg", "Melk", "Bacon", "Parmesan", "Hvitløsbrød"],
    ["Fiskepinner", "Potetmos"],
    ["Hamburger", "Burgerbrød", "Pommes frites", "Salat", "Hamburgerdressing", "Cheddar"],
    ["Grøt", "Smør", "Kanel"],
    ["Biffstrimler", "Burgerbrød", "Pommes frites", "Salat", "Bernaise"],
    ["Peppes pizzasaus", "Pizzabunn", "Ost", "Strandaskinke", "Ruccola", "Rømmedressing", "Pepperoni"],
    ["Vårruller", "Ris"]
    ]
})

st.title("😋 Middagsplanleggeren")
with st.expander("Middager"):
    st.write(df)

tab1, tab2 = st.tabs(["Velg selv", "Tilfeldig"])
with tab1:
    dinner_list = st.multiselect("Velg middager", options=df["Middag"].to_numpy().flatten())
    if len(dinner_list) > 0:
        selected_arr = []
        ingredient_list = []
        for i in range(0, len(dinner_list)):   
            with st.expander(f"{df.iat[i,0]}"):
                st.write(df.iat[i,1])
            #--
            
            for index, ingredient in enumerate(df.iat[i,1]):
                ingredient_list.append(ingredient)

        ingredient_list = list(dict.fromkeys(ingredient_list))
        c1, c2 = st.columns(2)
        with c1:
            st.caption("Middager")
            st.write(dinner_list)
        with c2:
            st.caption("Ingredienser")
            st.write(ingredient_list)
        


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
            st.write(dinner_list)
        with c2:
            st.caption("Ingredienser")
            st.write(ingredient_list)




