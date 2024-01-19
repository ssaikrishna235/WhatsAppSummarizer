import openai
import pandas as pd
from datasets import Dataset, train_test_split

api_key = "YOUR_API_KEY_HERE"

def split_conversations(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        conversations = file.read().split("********************************")
    return [conversation.strip() for conversation in conversations if conversation.strip()]

file_path = 'conversations.txt'
conversation_texts = split_conversations(file_path)

data_points = []

for idx, conversation_text in enumerate(conversation_texts, start=1):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=conversation_text,
        max_tokens=50,
        api_key=api_key
    )

    summary = response.choices[0].text

    data_point = {
        "id": idx,
        "dialogue": conversation_text,
        "summary": summary
    }

    data_points.append(data_point)

df = pd.DataFrame(data_points)

train_percentage = 0.7
test_percentage = 0.15
validation_percentage = 0.15

train_dataset, test_dataset, validation_dataset = train_test_split(
    df, test_size=test_percentage + validation_percentage, train_size=train_percentage, shuffle=True
)

dataset_dict = {
    "train": train_dataset,
    "test": test_dataset,
    "validation": validation_dataset
}

dataset_path = "/content/whatsapp_data_and_hotel_conv_data/"
Dataset.from_dict(dataset_dict).save_to_disk(dataset_path)
