import google.generativeai as genai


genai.configure(api_key="API_KEY")
model = genai.GenerativeModel('gemini-pro')

prompt = "You are a helpful customer service agenthere to provide fun for the customer based on the user'spersonal information and topic preferences.This could include fun facts, jokes, or interesting stories. Make sure to make it engaging and fun!Return 'TERMINATE' when you are done"
response = model.generate_content(prompt)
print(response.text)
