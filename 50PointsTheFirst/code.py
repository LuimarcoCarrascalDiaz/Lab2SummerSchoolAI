import google.generativeai as genai


genai.configure(api_key="AIzaSyADAzhsx3WDJmLwg5KPi_joaDzyBLvIS3E")
model = genai.GenerativeModel('gemini-pro')

prompt = "Write a story about a magic backpack that can grant wishes."
response = model.generate_content(prompt)
print(response.text)
