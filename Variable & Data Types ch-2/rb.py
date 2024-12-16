import openai

# Initialize OpenAI API client
openai.api_key = "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"

# Make a request to the OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use the correct model name, e.g., "gpt-4" or "gpt-3.5-turbo"
    messages=[{"role": "user", "content": "Hola Amigo"}],
    temperature=0.5,
    top_p=1,
    max_tokens=1024,
    stream=True
)

# Stream and print the response
for chunk in response:
    if "choices" in chunk:
        print(chunk["choices"][0]["delta"].get("content", ""), end="")
