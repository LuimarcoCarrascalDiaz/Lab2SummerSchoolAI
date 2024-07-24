import google.generativeai as genai


genai.configure(api_key="API_KEY")
model = genai.GenerativeModel('gemini-pro')

prompt = "Your name is Cathy and you are a stand-up comedian."
response = model.generate_content(prompt)
print(response.text)
