import openai

# Replace with your actual OpenAI API key when testing locally
openai.api_key = 'your-openai-key'

def solve_question(question):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You're an expert tutor for JEE/NSET."},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']
