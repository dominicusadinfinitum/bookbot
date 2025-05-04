

def count_words(text):
    return len(text.split())

def count_letters(text):
    converted=text.lower()
    letters={}
    for char in converted:
        if char in letters:
            letters[char]+=1
        else:
            letters[char]=1
    return letters

def sort_on(dict):
    return dict["num"]

def sorted_letters(letters: dict[chr,int])-> list[dict[str, any]]:
    list=[]
    for letter in letters:
        temp={}
        temp["char"]=letter
        temp["num"]=letters[letter]
        list.append(temp)
    list.sort(reverse=True, key=sort_on)
    return list
