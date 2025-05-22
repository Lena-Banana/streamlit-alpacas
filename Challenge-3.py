# Import des bibliothèques
import pandas as pd
import streamlit as st
import json
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Authentification

# Import du CSV et conversion en JSON
df_account = pd.read_csv('account_data.csv', sep=';')
df_account.set_index('usernames', inplace=True)
account_json = {"usernames" : json.loads(df_account.to_json(orient='index'))}

# Création du formulaire
authenticator = Authenticate(account_json,
                             "cookie_name",
                             "cookie key",
                             30)

authenticator.login()

# Conditions
if st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')

# Création du site
if st.session_state["authentication_status"]:
    # Menu
    with st.sidebar:
        authenticator.logout("Déconnexion")
        st.text(f"Bienvenue {st.session_state['username']}")
        page = option_menu(menu_title=None,
                        options=["🦄 Accueil", "📷 Album photo de bébés alpagas"])

    # Page d'accueil
    if page == "🦄 Accueil":
        st.title("Bienvenue sur ma page")
        st.image("https://pbs.twimg.com/media/GMWN4osa4AI1W-X.jpg")
    
    # Album photo
    elif page == "📷 Album photo de bébés alpagas":
        st.title("Bienvenue dans l'album des bébés alpagas")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://i.pinimg.com/564x/22/3b/1a/223b1aa3effc17e56117cf1fca9eaa5a.jpg")
        with col2:
            st.image("https://i.pinimg.com/736x/a7/e3/fb/a7e3fb9f8f3676e7acc239529f28c8ac.jpg")
        with col3:
            st.image("https://www.boredpanda.com/blog/wp-content/uploads/2021/09/61557cedc46a5_koq9wu479u051-png__700.jpg")
