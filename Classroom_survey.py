# this is a list of question we are going to use. 
questions = [
    "Are lists part of Python data structure? ",
    "Are for loops and while loops the same? ",
    "Is .append, .join, .remove part of built-in function? "
]
# function to ask the user to ask the user their input 
def ask_questions():
    """Asks questions and collects responses"""
    # empty list 
    responses = []
    for question in questions:
        print("\n")
        # .lower is used to take the input of the user and turn it to lowercase
        answer = input(question).strip().lower()
        responses.append(answer)
        print(f"You answered: {answer}")
    #the response will be on a new line
    print("\nYour responses:")
    print(responses)
    return responses

def count_responses(responses):
    """Counts the occurrences of each response"""
#empty dictionary 
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
