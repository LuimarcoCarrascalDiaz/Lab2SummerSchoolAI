import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-pro')

prompt = "Write a story about a magic backpack that can grant wishes."
response = model.generate_content(prompt)
print(response.text)
