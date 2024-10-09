import openai
import os

openai.api_key = os.getenv("OPEN_API_KEY")

def evaluate_answer_with_llm(submitted_answer, correct_answer):
    # Define a prompt to compare the user's answer with the correct answer
    prompt = (
        f"Evaluate the following user answer compared to the correct answer \n"
        f"Correct Answer: {correct_answer}\n"
        f"User Answer: {submitted_answer}\n"
        f"Determin if the user's answer is correct or not, and explain why."
        f"Provide feedback on the user's response, highlighting what is correct or how it could be improved."
    )

    
    # Call the OpenAI API to get the evaluation
    response = openai.Completion.create(
        # specify the language model
        engine="text-davinci-003",
        prompt=prompt,
        # 1 token roughly corresponds to 0.75 words in English
        max_tokens=500,
        # controls the randomness of the model's output, determining how creative the model should be.
        temperature=0.5
    )

    # Extract the feedback from the response
    feedback = response.choices[0].text.strip()

   # Determin correctness based on the feedback
   is_correct = "correct" in feedback.lower() and "not correct" not in feedback.lower()

   return is_correct, feedback
