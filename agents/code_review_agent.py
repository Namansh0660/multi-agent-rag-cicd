import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

code_files = [f for f in os.listdir() if f.endswith(".py") and "agent" not in f]

review_report = "# Code Review Report\n\n"

for file in code_files:
    with open(file, "r") as f:
        code = f.read()

    prompt = f"Review the following code for best practices and issues:\n\n{code}"
    response = model.generate_content(prompt)
    review_report += f"## {file}\n{response.text}\n\n"

with open("reports/code_review_report.md", "w") as f:
    f.write(review_report)

print("[Agent] Code review completed and saved.")
