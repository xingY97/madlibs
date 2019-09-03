
"""as refrence, I used this tutorial http://anh.cs.luc.edu/handsonPythonTutorial/madlib2.html"""

def main (): #https://www.pinterest.com/pin/375839531387234463 story found here.
    story = """ \033[42m Pizza was invented by a \033[0;32m{adjective} \033[0;34m {nationality} chef named {name}. To make a pizza, you need to take a lump of \033[0;37m {noun}, and make a thin, round \033[4;33m{adjective} \033[4;33m{noun}. Then you cover it with \033[0;31m{adjective} sauce, \033[0;35m {adjective} cheese, and fresh chopped \033[1;31m{plural_noun}. Next you have to bake it in a very hot {noun}. When it is done, cut it into {number} {shapes}. some kids like {food} pizza. If I could, I would eat pizza {number} times a day. """

    tellStory(story)
    print("come back Soon!")
def getKeys(user_input):
    keylist = list ()
    end = 0
    words = user_input.count('{')
    for i in range (words):
        start = user_input.find('{', end) + 1
        end = user_input.find('}', start)
        key = user_input[start : end]
        keylist.append(key)

    return (keylist)

def addPicks(cue, dictionary): # "Enter a specific example for {name}: "
    user_input = "Enter a {name} : "
    prompt = user_input.format(name=cue)
    response = input(prompt)
    dictionary[cue] = response

def getUserPicks(cues):
    userPicks = dict()
    for cue in cues:
        addPicks(cue,userPicks)
    return userPicks
def tellStory(storyFormat):
    cues = getKeys(storyFormat)
    userPicks = getUserPicks(cues)
    story = storyFormat.format(**userPicks)
    print(story) 


main()



