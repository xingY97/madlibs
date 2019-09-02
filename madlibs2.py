def getKeys(formatString):
    keylist = list ()
    end = 0
    words = formatString.count('{')
    for i in range (words):
        start = formatString.find('{', end) + 1
        end = formatString.find('}', start)
        key = formatString[start : end]
        keylist.append(key)
    return set(keylist) #set removes duplicates

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
def main (): #https://www.pinterest.com/pin/375839531387234463 story found here.
    story = """ Pizza was invented by a {adjective} {nationality} chef named {name}. To make a pizza, you need to take a lump of {noun}, and make a thin, round {adjective}{noun}. Then you cover it with {adjective} sauce, {adjective} cheese, and fresh chopped {plural_noun}. Next you have to bake it in a very hot {noun}. When it is done, cut it into {number} {shapeds}. some kids like {food} pizza. If I could, I would eat pizza {number} times a day. """

    tellStory(story)
    print("come back Soon!")

main()



