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
            if star_count < 1:
                star_count = 1
            elif star_count == 1:
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
    ##CHECK PLEASE

if __name__=="__main__":
    initialize()
    perform_activity("running", 30)
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(most_fun_activity_minute())  # resting                              # Test 3

    perform_activity("resting", 30)

    offer_star("running")

    print(most_fun_activity_minute())  # running                              # Test 4

    perform_activity("textbooks", 30)
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6

    offer_star("running")

    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8

    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10

    # My tests

    # Variations of consecutive running
    print()
    perform_activity("resting", 1)
    print(get_cur_health())            # 700, nothing happens
    print(get_cur_hedons())            # -430, nothing happens
    # Combined consecutive running > 180m
    perform_activity("running", 120) # tired
    perform_activity("running", 30)
    perform_activity("running", 50)
    print(get_cur_health())            # 1260 = 700 + 180 * 3 + 20 * 1
    print(get_cur_hedons())            # -830 = -430 - 200 * 2
    perform_activity("running", 100) # tired
    print(get_cur_health())            # 1360 = 1260 + 100 * 1
    print(get_cur_hedons())            # -1030 = -830 - 100 * 2
    # Single running event < 180m
    perform_activity("textbooks", 20) # tired
    print(get_cur_health())            # 1400 = 1360 + 20 * 2
    print(get_cur_hedons())            # -1070 = -1030 - 20 * 2
    # Single running event > 180m
    perform_activity("running", 300) # tired
    print(get_cur_health())            # 2060 = 1400 + 180*3 + 120*1
    print(get_cur_hedons())            # -1670 = -1070 - 300 * 2

    # Tired
    print()
    perform_activity("resting", 120) # no longer tired
    print(get_cur_health())            # 2060, nothing happens
    print(get_cur_hedons())            # -1670, nothing happens
    # Not valid activities with times > 120m between tiring activities
    perform_activity("textbooks", 30)
    print(get_cur_health())            # 2120 = 2060 + 2 * 30
    print(get_cur_hedons())            # -1660 = -1670 + 20 * 1 - 10 * 1
    #perform_activity("jogging", 50)
    #perform_activity("cycling", 80)
    perform_activity("running", 80) # tired
    print(get_cur_health())            # 2360 = 2120 + 3 * 80
    print(get_cur_hedons())            # -1820 = -1660 - 2 * 80
    # consecutive tiring activities
    perform_activity("textbooks", 90) # tired
    print(get_cur_health())            # 2540 = 2360 + 2 * 90
    print(get_cur_hedons())            # -2000 = -1820 - 2 * 90
    perform_activity("running", 190) # tired
    print(get_cur_health())            # 3090 = 2540 + 3 * 180 + 1 * 10
    print(get_cur_hedons())            # -2380 = -2000 - 2 * 190
    # rests of not enough time between tiring activites
    perform_activity("resting", 119)
    print(get_cur_health())            # 3090, nothing happens
    print(get_cur_hedons())            # -2380, nothing happens
    perform_activity("running", 180) # tired
    print(get_cur_health())            # 3630 = 3090 + 3 * 180
    print(get_cur_hedons())            # -2740 = -2380 - 2 * 180
    # rests of enough time between tiring activites
    perform_activity("resting", 150) # no longer tired
    print(get_cur_health())            # 3630, nothing happens
    print(get_cur_hedons())            # -2740, nothing happens
    perform_activity("textbooks", 30)
    print(get_cur_health())            # 3690 = 3630 + 2 * 30
    print(get_cur_hedons())            # -2730 = -2740 + 1 * 20 - 1 * 10

    initialize() # SHOULD RESET

    # Stars, part 1
    print()
    # not tired, running, resting, textbooks
    offer_star("running") # t = 0
    perform_activity("running", 180)
    print(get_cur_health())            # 540 = 0 + 3 * 180
    print(get_cur_hedons())            # -290 = 0 + 2 * 10 - 2 * 170 + 3 * 10
    perform_activity("resting", 120)
    print(get_cur_health())            # 540, nothing happens
    print(get_cur_hedons())            # -290, nothing happens
    offer_star("textbooks") # t = 300
    perform_activity("textbooks", 8)
    print(get_cur_health())            # 556 = 540 + 2 * 8
    print(get_cur_hedons())            # -258 = -290 + 1 * 8 + 3 * 8
    # tired running, resting
    offer_star("running") # t = 308
    perform_activity("running", 181)
    print(get_cur_health())            # 1097 = 556 + 3 * 180 + 1 * 1
    print(get_cur_hedons())            # -590 = -258 - 2 * 181 + 3 * 10
    offer_star("textbooks") # t = 489
    perform_activity("textbooks", 11)
    print(get_cur_health())            # 1119 = 1097 + 2 * 11
    print(get_cur_hedons())            # -582 = -590 - 2 * 11 + 3 * 10
    # not bored with stars, 3 at 2 hours
    offer_star("running") # t = 500
    perform_activity("running", 109)
    print(get_cur_health())            # 1446 = 1119 + 3 * 109
    ##here
    print(get_cur_hedons())            # -770 = -582 - 2 * 109 + 3 * 10
    offer_star("running") # t = 609, 3rd star, 120 min, not bored
    perform_activity("running", 9)
    print(get_cur_health())            # 1473 = 1446 + 3 * 9
    print(get_cur_hedons())            # -761 = -770 - 2 * 9 + 3 * 9
    # bored with stars, 3 within 2 hours
    perform_activity("resting", 1)
    offer_star("running") # t = 619, 3rd star, 119 min, bored
    perform_activity("running", 60)
    print(get_cur_health())            # 1653 = 1473 + 3 * 60
    print(get_cur_hedons())            # -881 = -761 - 2 * 60
    # test more stars while bored
    perform_activity("resting", 30)
    perform_activity("resting", 90)
    offer_star("textbooks") # no effect
    perform_activity("textbooks", 10)
    print(get_cur_health())            # 1673 = 1653 + 2 * 10
    print(get_cur_hedons())            # -871 = -881 + 1 * 10


    # Bored with Stars (incomplete)
    print()
    # 3 in 2 hours
    offer_star("running")
    offer_star("textbooks")
    perform_activity("running", 20)
    print(get_cur_health() == 20*3) # 60
    print(get_cur_hedons() == 2*10 - 2 * 10) # 0
    offer_star("running")
    perform_activity("running", 170) # tired, >180 minutes, bored w/ stars
    print(get_cur_health() == 60 + 3 * 160 + 1 * 10) # 550
    print(get_cur_hedons() == 0 - 2 * 170) # -340

