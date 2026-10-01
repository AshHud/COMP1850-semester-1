"""Advanced Task 3: Clean Message Toolkit
- Collect a message that might contain extra spaces or mixed casing.
- Use at least three different string methods (e.g. strip, title, replace, upper) to tidy the message.
- Print the original and cleaned versions so the difference is obvious.
- Extension: show the message length before and after cleaning.
"""

raw_message = input("Type a message to tidy: ")
rawlength = len(raw_message)

changed_message = raw_message.strip()
changed_message = changed_message.lower()
changed_message = changed_message.capitalize()
changedlength = len(changed_message)

print(f"The original message was: {raw_message}, which was {rawlength} characters long")
print(f"The new message is: {changed_message}, which was {changedlength} characters long")

# TODO: apply a sequence of string methods to produce a cleaned_message
# Example methods: strip, title, replace, lower, upper
# TODO: display the original and cleaned messages
# Extension: display the character counts for each version
