import streamlit as st
import pandas as pd

st.title("licooorne")
st.subheader("J'aime les licoornes")
st.sidebar.title("Poney")

monImage = "https://images.unsplash.com/photo-1604026732875-e2f78f86e8e6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=600&q=60"
st.image(monImage)
immunite = st.number_input("Entrez le seuil d'immunite collective", 50, 100, 60, 5)/ 100
population = st.number_input("Entrez la population en millions", 5, 300, 65, 5) * 1000000

ip = immunite * population
st.write("Il faut au moins ", "{:,.2f}".format(ip), " personnes contaminees pour atteindre l'immunite collective")

n = 1

def u(n):
    return 200000 + n * 30000

def v(n):
    if n < 20:
        r = 0.05 * u(n)
    else:
        r = 0.05 * u(n) - 0.05 * u(n - 20)
    return r



