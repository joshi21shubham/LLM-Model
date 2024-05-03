import os
from openai import Completion

# Function to generate response using the OpenAI Completion API
def generate_response(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    completion = Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion.choices[0].text.strip()

# Function to ask a question and get user's response
def ask_question(question_text):
    print(generate_response(f"Doc Sage: {question_text}"))
    user_answer = input("User: ")
    return user_answer

# Function to ask the questionnaire
def ask_questionnaire():
    questions = [
        "How often do you feel restless or unable to sit still?",
        "How often do you worry excessively about various aspects of your life?",
        # Include all your questionnaire questions here
    ]

    all_user_answers = []
    for question in questions:
        user_answer = ask_question(question)
        all_user_answers.append(user_answer)

    return all_user_answers

# Function to analyze user's answers
def analyze_answers(answers):
    # Implement your analysis logic here
    # You can use the 'generate_response' function with a prompt 
    # that includes the user's answers to get potential diagnoses
    # and suggestions.
    diagnosis_prompt = f"A user provided the following answers to a mental health questionnaire: {answers}. Based on these answers, what are the potential mental health disorders and suggestions for the user?"
    diagnosis = generate_response(diagnosis_prompt)
    return diagnosis

# Function to provide support and resources based on diagnosis
def provide_support(diagnosis):
    support_prompt = f"Doc Sage: I understand this can be challenging. Based on the potential diagnosis of {diagnosis}, here are some ways I can support you and resources that might be helpful."
    support_message = generate_response(support_prompt)
    print(support_message)

# Set your API Key as an environment variable before running the script
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"  # Replace with your actual API Key

# Start of the conversation
print(generate_response("Your name is Doc Sage(male), a mental health therapist with an uplifting, motivating, empathic, and cheerful nature. Greet the user warmly."))

# Ask the questionnaire and analyze responses
all_user_answers = ask_questionnaire()
potential_diagnosis = analyze_answers(all_user_answers)
print(generate_response(f"Doc Sage: {potential_diagnosis}"))

# Provide support and resources
provide_support(potential_diagnosis)
