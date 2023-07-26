import os
import requests

BASE_DIR = "D:/anime"
GPT_API_URL = "https://api.openai.com/v1/engines/davinci-codex/completions"
ANIDB_API_URL = "https://api.anidb.net/v1/anime"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('GPT_API_KEY')}",
}

def send_to_chat_gpt_batch(directory_names):
    data = {
        "model": "text-davinci-004",
        "messages": [
            {
                "role": "system",
                "content": "Translate these anime names into English and Japanese."
            },
            {
                "role": "user",
                "content": "\n".join(directory_names)
            }
        ]
    }
    response = requests.post(GPT_API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip().split('\n')

def fetch_anidb_id(english_name):
    params = {"filter": english_name}
    response = requests.get(ANIDB_API_URL, params=params)
    response.raise_for_status()
    return response.json()["data"]["id"]

def format_directory_name(original_name, english_name, japanese_name, anidb_id):
    return f"{original_name} ({english_name}, {japanese_name}) [anidb={anidb_id}]"

def process_directories_batch():
    directory_names = os.listdir(BASE_DIR)
    full_names_batch = send_to_chat_gpt_batch(directory_names)

    for i in range(len(directory_names)):
        english_name, japanese_name = full_names_batch[i].split(', ')
        anidb_id = fetch_anidb_id(english_name)
        formatted_name = format_directory_name(directory_names[i], english_name, japanese_name, anidb_id)
        print(f"Original Name: {directory_names[i]}\nFormatted Name: {formatted_name}\n")

if __name__ == "__main__":
    process_directories_batch()
