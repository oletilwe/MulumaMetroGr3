Question = ["Are lists part of python data structure?", 
            "Are for loops and while loops the same? ",
            "is .append, .join, .remove part of built-in function" 
            ]


def Question_to_ask():
    response = []
    for item in Question:
        #The range asks how many questions are there and the loop will work with the number
        print("\n" * 2)
        # print("These are Yes or No Question!!!!!")
        answer = input(item + " "+ "")
        response.append(answer)
        print(answer)

    print(response)

# Count and print response occurrences
print("\nResponse counts:")
print(count_responses(responses))
