import google.generativeai as genai


genai.configure(api_key="API_KEY")
model = genai.GenerativeModel('gemini-pro')

prompt = "Write a story about a magic backpack that can grant wishes."
response = model.generate_content(prompt)
print(response.text)
