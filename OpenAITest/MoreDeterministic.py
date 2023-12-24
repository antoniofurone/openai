import asyncio
import openai
import pprint
import difflib


GPT_MODEL = "gpt-3.5-turbo"

async def get_chat_response(system_message: str, user_request: str, seed: int = None):
    try:
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_request},
        ]

        response = openai.chat.completions.create(
            model=GPT_MODEL,
            messages=messages,
            seed=seed,
            max_tokens=200,
            temperature=0.7,
        )

        response_content = response.choices[0].message.content
        system_fingerprint = response.system_fingerprint
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = (
            response.usage.total_tokens - response.usage.prompt_tokens
        )

        
        print("** response_content ***")
        print(response_content)
        print("*** system_fingerprint=",system_fingerprint)
        print("*** prompt_tokens=",prompt_tokens)
        print("*** completion_tokens=",completion_tokens,"\n")
        
        
        return response_content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# This function compares two responses and displays the differences in a table.
# Deletions are highlighted in red and additions are highlighted in green.
# If no differences are found, it prints "No differences found."


def compare_responses(previous_response: str, response: str):
    d = difflib.Differ()
    diff = d.compare(previous_response.splitlines(), response.splitlines())

    diff_table = ""
    diff_exists = False

    for line in diff:
        if line.startswith("- "):
            diff_table += f"{line}\n"
            diff_exists = True
        elif line.startswith("+ "):
            diff_table += f"{line}\n"
            diff_exists = True
        else:
            diff_table += f"{line}\n"

    if diff_exists:
        print(diff_table)
    else:
        print("No differences found.")

async def run1():
    topic = "a journey to Mars"
    system_message = "You are a helpful assistant that generates short stories."
    user_request = f"Generate a short story about {topic}."

    previous_response = await get_chat_response(system_message=system_message, user_request=user_request)

    response = await get_chat_response(system_message=system_message, user_request=user_request)

    # The function compare_responses is then called with the two responses as arguments.
    # This function will compare the two responses and display the differences in a table.
    # If no differences are found, it will print "No differences found."
    compare_responses(previous_response, response)

async def run2():
    topic = "a journey to Mars"
    system_message = "You are a helpful assistant that generates short stories."
    user_request = f"Generate a short story about {topic}."

    SEED=123

    previous_response = await get_chat_response(system_message=system_message, seed=SEED, user_request=user_request)

    response = await get_chat_response(system_message=system_message, seed=SEED, user_request=user_request)

    # The function compare_responses is then called with the two responses as arguments.
    # This function will compare the two responses and display the differences in a table.
    # If no differences are found, it will print "No differences found."
    compare_responses(previous_response, response)


print("***> Run <***")
#r=run1()
r=run2()
asyncio.run(r)