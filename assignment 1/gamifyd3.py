def initialize():
    '''initializes all global variables in the code by setting them to either a boolean (True or False), or their initial amounts'''
    global hedons #store the number of hedons the user has
    global health_points #store the number of health points the user has
    global last_duration #store the value of the duration of the last activity
    global last_activity #store the last activity that the user did
    global star #boolean, always return true, so when star_run and star_textbook need to be "activated", they can be set equal to star
    global star_count #store the number of stars that the user has (and keeps track of how many are left)
    global star_run #store boolean value for star_run; initially false because no stars for running are offered
    global star_textbooks # boolean value for star_textbooks; initially false because no stars for textbooks are offered
    global star_bonus #store the value for the bonus for hedons from stars
    global star_cooldown #store the 'cooldown' value between when star was offered and when star is called.
    global tired #boolean -true when no resting over 120 minutes between activities
    global cooldown #store cooldown between activities to keep track of if the user is tired
    global run_count #count total duration for consecutive running activities
    global bored #store boolean to check if user is bored of stars or not (i.e. when all stars used and cooldown<120).
    global num_run #track number of consecutive running activities
    num_run = 0
    bored = False
    star_cooldown = 0
    run_count = 0
    cooldown = 0
    tired = False
    last_activity = "n/a" #last_activity does not exist at first because the user hasn't done an activitiy
    star_count = 2
    star = True
    star_rest = False
    star_run = False
    star_textbooks = False
    last_duration = 0
    hedons = 0
    star_bonus =0
    health_points = 0
def get_cur_hedons():
    '''returns the number of hedons the user has accumulated. the global variable hedons updaets hedons each time'''
    global hedons
    return hedons

def get_cur_health():
    '''returns the number of health_points the user has acculumated. global variable health_points updates health_points each time'''
    global health_points
    return health_points


def perform_activity(activity, duration):
    '''assume duration is a positive integer. if activity is NOT running, textbooks, or resting, running the function returns for the user to input a valid value.
    activity is the string input for what the user is doing, from which they have three options: "running", "resting", or "textbooks". the duration is the positive integer input for which the user says for how long they are doing these activities.
    this function computes the hedons and health_points respective to the activity and duration of the user'''
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
    global star_bonus #track if star_bonus is 3 or 0, depending on if stars offered
    global tired
    global run_count
    global cooldown
    global bored
    global num_run

    if activity == "resting": #if the user is resting, adds duration to cooldown, and star for running or textbooks is ineffective. if user is not resting, they get no cooldown
        cooldown = cooldown + duration
        star_run = False
        star_textbooks = False
    elif last_activity == "running" or last_activity=="textbooks":
        cooldown = 0

#if the input is not running, textbooks, or resting, the function requires a valid input
    if not (activity == "running" or activity == "textbooks" or activity == "resting"):
        print("please enter either running, textbooks, or resting")


#if the user rested now or last time (or "n/a", the initial state of the user) and the user is cooled down for over 120 minutes, then the user is not tired. if the previous is not true, the user is tired and they get no cooldown
    if ((last_activity == "resting" or activity == "resting") and cooldown>=120) or last_activity == "n/a" or activity == "resting":
        tired = False
    else:
        tired = True
        cooldown = 0
#if the user rested last, then their counts of consecutive running is zero
    if last_activity == "resting":
        run_count = 0
#if the user is running, this duration gets added to the count of consecutive running sessions. if the user is carrying textbooks, this count is 0.
    if activity == "running":
        run_count=run_count + duration
    elif activity == "textbooks":
        run_count = 0

