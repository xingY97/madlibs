
def mad_libs ():
    story = "pizza was invented by a {adjective} {country} chef named {name}"
    list = {}
    list["adjective"] = input ("Enter a adjejctive: ")
    list["country"] = input ("Enter a country")
    list["name"] = input ("Enter a name")

    print (story)


def story():
    template = "Didn't you hear? %(noun)-%(verb)sing %(noun)s are the new %(color)s"
    dictionary = {}
    dictionary["noun"] = raw_input("Enter a noun: ")
    dictionary["verb"] = raw_input("Enter a -ing verb: ")
    dictionary["color"] = raw_input("Enter a color: ")
    print (template % dictionary)