# 🚘 Car Assistant App

A powerful **Streamlit web application** that helps users:
- ❓ Ask specific questions about car specifications.
- 🧠 Get intelligent car recommendations based on features.
- 🌐 Find live car listings for sale online using Google Search (via Serper.dev API).

Built using **LangChain**, **OpenAI**, **Chroma**, and **Serper.dev** with an interactive UI powered by **Streamlit**.

---

## ✅ Features

- 🔍 **Ask Car Questions** – Ask detailed questions about horsepower, 0–60 times, fuel efficiency, top speed, drivetrain, and more.
- 🎯 **Find a Car for You** – Use filters like manufacturer, body type, drivetrain, and car class to find vehicles that match your needs from a 30k+ entry dataset.
- 🌐 **Find Online Listings** – Input your car model and location to get **real, clickable listings** from trusted sites like Cars.com, AutoTrader, and CarGurus.

---

## 🧭 Usage Modes

The application supports **three powerful modes**:

### 1. 🧠 Ask About Specs

Input natural language questions about any car spec.

**Examples:**
- "What’s the horsepower of the 2020 BMW M3?"
- "Compare 0–60 time for Audi A6 and Tesla Model 3."
- "What are the features of a 2022 Toyota Corolla?"

🔗 **Answers include**:
- A concise AI-generated summary.
- A list of car entries used to generate the answer (make/model/year).

---

### 2. 🎯 Find the Car for You

Fill out a short form to specify your desired vehicle characteristics:
- Car Type (Sports, Luxury, Electric, etc.)
- Manufacturer (e.g., BMW, Honda, Toyota)
- Body Type (Sedan, SUV, Truck, etc.)
- Drivetrain (AWD, RWD, FWD)

🛠 The system builds a smart RAG query to pull matching cars from the vector store.

**Example Output:**
> "2022 BMW M440i xDrive Coupe – AWD – Sport Class"

---

### 3. 🌐 Find Online Listings

Use this mode to find real car listings currently for sale online.

**Input fields:**
- Car Query (e.g., "2021 Honda Accord Sport")
- Location (e.g., "Los Angeles, CA")

The app uses the **Serper.dev** API to search Google and filters for car marketplaces.

🔗 **Output:**
- Up to 5 clickable links to real listings (Cars.com, CarGurus, AutoTrader, etc.)
- Each result includes a title and link.

---****
