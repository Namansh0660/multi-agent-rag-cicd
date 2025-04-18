import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.0-flash")
prompt = "Generate a Python function that reverses a string and checks if it's a palindrome."

response = model.generate_content(prompt)

# 🔥 Save the output in outputs folder
os.makedirs("outputs", exist_ok=True)
with open("outputs/generated_code.py", "w") as f:
    f.write(response.text)

print("[Agent] Generated code saved to 'outputs/generated_code.py'")
