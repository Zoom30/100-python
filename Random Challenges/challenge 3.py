# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

#     It must start with a hashtag (#).
#     All words must have their first letter capitalized.
#     If the final result is longer than 140 chars it must return false.
#     If the input or the result is an empty string it must return false.

# Examples

# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""

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


