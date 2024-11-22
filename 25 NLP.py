import openai

openai.api_key = 'your-api-key-here'

prompt = "Once upon a time, in a faraway kingdom, there was a dragon who..."

response = openai.Completion.create(
  engine="text-davinci-003",  # You can use "gpt-3.5-turbo" as well
  prompt=prompt,
  max_tokens=50
)

print(response.choices[0].text.strip())
