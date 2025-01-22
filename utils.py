def get_queries_as_list(s):
    results = []
    switch = False
    word = ""
    for char in s:
        if char =="\"":
            switch = not switch
            continue
        if switch == True:
            word += char
        if switch == False and len(word)>0:
            results.append(word)
            word = ""
    print(results)
    return results

#get_last_row_as_list(
#''' 
# Sure! Here are the search queries extracted from the given string:
#
#"SpaceX frozen valve issue update," "Starship launch timeline May 1st," "Valve issue impact on Starship liftoff"
#'''
#)

def get_ranking(s):
    idx = s.find("Rating:")
    # return first digit found in ranking output from LLM
    for char in s[idx:idx+15]:
        if char.isdigit():
            return int(char)