# app.py – Streamlit app for Car Specs RAG + Find Cars + Online Listings

import streamlit as st
from rag import qa_chain
from serper_search import search_car_online

st.set_page_config(page_title="Car Spec & Finder Assistant", layout="wide")
st.title("🚘 Car Assistant")

mode = st.radio("Choose Mode:", [
    "Ask about specs",
    "Find the car for you",
    "Find online listings"
], horizontal=True)

if mode == "Ask about specs":
    st.markdown("""
    Ask questions about car specifications, such as:
    - "What is the horsepower of the 2020 BMW M3?"
    - "Compare the top speed of Audi A4 and Mercedes C300."
    - "Give me every spec for the 2022 Audi A4."
    """)

    user_input = st.text_input("Enter your car spec question:", key="input_spec")

    if st.button("Ask") and user_input:
        with st.spinner("Thinking..."):
            try:
                result = qa_chain({"query": user_input})
                st.subheader("Answer")
                st.write(result["result"])

                st.subheader("Sources")
                for doc in result["source_documents"]:
                    make = doc.metadata.get("make", "Unknown")
                    model = doc.metadata.get("model", "Unknown")
                    year = doc.metadata.get("year", "Unknown")
                    st.markdown(f"- **{make} {model} {year}**")

            except Exception as e:
                st.error(f"An error occurred: {e}")

elif mode == "Find the car for you":
    st.header("🔍 Find the Car that Matches Your Specs")

    col1, col2 = st.columns(2)
    with col1:
        car_type = st.selectbox("Car type:", ["Sports", "Luxury", "Off-Road", "Commuter", "Electric", "Hybrid"])
        manufacturer = st.text_input("Manufacturer (e.g., Honda, Toyota, BMW)")
    with col2:
        body_type = st.selectbox("Body type:", ["Sedan", "SUV", "Coupe", "Truck", "Van", "Wagon"])
        drivetrain = st.selectbox("Drivetrain:", ["FWD", "RWD", "AWD"])

    if st.button("Find Matching Cars"):
        if not manufacturer:
            st.warning("Please fill out the manufacturer field.")
        else:
            with st.spinner("Searching car specs from dataset..."):
                query = f"List {car_type} cars from {manufacturer} with {body_type} body type and {drivetrain} drivetrain"
                try:
                    result = qa_chain({"query": query})
                    st.subheader("Matching Cars:")
                    st.write(result["result"])
                except Exception as e:
                    st.error(f"An error occurred during spec search: {e}")

elif mode == "Find online listings":
    st.header("🌐 Find Online Listings for Your Car")

    car_query = st.text_input("Enter the car you're looking for (e.g., 2021 Toyota Camry)", key="car_query")
    location = st.text_input("Enter your location (e.g., Los Angeles, CA)", key="location")

    if st.button("Search Listings"):
        if not car_query or not location:
            st.warning("Please fill in both car query and location.")
        else:
            with st.spinner("Searching for online listings..."):
                try:
                    results = search_car_online(car_query, location)
                    if results:
                        st.success(f"Listings for '{car_query}' in '{location}':")
                        for i, (title, url) in enumerate(results, 1):
                            st.markdown(f"{i}. [{title}]({url})")
                    else:
                        st.warning("No listings found. Try a different query or location.")
                except Exception as e:
                    st.error(f"An error occurred while searching listings: {e}")