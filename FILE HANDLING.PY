# Write to file
with open("text.py","a") as f:    
    f.write("Hi im varsha")

# Read from file
with open("text.py","r") as f:
    content = f.read()

print(f"Content: {content}")     # Prints: Content: Hi im varsha
print(f"File closed: {f.closed}") # Prints: File closed: True