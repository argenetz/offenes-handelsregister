import streamlit as st
import requests

from datetime import datetime

url = "https://www.handelsregister.de/rp_web/erweitertesuche.xhtml"
options = {
    "schlagwoerter": "Looft-Schmidt GmbH & Co. 4. Betriebs KG",
    "schlagwortOptionen": 3
}

if st.button("Send Request", type="primary"):
    result = requests.post(url, json=options)
    directory = "responses/"
    filename = "response_" + datetime.now().strftime("%Y_%m_%d-%H_%M_%S") + ".html"

    st.write(result.status_code)
    st.write('Response in file "' + filename + '".')

    f = open(directory + filename, "a")
    f.write(result.text)
    f.close()

    result.close()
