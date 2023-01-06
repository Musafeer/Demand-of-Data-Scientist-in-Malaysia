# Data Science Job Demand in Malaysia

This project aims to analyse the demand for data science jobs in Malaysia.

## Data Scrapping

The data for this project was scrapped using a scrapper built with Selenium.

## Data Analysis

In the data analysis phase of this project, we used the following techniques and tools:

- Data manipulation with pandas
- Numerical operations with numpy
- Data visualization with plotly
- Word cloud generation with wordcloud
- Serialization of specialized words with pickle

## Web App

The Django web app for this project requires login and presents a dashboard upon successful login. The dashboard includes Plotly visualizations of the data, including information on salary demand, locations with the most job postings, companies with the most job postings, remote vs on-site job offers, and data scientist skills.

## Technologies Used

- Selenium (webscrapping)
- Jupyter Notebook (EDA)
- pandas (dataframe)
- numpy (array object handling)
- plotly (interactive visualisation)
- wordcloud (static visualisation)
- pickle (pickling words)
- Django (webapp)
- whitenoise (serving static files)
- nltk (text processing)
- gunicorn (python web server gateway)

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

## Deployed link

https://demand-of-data-scientist-in-malaysia-hjq4-1q38-ma-f7w7i6uxla-as.a.run.app/
