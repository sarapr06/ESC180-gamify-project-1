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
    global star
    global star_count
    global star_run
    global star_textbook
    global star_rest
    global total_duration
    total_duration = 0
    star_count = 2
    star = True
    star_rest = False
    star_run = False
    star_textbook = False
    last_duration = 0
    hedons = 0
    health_points = 0
    return star_run
    return star_textbook

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
    global star
    global star_count
    global star_rest
    global star_run
    global star_textbook
    global total_duration
    global star_cooldown

    if star_run and activity == "running":
        if last_duration == 0:
            if duration <=180:
                if duration <=10:
                    hedons = hedons + duration*5
                else:
                    hedons = hedons + 10*5 + (duration-10)*-2
                health_points = health_points + duration*3
                last_activity = activity
                last_duration = duration
                total_duration = total_duration+duration
                star_run = False
                return star_run
                return total_duration
                return last_duration
                return last_activity
                return hedons
                return health_points
            else:
                if duration <=10:
                    hedons = hedons + duration*5
                else:
                    hedons = hedons + 10*5 + (duration-10)*-2
                health_points = health_points + 180*3 + (duration-180)*1
                last_activity = activity
                last_duration = duration
                total_duration = total_duration+duration
                star_run = False
                return star_run
                return total_duration
                return last_duration
                return last_activity
                return hedons
                return health_points
        elif last_duration <120 and (last_activity == "running" or last_activity == "carrying textbooks") :
            if duration<=180: #gets 3hp for less than 180
                if duration <=10:
                    hedons = hedons + duration*5
                else:
                    hedons = hedons + 10*5 + duration*-2
                health_points = health_points + duration*3
                last_activity = activity
                last_duration = duration
                total_duration = total_duration+duration
                star_run = False
                return star_run
                return total_duration
                return last_duration
                return last_activity
                return hedons
                return health_points
            elif duration>180: #gets 560+whatever duration left for more than 180
                if duration <=10:
                    hedons = hedons + duration*5
                else:
                    hedons = hedons + 10*5 + (duration-10)*-2
                health_points = health_points + 180*3 + (duration-180)*1
                last_activity = activity
                last_duration = duration
                total_duration = total_duration+duration
                star_run = False
                return star_run
                return total_duration
                return last_duration
                return last_activity
                return hedons
                return health_points
        elif last_activity == "resting" and last_duration>=120:
            if duration<=180: #gets 3hp for less than 180
                if duration <=10:
                    hedons = hedons + duration*5
                else:
                    hedons = hedons + 10*5 + (duration-10)*-2
                health_points = health_points + duration*3
                last_activity = activity
                last_duration = duration
                total_duration = total_duration+duration
                star_run = False
                return star_run
                return total_duration
                return last_duration
                return last_activity
                return hedons
                return health_points
            elif activity == "running" and duration>180: #gets 560+whatever duration left for more than 180
                if duration <=10:
                    hedons = hedons + duration*5
                else:
                    hedons = hedons + 10*5 + (duration-10)*-2
                health_points = health_points + 180*3 + (duration-180)*1
                last_activity = activity
                last_duration = duration
                total_duration = total_duration+duration
                star_run = False
                return star_run
                return total_duration
                return last_duration
                return last_activity
                return hedons
                return health_points
    elif star_textbook and activity == "carrying textbooks":
        if last_duration ==0:
            if duration <=20:
                hedons = hedons + duration*1
            else:
                hedons = hedons + 10*2 + (duration-20)*-1
            health_points = health_points + duration*2
            last_activity = activity
            last_duration = duration
            total_duration = total_duration+duration
            star_textbook = False
            return star_textbook
            return total_duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif last_duration <120 and (last_activity == "running" or last_activity == "carrying textbooks") :
            hedons = hedons + duration*-2
            health_points = health_points + duration*2
            last_activity = activity
            last_duration = duration
            total_duration = total_duration+duration
            star_textbook = False
            return star_textbook
            return total_duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif last_activity == "resting" and last_duration>=120:
            if duration <=20:
                hedons = hedons + duration*1
            else:
                hedons = hedons + 10*2 + (duration-20)*-1
            health_points = health_points + duration*2
            last_activity = activity
            last_duration = duration
            total_duration = total_duration+duration
            star_textbook = False
            return star_textbook
            return total_duration
            return last_duration
            return last_activity
            return hedons
            return health_points


    if last_duration ==0:
        if activity == "resting":
            hedons = hedons + 0
            health_points = health_points + 0
            last_activity = activity
            last_duration = duration
            total_duration = total_duration+duration
            return total_duration
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
            total_duration = total_duration+duration
            return total_duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif activity == "running" and duration>180: #gets 560+whatever duration left for more than 180
            if duration <=10:
                hedons = hedons + duration*2
            else:
                hedons = hedons + 10*2 + (duration-10)*-2
            health_points = health_points + 180*3 + (duration-180)*1
            last_activity = activity
            last_duration = duration
            total_duration = total_duration+duration
            return total_duration
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
            total_duration = total_duration+duration
            return total_duration
            return last_duration
            return last_activity
            return hedons
            return health_points
    elif last_duration <120 and (last_activity == "running" or last_activity == "carrying textbooks") :
        if  activity == "resting":
            hedons = hedons + 0
            health_points = health_points + 0
            last_activity = activity
            last_duration = duration
            total_duration = total_duration+duration
            return total_duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif activity == "running" and duration<=180: #gets 3hp for less than 180
            hedons = hedons + duration*-2
            health_points = health_points + duration*3
            last_activity = activity
            last_duration = duration
            total_duration = total_duration+duration
            return total_duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif activity == "running" and duration>180: #gets 560+whatever duration left for more than 180
            hedons = hedons + duration*-2
            health_points = health_points + 180*3 + (duration-180)*1
            last_activity = activity
            last_duration = duration
            total_duration = total_duration+duration
            return total_duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif activity == "carrying textbooks":
            hedons = hedons + duration*-2
            health_points = health_points + duration*2
            last_activity = activity
            last_duration = duration
            total_duration = total_duration+duration
            return total_duration
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
            total_duration = total_duration+duration
            return total_duration
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
            total_duration = total_duration+duration
            return total_duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif activity == "running" and duration>180: #gets 560+whatever duration left for more than 180
            if duration <=10:
                hedons = hedons + duration*2
            else:
                hedons = hedons + 10*2 + (duration-10)*-2
            health_points = health_points + 180*3 + (duration-180)*1
            last_activity = activity
            last_duration = duration
            total_duration = total_duration+duration
            return total_duration
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
            total_duration = total_duration+duration
            return total_duration
            return last_duration
            return last_activity
            return hedons
            return health_points
    else:
        print("please enter a valid activity")