#if the user has two stars, they have no cooldown because they have all stars.
    if star_count == 2:
        star_cooldown = 0
    elif star_count <0: #if the user has less than 0 stars, (i.e., used two stars), then if their cooldown is above 120, their star count gets reset to 2 and cooldown to 0.
        if star_cooldown>=120:
            star_count = 2
            star_cooldown = 0
        elif star_cooldown < 120: #if the user has less than zero stars and cooldown is less than 120, all their stars will be false and they will officially be bored
            star_textbooks = False
            star_run = False
            bored = True
    elif star_count <2: #if the user has less than 2 stars (but more than 0 stars), the duration of their activity is added to the cooldown.
        star_cooldown = star_cooldown + duration
        if star_cooldown>=120: #if their cooldown is more than 120, their star count is reset to 2 and cooldown reset to 0
            star_count = 2
            star_cooldown = 0
    if bored == True: #if the user is bored, then their star values will both be false because they cannot use them
        star_textbooks = False
        star_run = False

    if activity == "running": #if the user is running, the number of consecutive running activities is increased by 1 each time they run.
        num_run = num_run + 1
    elif not activity == "running":
        num_run = 0

    if star_run and activity == "running":#if the user got offered a star for their respective activity and they are doing that activity, apply a bonus of +3 for the stars, then set the values of each star for an activity to False so they cannot be re-redeemed. if the user is not offered this, then their bonus remains 0.
        star_bonus = 3
        star_run == False
    elif star_textbooks and activity == "textbooks":
        star_bonus = 3
        star_textbooks == False
    else:
        star_bonus = 0

    if activity == "resting": #if the user is resting, their hedons and healthpoints stay the same. last_activity, last_duration are updated to the ones currently, run_count is set to zero because the user is not running
        hedons = hedons
        health_points = health_points
        last_activity = activity #last activity is now resting
        last_duration = duration #last duration is now updated to this duration
        run_count = 0
        return hedons
    if not tired: #the following applies for if the user is not tired
        if activity == "running": #if the user is running
            if run_count <=180: #if duration equal to or less than 180, user gets 3 health points per minute for the first 180 minutes
                health_points = health_points + (duration)*3
            elif run_count>180: #if duration more than 180, user gets 540 health points for the first 180 minutes, then whatever is left of the duration *1hp/min. subtract healthpoints that would otherwise be added twice
                health_points = health_points + 180*3 + (run_count-180)*1 - (run_count-duration)*180

            if duration <=10:#if duration is less than equal to 10 minutes, they get 2 hedons per minute plus a star bonus, if applicable
                hedons = hedons + duration*(2+star_bonus)
            else: #if duration is more than 10 minutes, they get 2 hedons per min for the first 10 minutes, then -2 hedons per minute for the rest. star bonus applies if star is offered
                hedons = hedons + 10*(2+star_bonus) + (duration-10)*-2
            last_activity = activity #last activity set to activity
            last_duration = duration #last duration set to duration
            star_run = False #star run is now false-- used to make sure it does not stay true, even after used
            tired = True #user is now tired from an activity.
            return last_duration #the first return statement else the computation of the function
        elif activity == "textbooks": #if carrying textbooks, the user gets 1 hedon for the first 20 minutes (+star bonus if applicable) and then -1 hedon for every minute after
            if duration <=20:
                if duration <= 10:
                    hedons = hedons + duration*(1+star_bonus)
                else:
                    hedons = hedons + 10*(1+star_bonus)+ (duration-10)*1
            elif duration>20:
                hedons = hedons + 20*(1+star_bonus) + (duration-20)*-1
            health_points = health_points + duration*2 #gets two health points per minute
            last_activity = activity  #last activity is now textbooks
            last_duration = duration #last duration is now this duration
            star_textbooks = False #star textbooks is no longer valid, if it was
            tired = True #user is now tired from an activity
            return last_duration #the first return stops the rest of this function from running
    elif tired: #if the user is tired (consecutive activities without at least 120 minutes of rest)
        if activity == "running": #if the user is running, they get 3 health opints per min for the first 180 mins
            if run_count <=180:
                health_points = health_points + (duration)*3
            elif run_count>180:
                if num_run <=3: #if the totol consecutive time for running is more than 180, and the number of times the user ran consecutively is less than equal to 3, then get 3 health point for the first 180 minutes, then 1 for each minute after, subtracted by the amount of health_points that is added twice
                    health_points = health_points + 180*3 + (run_count-180)*1 - (run_count-duration)*3
                elif num_run >3: #if number of consecutive runs more than three, get one health point for each minute spent after 180. overlapping parts are subtracted to avoid redundancy
                    health_points = health_points + (run_count-180) - (run_count-180-duration)
            if duration <= 10: #get -2 hedons per minute if tired, added by star bonus
                hedons = hedons + duration*(-2 + star_bonus)
            elif duration >10:
                hedons = hedons + 10*(-2 + star_bonus) + (duration-10)*(-2)
            last_activity = activity #last activity is now running
            last_duration = duration #last duration is now this duration
            star_run = False #star run is false -- star inactive now
            return last_duration #first return statement keeps code from running
        elif activity == "textbooks": #if the user was carrying textbooks
            if duration <=10: #the user gets -2 hedons per minute if tired, added by the bonus
                hedons = hedons + duration*(-2 + star_bonus)
            elif duration >10:
                hedons = hedons + 10*(-2 + star_bonus) + (duration-10)*(-2)
            health_points = health_points + duration*2 #gets 2 health points per minute for textbooks
            last_activity = activity #last activity is now this activity
            last_duration = duration #last duration is now this duration
            star_textbooks = False #star for textbooks is now false-- inactive
            return last_duration #first return keeps function from running

    else: #applies if user did not enter "running, "textbooks", or "resting"
        print("please enter a valid activity")

