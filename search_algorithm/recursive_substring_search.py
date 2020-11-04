def match(text, pat, text_index, pat_index):
    if pat_index == len(pat):
        return 1
    
    if text_index == len(text):
        return 0

    if text[text_index] == pat[pat_index]:
        return match(text , pat, text_index + 1, pat_index+1)

    return 0


def contains(text, pat, text_index, pat_index):
    if len(text) == text_index:
        return 0

    if text[text_index] == pat[pat_index]:
        if match(text, pat, text_index+1, pat_index+1):
            return 1
    return contains(text, pat, text_index+1, pat_index)

print(contains("geeksforgeeks", "geeks", 0, 0)) 
print(contains("geeksforgeeks", "geeksquiz", 0, 0)) 
print(contains("geeksquizgeeks", "quiz", 0, 0)) 
