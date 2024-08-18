     
# import os

# from groq import Groq

# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),  
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Explain the importance of fast language models",   
#         }
#     ],
#     model="llama3-8b-8192",
# )

# print(chat_completion.choices[0].message.content)

from groq import Groq

client = Groq(api_key='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')
response = client.chat.completions.create(
    messages=[{"role": "user", "content": "Hello"}],     
    model="llama3-8b-8192"
)
print(response)

