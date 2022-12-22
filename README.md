# Data Science Job Demand in Malaysia

This project aims to analyse the demand for data science jobs in Malaysia.

## Data Scrapping

The data for this project was scrapped using a scrapper built with Selenium.

## Data Analysis

The data was then analysed using Jupyter Notebook. We used pandas for dataframe manipulation, numpy for numerical operations, plotly for data visualisation, and wordcloud for generating word clouds. We also used pickle to save specialised words for later use.

## Web App

We also created a Django web app that requires login and presents a dashboard upon successful login. The dashboard contains Plotly visualisations of the data.

## Technologies Used
- Selenium
- Jupyter Notebook
- pandas
- numpy
- plotly
- wordcloud
- pickle
- Django

## How to Run

To run this project, you will need to have Python and Django installed on your machine.

1. Clone this repository:
git clone https://github.com/Musafeer/data-science-job-demand-malaysia.git


2. Navigate to the project directory:
cd data-science-job-demand-malaysia

3. Install the required packages:
pip install -r requirements.txt


4. Run the Django development server:
python manage.py runserver


5. Open your web browser and go to http://localhost:8000 to access the web app.
