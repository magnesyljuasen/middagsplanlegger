import pandas as pd

def middager():
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
    return df

