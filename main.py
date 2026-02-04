from google import genai

client = genai.Client()

user_input = input("Enter text: ")

prompt = f"""
You are a professional assistant.
Respond with only the final answer.
Do not add explanations, emojis, headings, or extra text.

{user_input}
"""

response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents=prompt
)

print(response.text.strip())
