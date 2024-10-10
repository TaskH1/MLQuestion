from transformers import pipeline
import os

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

def evaluate_answer_with_llm(submitted_answer, correct_answer):
    # Define a prompt to compare the user's answer with the correct answer
    prompt = (
        f"Evaluate the following user answer compared to the correct answer \n"
        f"Correct Answer: {correct_answer}\n"
        f"User Answer: {submitted_answer}\n"
        f"Determin if the user's answer is correct or not, and explain why."
        f"Provide feedback on the user's response, highlighting what is correct or how it could be improved."
    )

    # Generate the response using the Hugging Face model
    response = generator(prompt, max_length=200, num_return_sequences=1, do_sample=True)

    # Extract the generated text from the response
    feedback = response[0]['generated_text']

    # Determin correctness based on the feedback
    is_correct = "correct" in feedback.lower() and "not correct" not in feedback.lower()

    return is_correct, feedback
