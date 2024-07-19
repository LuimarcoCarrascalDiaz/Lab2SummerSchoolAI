import google.generativeai as genai


genai.configure(api_key="API_KEY")
model = genai.GenerativeModel('gemini-pro')

prompt = "you are a lawyer consultant"
response = model.generate_content(prompt)
print(response.text)
