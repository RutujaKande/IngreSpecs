import pandas as pd

def main(ingredient_str):
    try:
        df = pd.read_excel("C:/Users/Rutuja/OneDrive/Desktop/NLP_Ingred/Medilab/ingredients.xlsx")
    except FileNotFoundError:
        return "Error: File not found"

    ingredients = [ingredient.strip() for ingredient in ingredient_str.split(',')]

    output = []
    output.append("Name\tHealth Concern\tPurpose\tDescription")

    for ingredient in ingredients:
        row = df[df['Name'] == ingredient]
        if not row.empty:
            name = row.iloc[0]['Name']
            purpose = row.iloc[0]['Purpose']
            health_concern = row.iloc[0]['Health Concern']
            value = row.iloc[0]['Value']
            description = get_description(purpose)
            if value.lower() == "safe":
                output.append(f"{name}\tSafe\t{purpose}\t{description}")
            else:
                health_concern_description = get_health_concern_description(health_concern)
                output.append(f"{name}\t{health_concern}\t{purpose}\t{health_concern_description}")
        else:
            output.append(f"{ingredient}\tNot found\t\t")

    return '\n'.join(output)

def get_description(purpose):
    # Here you can add a dictionary or a function to get a description of the purpose
    # This is just a placeholder
    return f"A substance used to {purpose.lower()}."

def get_health_concern_description(health_concern):
    # Here you can add a dictionary or a function to get a description of the health concern
    # This is just a placeholder
    return f"It may cause {health_concern.lower()}."

# Example usage:
ingredients = "Acesulfame potassium, Acetic Acid, Advantame"
results_text = main(ingredients)
print(results_text)
