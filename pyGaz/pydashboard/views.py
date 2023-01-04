from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import plotly.offline
import plotly.express as px
import pandas as pd
# Create your views here.


def indexView(request):
    return render(request, 'index.html')


@login_required()
def dashboardView(request):
    df = px.data.iris()

    # Chart1

    fig1 = px.scatter(df, x="sepal_width", y="sepal_length", color="species",height=600, width=1200)
    chart1 = fig1.to_html()

    # Chart2

    df = px.data.tips()
    fig2 = px.bar(df,
                 x="sex",
                 y="total_bill",
                 color="smoker",
                 barmode="group",
                 facet_row="time",
                 facet_col="day",
                 category_orders={
                     "day": ["Thur", "Fri", "Sat", "Sun"],
                     "time": ["Lunch", "Dinner"]
                 },height=600, width=1200)
    chart2 = fig2.to_html()

    # Chart3
    df = px.data.gapminder()
    fig3 = px.scatter(df.query("year==2007"),
                     x="gdpPercap",
                     y="lifeExp",
                     size="pop",
                     color="continent",
                     hover_name="country",
                     log_x=True,
                     size_max=60,
                     height=600, width=1200)

    chart3 = fig3.to_html()

    context = {
        'chart1': chart1,
        'chart2': chart2,
        "chart3": chart3,
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