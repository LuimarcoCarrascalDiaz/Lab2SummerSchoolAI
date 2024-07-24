import google.generativeai as genai


genai.configure(api_key="API_KEY")
model = genai.GenerativeModel('gemini-pro')

prompt = "Write a concise but engaging blogpost about DeepLearning.AI. Make sure the blogpost iswithin 100 words."
response = model.generate_content(prompt)
print(response.text)
