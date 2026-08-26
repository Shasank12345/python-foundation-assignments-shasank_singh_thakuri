

words=['shasank','bad','haha','ram']


word_dictionary={len(word):word for index ,word in enumerate(words) if len(word)>3}

print(f"Required Dictionary : {word_dictionary}")