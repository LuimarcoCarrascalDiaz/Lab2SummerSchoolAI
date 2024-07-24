import google.generativeai as genai


genai.configure(api_key="API_KEY")
model = genai.GenerativeModel('gemini-pro')

prompt = "You are an SEO reviewer"
response = model.generate_content(prompt)
print(response.text)
