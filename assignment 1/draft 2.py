#hand in one file called gamify.py (can resubmit)
#call all tests in ifname block but global variables initialized outside
#keep submitting before hte deadline
#write one function at a time
#NO SYNTAX ERRORS that will give 0
#document code (add comments):FOR FUNCTIONS do docstrings to describe parameters adn what function does. for GLOBAL VAR, describe what info variable stores and properties info has. help reader understand what code is doing.
#separate words with underscores
#choose good var names
#put a space blank betw operators
#each line less htan 80 char long, incl space and tabs
#docstrings: describe WHAT function does (not HOW it does it). describe parameter's purpose (and erefer to them by name). say if hte function returns or doesn't. explain conditions. be concise. use good grammar. write as a command -- e.g. 'return' rather than 'returns'

#encourage user to exercise by giving stars
#health points and fun points (hedons)
#a star increases number of hedons user gets from activity

#DONE: start with 0 hedons
#DONE: assume user is always running, carrying textbooks, or resting
#DONE: textbooks = 2hp/min
#DONE: resting = 0hedons/min
#DONE:running = 3hp/min for up to 180 mins; 1hp/min for every min over 180 mins
#DONE: #if not tired, running = 2hedon/min for first 10 mins of running, -2 hedons/min for every minute after first 10
#DONE: if not tired, carrying textbooks = 1hedon/min for first 20 mins, -1hedon/min for every minute after first 20
#DONE: resting and carrying textbooks =-2hedons/min if user is TIRED (finished running/carrying textbooks less than 2h before current activity) e.g. user tired if run for 2 mins then run again straight away
#^ and not using a star.
#STAR: additional 3hedons/min for at most ten mins. do NOT get hedons from star if do it more than 10 mins. assume no stars given for resting and two stars cannot be given at same time
#if three stars in the span of 2h, they will NOT get additional hedons from stars for hte rest of hte sim

def initialize():#initalizes all global vars in program
    global hedons
    global health_points
    global last_duration
    global last_activity
    last_duration = 0
    hedons = 0
    health_points = 0

def get_cur_hedons(): #return number of hedons
    global hedons
    print("hedons are: "+ str(hedons))

def get_cur_health(): #return HP
    global health_points
    print("health points are: " + str(health_points))


def perform_activity(activity, duration): #duration is positive int. if activity is NOT running, textbooks, or resting, running the function should have no effect
    global hedons
    global health_points
    global last_activity
    global last_duration
    if last_duration ==0:
        if activity == "resting":
            hedons = hedons + 0
            health_points = health_points + 0
            last_activity = activity
            last_duration = duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif activity == "running" and duration<=180: #gets 3hp for less than 180
            if duration <=10:
                hedons = hedons + duration*2
            else:
                hedons = hedons + 10*2 + (duration-10)*-2
            health_points = health_points + duration*3
            last_activity = activity
            last_duration = duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif activity == "running" and duration>180: #gets 560+whatever duration left for more than 180
            hedons = hedons + duration*2
            health_points = health_points + 180*3 + (duration-180)*1
            last_activity = activity
            last_duration = duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif activity == "carrying textbooks":
            if duration <=20:
                hedons = hedons + duration*1
            else:
                hedons = hedons + 10*2 + (duration-20)*-1
            health_points = health_points + duration*2
            last_activity = activity
            last_duration = duration
            return last_duration
            return last_activity
            return hedons
            return health_points
    elif last_duration <120 and (last_activity == "running" or last_activity == "carrying textbooks") :
        if activity == "running" and duration<=180: #gets 3hp for less than 180
            hedons = hedons + duration*-2
            health_points = health_points + duration*3
            last_activity = activity
            last_duration = duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif activity == "running" and duration>180: #gets 560+whatever duration left for more than 180
            hedons = hedons + duration*-2
            health_points = health_points + 180*3 + (duration-180)*1
            last_activity = activity
            last_duration = duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif activity == "carrying textbooks":
            hedons = hedons + duration*-2
            health_points = health_points + duration*2
            last_activity = activity
            last_duration = duration
            return last_duration
            return last_activity
            return hedons
            return health_points
    elif last_activity == "resting" and last_duration>=120:
        if activity == "resting":
            hedons = hedons + 0
            health_points = health_points + 0
            last_activity = activity
            last_duration = duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif activity == "running" and duration<=180: #gets 3hp for less than 180
            if duration <=10:
                hedons = hedons + duration*2
            else:
                hedons = hedons + 10*2 + (duration-10)*-2
            health_points = health_points + duration*3
            last_activity = activity
            last_duration = duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif activity == "running" and duration>180: #gets 560+whatever duration left for more than 180
            hedons = hedons + duration*2
            health_points = health_points + 180*3 + (duration-180)*1
            last_activity = activity
            last_duration = duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif activity == "carrying textbooks":
            if duration <=20:
                hedons = hedons + duration*1
            else:
                hedons = hedons + 10*2 + (duration-20)*-1
            health_points = health_points + duration*2
            last_activity = activity
            last_duration = duration
            return last_duration
            return last_activity
            return hedons
            return health_points
    else:
        print("please enter a valid activity")
def offer_star(activity): #offering star, and activity is string
    return 2
def star_can_be_taken(activity): #TRUE iff star can be used to get more hedons for an activity. star can only be taken if NO timie passed between star's offered and acrtivity and USER NOT BORED WITH STARS and STAR offered for "activity'
    return 3
def most_fun_activity_minute(): #returns one of activities which would give most hedons if person did it for ONE MINUTE at the current time
    return 4

if __name__=="__main__":
    initialize()
    perform_activity("running", 1)
    perform_activity("running", 2)
    get_cur_hedons()
    get_cur_health()