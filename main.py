msg = input("> ")
words = msg.split(' ')
emojis = {
  ":)": "😋",
  ">:(": "🤬",
  ":(": "🥺"
}
output = "\n"
for word in words:
    output += emojis.get(word, word) + " "

print(output)