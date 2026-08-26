


words=['banana','kiwi','apple','fig']


alphabetical_words=sorted(words)
sorted_by_lenght=sorted(words,key=lambda x:len(x))
desending=sorted(words,key=lambda x:-len(x))

print(f'''List sorted alphabetically : {alphabetical_words}
list sorted by lenght : {sorted_by_lenght}
Descending lenght : {desending}''')