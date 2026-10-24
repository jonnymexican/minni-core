import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Minni Playground",
    layout="wide"
)

st.title("Minni")
st.caption("Turn Memory Into Intelligence")

user_id = st.text_input(
    "User ID",
    value="john"
)

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Remember",
        "Recall",
        "Profile",
        "Context"
    ]
)

with tab1:

    memory = st.text_area("Memory")

    if st.button("Store Memory"):

        response = requests.post(
            f"{BASE_URL}/remember",
            json={
                "user_id": user_id,
                "content": memory
            }
        )

        st.json(response.json())

with tab2:

    query = st.text_input("Query")

    if st.button("Recall"):

        response = requests.post(
            f"{BASE_URL}/recall",
            json={
                "user_id": user_id,
                "query": query
            }
        )

        st.json(response.json())

with tab3:

    if st.button("Generate Profile"):

        response = requests.get(
            f"{BASE_URL}/profile/{user_id}"
        )

        st.json(response.json())

with tab4:

    context_query = st.text_area(
        "Question",
        key="context_question"
    )

    if st.button("Generate Context"):

        response = requests.post(
            f"{BASE_URL}/context",
            json={
                "user_id": user_id,
                "query": context_query
            }
        )

        st.json(response.json())
