
questions = [
    "Are lists part of Python data structure? ",
    "Are for loops and while loops the same? ",
    "Is .append, .join, .remove part of built-in function? "
]

def ask_questions():
    """Asks questions and collects responses"""
    responses = []
    for question in questions:
        print("\n")
        answer = input(question).strip().lower()
        responses.append(answer)
        print(f"You answered: {answer}")
    
    print("\nYour responses:")
    print(responses)
    return responses

def count_responses(responses):
    """Counts the occurrences of each response"""
    answers = {}
    for response in responses:
        if response in answers:
            answers[response] += 1
        else:
            answers[response] = 1 
    return answers

# Ask questions and collect responses
responses = ask_questions()

# Count and print response occurrences
print("\nResponse counts:")
print(count_responses(responses))
