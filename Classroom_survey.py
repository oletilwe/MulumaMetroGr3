#list of our questions to ask the user. 
questions = [
    "Are lists part of Python data structure? ",
    "Are for loops and while loops the same? ",
    "Is .append, .join, .remove part of built-in function? "
]
# Function to ask the user all of our questions.
def ask_questions():
    """Asks questions and collects responses"""
    #all their users answers would be stored in this list called response
    responses = []
    for question in questions:
        print("\n")
        # the answer will be turned to lowercase so that it can be counted later on. 
        # it will also strip all the white spaces 
        answer = input(question).strip().lower()
        responses.append(answer)
        print(f"You answered: {answer}")
    
    print("\nYour responses:")
    print(responses)
    return responses
# this function is to count the answers. 
def count_responses(responses):
    """Counts the occurrences of each response"""
    # the answers will be stored in here. 
    answers = {}
    for response in responses:
        # this for loop checks how many yes and no there are and displays it back to the user. 
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
