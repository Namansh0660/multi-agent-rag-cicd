import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

# Simulate reading issue or PR title from GitHub (for demo)
prompt = "Generate a Python function that reverses a string and checks if it's a palindrome."

response = model.generate_content(prompt)

with open("generated_code.py", "w") as f:
    f.write(response.text)

print("[Agent] Generated code saved to 'generated_code.py'")
