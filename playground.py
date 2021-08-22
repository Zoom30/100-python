def generate_hashtag(s):
    #your code here
    hash_tag = []
    there_is_space = False
    if len(s) == 0 or len(s) > 140:
        return False
    else:
        for i in range(0, len(s)):
            if i == 0:
                hash_tag.append(s[i].upper())
            elif s[i] == " ":
                there_is_space = True
            elif there_is_space == True and s[i] != " ":
                hash_tag.append(s[i].upper())
                there_is_space = False
            else:
                if s[i] == s[i].upper():
                    hash_tag.append(s[i].lower())
                else:
                    hash_tag.append(s[i])
        text = "".join(hash_tag)
        return f"#{text}"

print(generate_hashtag("CodeWars is nice"))