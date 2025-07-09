# Car-Specs-RAG
🚘 Car Assistant App
A powerful Streamlit web application that helps users:

Ask questions about car specifications from a dataset.

Get personalized car recommendations based on desired specs.

Find real-time online listings of cars for sale using the Serper.dev API (Google Search wrapper).



✅ Features
🔍 Ask car questions: "What's the horsepower of the 2021 BMW M3?" – Powered by RAG (Retrieval-Augmented Generation) over a structured dataset.

🎯 Find a matching car: Input your desired car specs and get suitable cars from a 30k-entry dataset.

🌐 Locate live listings online: Enter a car model and location – get real-time clickable links from trusted sources like Cars.com, CarGurus, AutoTrader, etc.

📚 Source-aware answers: Each RAG answer also shows the vehicle entries used to generate the response.

🧠 Built with LangChain, OpenAI, ChromaDB, and Serper.dev for maximum flexibility and intelligence.



1. 🧠 Ask About Specs
Ask natural language questions about any car specs like:

"What is the top speed of 2022 Audi RS5?"

"Compare the fuel efficiency of Prius and Civic."

"List all features of 2020 Toyota Camry."

The app uses vector search + OpenAI to answer using embedded specs.

✅ Output includes:

Natural language answer.

The specific car makes/models used as reference.

2. 🎯 Find the Car for You
A guided input mode. Just select or enter:

Car type: Sports, Commuter, Electric, etc.

Manufacturer: e.g., Honda, Tesla, BMW

Body type: SUV, Sedan, Coupe, etc.

Drivetrain: AWD, FWD, RWD

🛠 The app constructs a custom query and uses LangChain to search your dataset.

✅ Output:

List of matching vehicles with brief descriptions.

3. 🌐 Find Online Listings
Enter:

Car name/model (freeform, e.g., "2019 Audi Q7 Premium Plus")

Location (city + state)

📡 The app:

Calls the Serper.dev API (Google Search wrapper).

Filters links from sites like AutoTrader, Cars.com, CarGurus, etc.

Returns up to 5 listings with clickable links.

✅ Output:

List of titles + links you can click to view full listings.
