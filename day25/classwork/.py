def some_text():
    text=input("enter your message")

    upper_text=text.upper()
    print(f"ipper texts: {upper_text}")
    
    lower_text=text.lower()
    print(f"low texts: {lower_text}")


    lower_text=text.lower()
    print(f"low texts: {lower_text}")

    capitalized=text.capitalize()
    print(f"first big word: {capitalized}")

    find_word=input("find single word")
    index=text.find(find_word)
    if index !=-1:
        print(f"word '{find_word}' firstly is index: {index}")
    else:
         print(f"word '{find_word}' can not find.")