def offer_star(activity):
    '''offers star for each activity -- sets true for either star_run, star_textbooks, or star_rest (for this assignment, we generally assume star_rest is not called.
    star is always true, and star_run and star_textbooks are set to star when we want to change their value to true.
    star_count keeps track fo the number of stars, star_cooldown of the time spent between stars, and bored for when the user has used more than 2 stars in 120 minutes.'''
    global star
    global star_count
    global star_run
    global star_rest
    global star_textbooks
    global star_cooldown
    global bored
    if activity == "running": #sets star_run to True (star) if the user selected "running", and other activities to false. number of star is now one less.
        star_run = star
        star_textbooks = False
        star_count = star_count -1
    elif activity == "textbooks":#sets star_textbooks to True (star) if the user selected "textbooks", and other activities to false. number of star is now one less.
        star_textbooks = star
        star_run = False
        star_count = star_count -1
    elif activity == "rest": #sets star_rest to True (star) if the user selected "resting", and other activities to false. number of star is now one less. we generally assume this case doesn't exist (see assignment PDF)
        star_rest = star
        star_count = star_count -1
    else: #occurs if user did not enter "running", "resting", or "textbooks"
        print("please enter a valid activity to get a star")
    if star_count <0: #the user is bored if they ran out of stars
        bored = True
    if bored == True: #if the user is bored, they can no longer use stars to get bonuses for hedons for running or carrying textbooks
        star_run = False
        star_textbooks = False
def star_can_be_taken(activity):
    global star_run
    global star_count
    global bored
    global star_textbooks
    '''tells the user if they can take a star for the activity they have input. global variables are star run, star count, star textbooks, and bored, because those are the ones that need to be checked for the conditions to be fulfilled. '''
   #if a star is valid for running, the user chose running, they have available stars, and the user is not bored, then they can use  stars for running
    if star_run == True and activity == "running" and star_count>=0 and bored == False:
        print("True")
    #if a star is valid for textbooks, the user chose textbooks, they have available stars, and the user is not bored, then they can use  stars for textbooks
    elif star_textbooks == True and activity == "textbooks" and star_count>=0 and bored == False:
        print("True")
    #if none of the above conditions are true, then False is printed
    else:
        print("False")

def most_fun_activity_minute():
    '''sets conditions for which activity returns the most hedons if the user did it for one minute. in this case, the highest ranking in hedons is if the user has a star for running and is not tired (5 hedons), and the lowest is if the user is just tired, in which they will get 0 hedons for resting'''
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