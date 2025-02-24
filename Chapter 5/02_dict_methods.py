marks = {
    "Jordan": 100,
    "Alex": 56,
    "Charlotte": 23,
    0: "Reiner",
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 99, "Renuka": 100})
# print(marks)

print(marks.get("Jordan2")) # Prints None
print(marks["Jordan2"]) # Returns an error