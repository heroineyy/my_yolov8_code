def Season1():
    print("Spring")
    # return "Spring"
def Season2():
    print("Summer")
    # return "Summer"
def Season3():
    print("Fall")
    return "Fall"
def Season4():
    print("Winter")
    return "Winter"
def Default():
    print("Invalid Season")
    return "Invalid Season"
seasondict = {
    Season1: Season1,
    Season2: Season2,
    Season3: Season3,
    Season4: Season4
}

def getSeason(season):

    fun = seasondict.get(season, Default)
    return fun()


getSeason(Season4)
