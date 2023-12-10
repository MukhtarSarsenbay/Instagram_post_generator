# main.py

import pandas as pd
import openai
from dotenv import load_dotenv
import os


# Load the Housing Prices Dataset
dataset_path = 'Housing.csv'
housing_data = pd.read_csv(dataset_path)

# Extract relevant information
selected_columns = ['price','area','bedrooms','bathrooms','stories','mainroad','guestroom','basement','hotwaterheating','airconditioning','parking','prefarea','furnishingstatus']  # Add other relevant features
selected_data = housing_data[selected_columns]

# Display a sample of the dataset
print(selected_data.head())



# Load OpenAI API key from environment variables
load_dotenv(dotenv_path=".env")
openai.api_key = os.getenv("openai_token")

def generate_post(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  
        prompt=prompt,
        max_tokens=150  # Adjust as needed
    )
    return response.choices[0].text.strip()

# Example prompt
example_prompt = "Generate an engaging Instagram post for a real estate listing with the following features: price=$500,000, area=2000 sq ft, feature1=..."

# Generate post
generated_post = generate_post(example_prompt)

# Print the generated post
print(generated_post)

# Example generation
num_examples = 20

with open("EXAMPLE.md", "w") as file:
    for _ in range(num_examples):
        # Randomly select a data entry from the dataset
        random_entry = selected_data.sample().squeeze()

        # Format the prompt
        prompt = f"Generate an Instagram post for a real estate listing with the following features: {random_entry}"

        # Generate post
        generated_post = generate_post(prompt)

        # Write to EXAMPLE.md
        file.write(f"{random_entry.to_string()}\n")
        file.write(f"{generated_post}\n")
        file.write("------------------------\n")