import os
from datetime import datetime  # Import datetime for timestamp
from dotenv import load_dotenv  # Import dotenv for loading environment variables
from openai import OpenAI
from utils.file_io import write_file  # Import the write_file utility

def call_llm(prompt):
    # Load environment variables from .env file
    load_dotenv()
    
    # Get API key from environment variables
    api_key = os.environ.get('OPENAI_API_KEY')
    
    if not api_key:
        raise ValueError("OpenAI API key not found in environment variables")
    
    client = OpenAI(api_key=api_key)
    r = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    response = r.choices[0].message.content
    
    # Get the current date and time for the log filenames
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Ensure the logs directory exists
    log_directory = "logs"
    os.makedirs(log_directory, exist_ok=True)  # Create logs directory if it doesn't exist
    
    # Create log file paths with timestamp
    prompt_log_file_path = os.path.join(log_directory, f"{timestamp}_prompt.log")
    response_log_file_path = os.path.join(log_directory, f"{timestamp}_response.log")
    
    # Use the write_file utility to save the prompt and response
    write_file(prompt_log_file_path, prompt + "\n")  # Save the prompt
    write_file(response_log_file_path, response + "\n")  # Save the response
    
    return response

if __name__ == "__main__":
    prompt = "What is the meaning of life?"
    call_llm(prompt)  # Call the function without printing
