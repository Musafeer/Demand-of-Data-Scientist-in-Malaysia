from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import plotly.express as px
import pandas as pd
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Create your views here.


def indexView(request):
    return render(request, 'index.html')


@login_required()
def dashboardView(request):

    # Chart0 companies_top20.csv
    df = pd.read_csv(
        'https://raw.githubusercontent.com/Musafeer/Demand-of-Data-Scientist-in-Malaysia/main/Database/companies_top20.csv')
    fig = px.bar(df, x='jobs', y='companies', text_auto='.2s', color_discrete_sequence=px.colors.qualitative.Set3, orientation='h',
                 title="Data Science Job Availability at Leading Companies", width=1200, height=600)
    fig.update_layout(title_font_size=24, title_x=0.5)
    fig.update_traces(textfont_size=12, textangle=0,
                      textposition="outside", cliponaxis=False)
    chart0 = fig.to_html()

    # # Chart1 companies_bottom
    # df1 = pd.read_csv('https://raw.githubusercontent.com/Musafeer/Demand-of-Data-Scientist-in-Malaysia/main/pyGaz_EDA/final_dataset/companies_bottom.csv')
    # fig1 = px.bar(df1, x='jobs', y='companies', text_auto='.2s',color_discrete_sequence=px.colors.qualitative.Set1, orientation='h',
    #          title="Companies with Limited Job Opportunities " ,width=1200, height=600)
    # fig1.update_layout(title_font_size=24, title_x=0.5)
    # fig1.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    # chart1 = fig1.to_html()

    import plotly.graph_objects as go

# Extract the top 10 skills and their counts

    df = pd.read_csv(
        'https://raw.githubusercontent.com/Musafeer/Demand-of-Data-Scientist-in-Malaysia/main/Database/skills.csv')
    fig2 = px.bar(df, x="Skill", y="Count", hover_name="Skill",
                  title="Top 10 Data Science Skills in Demand", color="Skill", width=1200, height=600)
    # Add labels to the chart
    fig2.update_layout(yaxis_title='Number of occurrences',
                       xaxis_title='Skill', title_font_size=24, title_x=0.5)

    # Show the chart
    chart2 = fig2.to_html()

    # Chart3a cleaned_is_remote2
    df3 = pd.read_csv(
        'https://raw.githubusercontent.com/Musafeer/Demand-of-Data-Scientist-in-Malaysia/main/Database/cleaned_is_remote2.csv')
    df3 = df3.head(10)
    fig3a = px.histogram(df3, y="location", x='num_is_remote', color="is_remote", orientation='h',
                         width=1200, height=600, title="Number of Remote Job Openings by Location")
    fig3a.update_layout(title_font_size=24, title_x=0.5)
    chart3a = fig3a.to_html()

    # Create the boxplot figure with a custom title
    # Salary
    filtered_df = pd.read_csv(
        "https://raw.githubusercontent.com/Musafeer/Demand-of-Data-Scientist-in-Malaysia/main/Database/salary.csv")
    fig = px.box(filtered_df, x="Salary", title="Distribution of Salary")

    # Set the label of the y-axis
    fig.update_layout(yaxis=dict(title="Salary (MYR)"),
                      title_font_size=24, title_x=0.5, width=1200, height=600)

    # Set the color of the boxes to blue
    fig.update_traces(marker_color='blue')

    # Show the figure
    chart4 = fig.to_html()

    # Location
    df = pd.read_csv(
        "https://raw.githubusercontent.com/Musafeer/Demand-of-Data-Scientist-in-Malaysia/main/Database/location.csv")

    # Create bubble map
    fig = px.scatter_geo(df, lat="Latitude", lon="Longitude", size="Count", color="State",
                         title="Demand Based On Location", hover_name="State", size_max=20, width=1200, height=600)
    fig.update_layout(title_font_size=24, title_x=0.5)
    chart5 = fig.to_html()

    context = {
        'chart0': chart0,
        "chart2": chart2,
        "chart3a": chart3a,
        # "chart3b":chart3b,
        "chart4": chart4,
        "chart5": chart5,

    }
    return render(request, 'test2.html', context)


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# def Chart(request):

#     return render(request, 'test2.html', context)
