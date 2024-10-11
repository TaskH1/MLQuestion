from transformers import BertTokenizer, BertModel, AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import os
import numpy as np

huggingface_token = "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"
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_sentence_embedding(sentence):
    # Tokenize the input sentence and convert to tensor
    inputs = tokenizer(sentence, return_tensors='pt', padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    # Get the last hidden state tensor (shape: [batch_size, sequence_length, hidden_size])
    last_hidden_state = outputs.last_hidden_state
    # Average the token embeddings to get the sentence embedding
    sentence_embedding = last_hidden_state.mean(dim=1).squeeze()
    return sentence_embedding

def evaluate_answer_with_bert(submitted_answer, correct_answer):
    # Get the embeddings for both submitted_answer and correct_answer
    submitted_embedding = get_sentence_embedding(submitted_answer)
    correct_embedding = get_sentence_embedding(correct_answer)

    # Reshape embeddings for cosine similarity caluculation
    submitted_embedding = submitted_embedding.detach().cpu().numpy().reshape(1, -1)
    correct_embedding = correct_embedding.detach().cpu().numpy().reshape(1, -1)

    # Calculate similarity score
    similarity_score = cosine_similarity(submitted_embedding, correct_embedding)

    # Determine if the answer is correct based on a threshold
    threshold = 0.75
    is_correct = similarity_score >= threshold

    # Generate feedback based on the similarity score
    feedback = f"The similarity score is {similarity_score.item():.2f}."
    feedback += "Your answer is correct." if is_correct else "Your answer could be improved. Please review the key points."

    return is_correct, feedback


# def evaluate_answer_basic(submitted_answer, correct_answer):
#     keywords = correct_answer.lower().split()
#     submitted = submitted_answer.lower()


#     is_correct = all(keyword in submitted for keyword in keywords)
#     feedback = "Your answer is correct." if is_correct else "Your answer could be improved, Please review the key points."

#     return is_correct, feedback

# huggingface_token = os.getenv("HUGGINGFACE_API_TOKEN")

# model_name = "meta-llama/Meta-Llama-Guard-2-8B"
# # Load the tokenizer associated with model
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# # Load the Language model itself
# model = AutoModelForCausalLM.from_pretrained(model_name)

# def evaluate_answer_with_llm(submitted_answer, correct_answer):
#     # Define a prompt to compare the user's answer with the correct answer
#     prompt = (
#         f"You are a knowledgeable teacher evaluating student answers. "
#         f"Please provide detailed feedback on the following user's answer compared to the correct answer.\n"
#         f"Correct Answer: {correct_answer}\n"
#         f"User Answer: {submitted_answer}\n"
#         f"Evaluate if the user's answer is correct, and explain why. "
#         f"Also, provide suggestions for improvement if there are any mistakes."
#     )

#     # Tokenize the input prompt
#     inputs = tokenizer(prompt, return_tensors="pt")

#     # Generate the response using the model
#     outputs = model.generate(**inputs, max_length=200, do_sample=True)

#     feedback = tokenizer.decode(outputs[0], skip_special_tokens=True)

#     is_correct = "correct" in feedback.lower()

#     return feedback, is_correct