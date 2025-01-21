from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .forms import MyForm
from django.http import JsonResponse
import subprocess
import wikipediaapi
import pandas as pd

   
def fetch_from_wikipedia(ingredient):
    wiki_wiki = wikipediaapi.Wikipedia('en', user_agent='MyIngredientAnalyzer/1.0')
    page = wiki_wiki.page(ingredient)
    if page.exists():
        return page.summary.split('.')[0]  # Get the first sentence of the summary
    else:
        return f"No information found for {ingredient} on Wikipedia."
# Function to analyze ingredients
def analyze_ingredients(input_text):
    input_text=input_text.lower()
    # Load the dataset
    try:
        df = pd.read_excel("C:\\Users\\Rutuja\\OneDrive\\Desktop\\NLP_Ingred\\playground\\ingredients.xlsx")

    except FileNotFoundError:
        return "Error: Dataset not found."

    # Split the input text by commas to get individual ingredients
    ingredients = [ingredient.strip() for ingredient in input_text.split(',')]
    
    # Process ingredients
    results = []
    purpose="unknown"
    for ingredient in ingredients:
        # Check if ingredient exists in the dataset
        if ingredient in df['Name'].values:
            row = df[df['Name'] == ingredient].iloc[0]  # Get the row corresponding to the ingredient
            purpose = row['Purpose']
            health_concern = row['Health Concern']
            value = row['Value']
            # Analyze safety
            if value == 'safe':
                analysis = "Safe to use."
            elif value == 'avoid':
                analysis = f"Avoid: May pose health concern - {health_concern}."
            else:
                analysis = f"Use with caution - {value}."
        else:
            # If ingredient not found in dataset, provide a generic response
           #wiki_info = fetch_from_wikipedia(ingredient)
           #analysis = f"{wiki_info}"

            analysis="Not found"
        # Beautify output
        result_str = f"Ingredient: {ingredient}\nPurpose: {purpose}\nAnalysis: {analysis}\n"
        results.append(result_str)

    # Combine results into a single string
    return "\n".join(results)


def submit_ingredient(request):
     if request.method == 'POST':
        # Handle form submission
        # ...
        ingredient = request.POST.get('ingredient')
        output = analyze_ingredients(ingredient)

       

        # Redirect to y.html with output as context data
        print(ingredient)
        return render(request, 'y.html', {'output': output})
       
        return redirect('y') # Redirect to another page
     else:
        # Handle other HTTP methods (e.g., GET)
        # ...
        return render(request, 'template.html')

def my_view(request):
    form = MyForm()
    data={{'formm': form}}
    return render(request, 'index.html',{'formm':form} )

def sayHello(request):
    return render(request,'index.html')

def submitform(request):
    if request.method=="POST":
        message=request.POST['message']
        print(message)
    return render(request,'x.html') 

# views.py
def y_view(request, output=None):
    # Render y.html with output
    return render(request, 'y.html', {'output': output})
