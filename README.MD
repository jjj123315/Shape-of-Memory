## Introduction 
### How to perform semantic analysis and data organization on a large CSV file
In the Fall 2024 semester, I attempted to collect posts from the Instagram platform and conducted semantic analysis and sentiment research on the data. Throughout the research process, my main focus was on how to analyze and organize the large dataset collected (including image URLs, post text, geographical location information, etc.). The workflow, from operating the semantic analysis model to the preliminary organization of the CSV files, can be divided into the following parts:
1. Sentiment analysis models, including Ollama and Transformers.
2. Perform simple data organization on the obtained CSV files, such as averaging the score results for multiple entries corresponding to the same geographical location or re-extracting multiple keywords, making it easier for quick reading or phenomenon research.
3. Interactive map creation.
--- 
### Key resources
1. Datasets
- The text or images you want to analyze.
-- 
2.  Simulation model & implementation
- Ollama-llama2 
- Ollama-7B 
- nlptown/bert model 
- Folium
- Google geocoing API
-- 
3. Tools & languages
- Python
- Docker
--- 
### Associated papers
- Chen, Chia-Hao, et al."A Brief Introduction to Sentence BERT Semantic Analysis Model"(2022)
- Bolei Zhou, et al."Recognizing City Identity via Attribute Analysis of Geo-tagged Images"(2014)
- JAYEDI AMAN, et al."Sensing The City"(2022)
