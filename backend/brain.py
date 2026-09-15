def chinky_brain(message):
    return {
        "reply": "You Said " + message + " "
    }
message = input("Ask Anythig..... ->")
response = chinky_brain(message)
print(response)