#Line and Word Counter 


def line_word_counter(path)->tuple:

    print(f"{path}")
    line_count=0
    words_count=0
    with open(path, "r") as f:
        for line in f:
            line_count+=1
            words_count+=len(line.split())

    return (line_count,words_count)

with open("day-04-python-foundations/diary.txt", "w") as f:
        f.write("Today I practiced file handling in Python.\nIt was easier than I expected.\nTomorrow: error handling and logging.")

count=line_word_counter("day-04-python-foundations/diary.txt")


print(f"The Total lines in file is :{count[0]} "
      f"The Total Words in file is :{count[1]}")