def offer_star(activity): #offering star, and activity is string
    global star
    global star_count
    global star_run
    global star_rest
    global star_textbooks
    global star_cooldown
    if activity == "running":
        star_run = star
        star_count = star_count -1
        star_cooldown= 0
        return star_cooldown
        return star_count
        return star_run
    elif activity == "textbooks":
        star_textbooks = star
        star_count = star_count -1
        star_cooldown= 0
        return star_cooldown
        return star_count
        return star_textbooks
    elif activity == "rest":
        star_rest = star
        star_count = star_count -1
        star_cooldown= 0
        return star_cooldown
        return star_count
        return star_rest
    else:
        print("please enter a valid activity to get a star")
def star_can_be_taken(activity): #TRUE iff star can be used to get more hedons for an activity. star can only be taken if NO timie passed between star's offered and acrtivity and USER NOT BORED WITH STARS and STAR offered for "activity'
    return 3
def most_fun_activity_minute(): #returns one of activities which would give most hedons if person did it for ONE MINUTE at the current time
    return 4

if __name__=="__main__":
    initialize()
    perform_activity("running", 30)
    get_cur_hedons() # -20 = 10 * 2 + 20 * (-2)
    get_cur_health() # 90 = 30 * 3
    perform_activity("resting", 30)
    offer_star("running")
    perform_activity("textbooks", 30)
    get_cur_health() # 150 = 90 + 30*2
    get_cur_hedons() # -80 = -20 + 30 * (-2)
    offer_star("running")
    perform_activity("running", 20)
    get_cur_health() # 210 = 150 + 20 * 3
    get_cur_hedons() # -90 = -80 + 10 * (3-2) + 10 * (-2)
    perform_activity("running", 170)
    get_cur_health() # 700 = 210 + 160 * 3 + 10 * 1
    get_cur_hedons() # -430 = -90 + 170 * (-2)