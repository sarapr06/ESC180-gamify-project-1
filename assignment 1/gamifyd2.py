#hand in one file called gamify.py (can resubmit)
#document code (add comments):FOR FUNCTIONS do docstrings to describe parameters adn what function does. for GLOBAL VAR, describe what info variable stores and properties info has. help reader understand what code is doing.
#separate words with underscores
#choose good var names
#put a space blank betw operators
#each line less htan 80 char long, incl space and tabs
#docstrings: describe WHAT function does (not HOW it does it). describe parameter's purpose (and erefer to them by name). say if hte function returns or doesn't. explain conditions. be concise. use good grammar. write as a command -- e.g. 'return' rather than 'returns'

def initialize():#initalizes all global vars in program
    global hedons
    global health_points
    global last_duration
    global last_activity
    global star
    global star_count
    global star_run
    global star_textbooks
    global star_bonus
    global star_cooldown
    global tired
    global cooldown
    global run_count
    global bored
    global num_run
    num_run = 0
    bored = False
    star_cooldown = 0
    run_count = 0
    cooldown = 0
    tired = False
    last_activity = "n/a"
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
    return hedons

def get_cur_health(): #return HP
    global health_points
    return health_points


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
    global star_bonus
    global tired
    global run_count
    global cooldown
    global bored
    global num_run

    if activity == "resting":
        cooldown = cooldown + duration
        star_run = False
        star_textbooks = False
    elif last_activity == "running" or last_activity=="textbooks":
        cooldown = 0

    if not (activity == "running" or activity == "textbooks" or activity == "resting"):
        print("please enter either running, textbooks, or resting")



    if ((last_activity == "resting" or activity == "resting") and cooldown>=120) or last_activity == "n/a" or activity == "resting":
        tired = False
    else:
        tired = True
        cooldown = 0
    # elif ((last_duration <120 and last_activity == "resting") or (not last_activity == "resting" and not activity == "resting")) and not total_duration%120==0:
    #     tired = True

    if last_activity == "resting":
        run_count = 0
    if activity == "running":
        run_count=run_count + duration
    elif activity == "textbooks":
        run_count = 0


    if star_count == 2:
        star_cooldown = 0
    elif star_count <0:
        if star_cooldown>=120:
            star_count = 1
            star_cooldown = 0
        elif star_cooldown < 120:
            star_textbooks = False
            star_run = False
            bored = True
    elif star_count <2:
        star_cooldown = star_cooldown + duration
        if star_cooldown>=120:
            star_count = 2
            star_cooldown = 0
        elif star_cooldown < 120 and star_count <0:
            star_textbooks = False
            star_run = False
            bored = True
    if bored == True:
        star_textbooks = False
        star_run = False

    if activity == "running":
        num_run = num_run + 1
    elif not activity == "running":
        num_run = 0

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
        run_count = 0
        return hedons
    if not tired:
        if activity == "running":
            if run_count <=180:
                health_points = health_points + (duration)*3
            elif run_count>180:
                health_points = health_points + 180*3 + (run_count-180)*1 - (run_count-duration)*180

            if duration <=10:
                hedons = hedons + duration*(2+star_bonus)
            else:
                hedons = hedons + 10*(2+star_bonus) + (duration-10)*-2
            last_activity = activity
            last_duration = duration
            star_run = False
            tired = True
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
            elif duration>20:
                hedons = hedons + 20*(1+star_bonus) + (duration-20)*-1
            health_points = health_points + duration*2
            last_activity = activity
            last_duration = duration
            star_textbooks = False
            tired = True
            return last_duration
            return last_activity
            return hedons
            return health_points
    elif tired:
        if activity == "running":
            if run_count <=180:
                health_points = health_points + (duration)*3
            elif run_count>180:
                if num_run <=3:
                    health_points = health_points + 180*3 + (run_count-180)*1 - (run_count-duration)*3
                elif num_run >3:
                    health_points = health_points + (run_count-180) - (run_count-180-duration)
            if duration <= 10:
                hedons = hedons + duration*(-2 + star_bonus)
            elif duration >10:
                hedons = hedons + 10*(-2 + star_bonus) + (duration-10)*(-2)
            last_activity = activity
            last_duration = duration
            star_run = False
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
            star_textbooks = False
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
    global bored
    if activity == "running":
        star_run = star
        star_textbooks = False
        star_count = star_count -1
    elif activity == "textbooks":
        star_textbooks = star
        star_run = False
        star_count = star_count -1
    elif activity == "rest":
        star_rest = star
        star_count = star_count -1
    else:
        print("please enter a valid activity to get a star")
    if star_count <0:
        bored = True
    if bored == True:
        star_run = False
        star_textbooks = False
def star_can_be_taken(activity):
    if star_run == True and activity == "running" and star_count>=0 and bored == False:
        print("True")
    elif star_textbooks == True and activity == "textbooks" and star_count>=0 and bored == False:
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
    elif star_textbooks:
        return "textbooks"
    elif not tired:
        return "running"
    elif tired:
        return "resting"

if __name__=="__main__":
    initialize()
