# WhatsApp Chat Summarizer

The **WhatsApp Chat Summarizer** is a tool designed to summarize entire conversations. It was created by combining data from existing WhatsApp web scrapers and additional conversational data, including hotel conversations, to create a dataset of approximately 10,000 conversations. The primary purpose of this tool is to summarize text-based conversations efficiently.

## Data Collection

To build the dataset, we employed an existing WhatsApp web scraper to gather chat data. However, the quantity of cleaned chats was limited. To address this, we supplemented the dataset with conversational data from various sources, including hotel conversations. This approach allowed us to create a more substantial and diverse dataset for training and evaluation.

## Summarization Using OpenAI ChatGPT

We used OpenAI's ChatGPT model for conversation summarization. This model has been fine-tuned using LLMa2 (Language Model with Multimodal Abilities 2) and the PEFT (Pseudo-Efficient Fine-Tuning) technique. Additionally, we incorporated elements of the QLOra technique, specifically fine-tuning only select modules of the LLMa model. These modules include queries, values, and keys of the attention model with 4-bit quantization.
