from ollama import chat
from gmail_send import send_email
import os
from dotenv import load_dotenv

load_dotenv()
model = os.getenv('MODEL')

#initialise
messages = [
    {
        'role':'system',
        'content':'You are Mailo, a helpful assistant. Use provided tools wherever necessary.'
    }
]

print(f'You are running {model}')
print("---Say 'bye' to exit chat---")


tools = [
    {
        'type':'function',
        'function':{
            'name':'send_email',
            'description':'send email using gmail account of user. DO NOT use emojis.',
            'parameters':{
                'type':'object',
                'properties':{
                    'to':{
                        'type':'string',
                        'description':'recipient email id'
                    },
                    'subject':{
                        'type':'string',
                        'description':'what the email is about'
                    },
                    'body':{
                        'type':'string',
                        'description':'content of the email'
                    }
                },
                'required':['to','subject','body']
            }
        }
    }
]

while True:
    user_input = input('\nYou: ')

    if user_input == 'bye':
        break

    messages.append({
        'role':'user',
        'content': user_input
    }
    )

    response = chat(
        model=model,
        messages=messages,
        tools=tools
    )
    messages.append(response.message)

    if response.message.tool_calls:
        for tool_call in response.message.tool_calls:
            function_name = tool_call.function.name
            args = tool_call.function.arguments

            if function_name == 'send_email':
                result = send_email(**args)

                messages.append({
                    'role':'tool',
                    'content': str(result)
                })
        print(f'Mailo: Sent Sucessfully')

    else:
        print(f'\nMailo: {response.message.content}')


