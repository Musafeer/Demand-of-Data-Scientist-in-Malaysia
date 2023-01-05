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
    
    
    #Chart0 companies_top20.csv
    # df = pd.read_csv('')    
    # fig = px.bar(df, x='jobs', y='companies', text_auto='.2s',color_discrete_sequence=px.colors.qualitative.Set3, orientation='h',
    #          title="Companies with the most jobs opening")
    # fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    # chart0 = fig.to_html()

    # Chart1 companies_bottom
    # df1 = pd.read_csv('')
    # fig1 = px.bar(df1, x='jobs', y='companies', text_auto='.2s',color_discrete_sequence=px.colors.qualitative.Set1, orientation='h',
    #          title="Companies with the least jobs opening")
    # fig1.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    # chart1 = fig1.to_html()
    
    # Chart2 location_top
    # df2 = pd.read_csv('')
    # fig2 = px.bar(df2, x='job_openings', y='locations', text='job_openings',
    #          color_discrete_sequence=px.colors.qualitative.Dark2, orientation='h',
    #          title="Top 20 locations with the most job openings")
    # chart2 = fig2.to_html()
    
    # Chart3a cleaned_is_remote2
    # df3 = pd.read_csv('')
    # df3 = df3.head(10)
    # fig3a = px.histogram(df3, y="location", x='num_is_remote',color="is_remote", orientation='h')
    # chart3a = fig3a.to_html()

    # Chart3b cleaned_is_remote2
    # df3 = pd.read_csv('')
    # df3 = df3.tail(10)
    # fig3b = px.histogram(df3, y="location", x='num_is_remote',color="is_remote", orientation='h')
    # chart3b = fig3b.to_html()
    
    # Chart4 worldcloud_df.csv
    # df4 = pd.read_csv('')
    # words = []
    # for phrase in df4.summary.values:
    #     for word in phrase.split():
    #         words.append(word)
    # word_list = ' '.join(words)

    # stop_words = stopwords.words('english')
    # stop_words = set(stop_words)
    # wordcloud = WordCloud(background_color='black',
    #                   collocations=False, contour_width=2,
    #                  ).generate(word_list)

    # plt.figure(figsize=(8, 7), facecolor='k')
    # plt.imshow(wordcloud, interpolation="bilinear")
    # plt.axis('off')
    # plt.tight_layout(pad=0);
    

    # context = {
    #     'chart': chart0,
    #     'chart1': chart1,
    #     "chart2": chart2,
    #     "chart3a": chart3a,
    #     "chart3b":chart3b,
    # }
    return render(request, 'test2.html')


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