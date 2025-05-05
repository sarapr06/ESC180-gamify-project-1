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

#if three stars in the span of 2h, they will NOT get additional hedons from stars for hte rest of hte sim

def initialize():#initalizes all global vars in program
    global hedons
    global health_points
    global last_duration
    global last_activity
    global star
    global star_count
    global star_run
    global star_textbooks
    global star_rest
    global star_bonus
    global total_duration
    global star_cooldown
    global tired
    global cooldown
    global run_count
    global text_count
    star_cooldown = 0
    text_count = 0
    run_count = 0
    cooldown = 0
    tired = False
    last_activity = "n/a"
    total_duration = 0
    star_count = 2
    star = True
    star_rest = False
    star_run = False
    star_textbooks = False
    last_duration = 0
    hedons = 0
    star_bonus =0
    health_points = 0

def get_cur_hedons(): #return number of hedons
    global hedons
    return "hedons are: "+ str(hedons)

def get_cur_health(): #return HP
    global health_points
    return "health points are: " + str(health_points)


def perform_activity(activity, duration): #duration is positive int. if activity is NOT running, textbooks, or resting, running the function should have no effect
    global hedons
    global health_points
    global last_activity
    global last_duration
    global star
    global star_cooldown
    global star_count
    global star_rest
    global star_run
    global star_textbooks
    global total_duration
    global star_bonus
    global tired
    global run_count
    global text_count
    global cooldown
    total_duration = total_duration + duration
    cooldown = cooldown + duration
    if not activity == "resting":
        cooldown = 0


    if (last_activity == "resting" and cooldown>=120) or last_activity == "n/a":
        tired = False
    else:
        tired = True
        cooldown = 0
    # elif ((last_duration <120 and last_activity == "resting") or (not last_activity == "resting" and not activity == "resting")) and not total_duration%120==0:
    #     tired = True

    if activity == "running":
        run_count=run_count + duration
        text_count = 0
    elif activity == "textbooks":
        text_count=text_count + duration
        run_count = 0


    if star_count <2:
        star_cooldown = star_cooldown + duration
        if star_cooldown < 120 and star_count < 0:
            star_textbooks = False
            star_run = False
        elif star_cooldown >120:
            star_count = 2

    if star_run and activity == "running":
        star_bonus = 3
        star_run == False
    elif star_textbooks and activity == "textbooks":
        star_bonus = 3
        star_textbooks == False
    else:
        star_bonus = 0

    if activity == "resting":
        hedons = hedons + 0
        health_points = health_points + 0
        last_activity = activity
        last_duration = duration
        total_duration = total_duration+ duration
        return total_duration
    if not tired:
        if activity == "running":
            if run_count <180:
                health_points = health_points + duration*3
            elif run_count>180:
                health_points = health_points + 180*3 + (run_count-180)*1
            if duration <=10:
                hedons = hedons + duration*(2+star_bonus)
            else:
                hedons = hedons + 10*(2+star_bonus) + (duration-10)*-2
            last_activity = activity
            last_duration = duration
            star_run = False
            tired = True
            return total_duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif activity == "textbooks":
            if duration <=20:
                if duration <= 10:
                    hedons = hedons + duration*(1+star_bonus)
                else:
                    hedons = hedons + 10*(1+star_bonus)+ (duration-10)*1
            else:
                hedons = hedons + 10*(2+star_bonus) + (duration-20)*-1
            health_points = health_points + duration*2
            last_activity = activity
            last_duration = duration
            star_textbooks = False
            tired = True
            return total_duration
            return last_duration
            return last_activity
            return hedons
            return health_points
    elif tired:
        if activity == "running":
            if run_count <180: #gets 3hp for less than 180
                health_points = health_points + duration*3
            elif run_count >= 180:
                health_points = health_points + 180*3 + (run_count-180)*1
            if duration <= 10:
                hedons = hedons + duration*(-2 + star_bonus)
            elif duration >10:
                hedons = hedons + 10*(-2 + star_bonus) + (duration-10)*(-2)
            last_activity = activity
            last_duration = duration
            star_run = False
            return total_duration
            return last_duration
            return last_activity
            return hedons
            return health_points
        elif activity == "textbooks":
            if duration <=10:
                hedons = hedons + duration*(-2 + star_bonus)
            elif duration >10:
                hedons = hedons + 10*(-2 + star_bonus) + (duration-10)*(-2)
            health_points = health_points + duration*2
            last_activity = activity
            last_duration = text_count
            star_textbooks = False
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
    elif activity == "textbooks":
        star_textbooks = star
        star_count = star_count -1
    elif activity == "rest":
        star_rest = star
        star_count = star_count -1
    else:
        print("please enter a valid activity to get a star")
def star_can_be_taken(activity):
    if star_run == True and activity == "running" and star_count>=0:
        print("True")
    elif star_textbooks == True and activity == "textbooks" and star_count>=0:
        print("True")
    else:
        print("False")
def most_fun_activity_minute():
    if star_run and not tired:
        return "running"
    elif star_textbooks and not tired:
        return "textbook"
    elif star_run:
        return "running"
    elif not tired:
        return "running"
    elif tired:
        return "resting"
    ##CHECK PLEASE

if __name__=="__main__":
    initialize()
    perform_activity("running", 150)
    perform_activity("textbooks", 1)
    perform_activity("running", 50)
    print(get_cur_health())