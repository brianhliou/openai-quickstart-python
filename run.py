import os

import openai
import argparse

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
    
def invoke_llm(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
    )

    return response.choices[0].text

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Process a prompt for the LLM.')
    parser.add_argument('prompt', type=str, help='The prompt to send to the LLM')

    # Parse the command line arguments
    args = parser.parse_args()

    # Invoke the LLM with the given prompt and get the response
    response = invoke_llm(args.prompt)

    # Print the response
    print(response)

if __name__ == "__main__":
    main()