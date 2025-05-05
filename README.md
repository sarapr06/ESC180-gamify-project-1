# ESC180-gamify-project-1
Gamifying points for a student, as per assignment 1 in ESC180 Course, taught by Michael Guerzhoy.

# Assignment description
Gamification is the integration of elements found in games – such as points and badges – into nongame activities. One example of gamification is students’ being awarded badges and points for completing exercises in online courses. This is done in order to encourage students to complete the exercises. Another example is supermarkets awarding points to customers for purchasing various items. This is done, in part, to induce the customers to purchase more items in order to gain more points.
In this project, you will implement a simulator for an app that encourages the user to exercise more by awarding “stars” to the user for exercising. The simulator will model how the user behaves, and could be used to try out various strategies for awarding stars.
We imagine the user as accumulating “health points” and “fun points” (sometimes called hedons). Every activity is associated with gaining some number of health points and some number of hedons. Receiving a star increases the number of hedons that the user gains from performing the activity. Receiving too many stars too often makes the user lose interest in stars altogether. The simulation proceeds as a series of operations, which are simulated using calls to the functions that you will define.
We assume that the user is always either running, carrying textbooks, or resting.
The user accumulates hedons and health points according to the following rules:

• The user starts out with 0 health points, and 0 hedons.

• The user is always either running, carrying textbooks, or resting.

• Running gives 3 health points per minute for up to 180 minutes, and 1 health point per minute for every minute over 180 minutes that the user runs. (Note that if the user runs for 90 minutes, then rests for 10 minutes, then runs for 110 minutes, the user will get 600 health points, since they rested in between the times that they ran.)

• Carrying textbooks always gives 2 health points per minute.

• Resting gives 0 hedons per minute.

• Both running and carrying textbooks give -2 hedons per minute if the user is tired and isn’t using a star (definition: the user is tired if they finished running or carrying textbooks less than 2 hours before the current activity started.) For example, for the purposes of this rule, the user will be tired if they run for 2 minutes, and then start running again straight away.

• If the user is not tired, running gives 2 hedons per minute for the first 10 minutes of running, and -2 hedons per minute for every minute after the first 10.

• If the user is not tired, carrying textbooks gives 1 hedon per minute for the first 20 minutes, and -1 hedon per minute for every minute after the first 20.

• If a star is offered for a particular activity and the user takes the star right away, the user gets an additional 3 hedons per minute for at most 10 minutes. Note that the user only gets 3 hedons per minute for the first activity they undertake, and do not get the hedons due to the star if they decide to keep performing the activity:

  offer_star("running")

  perform_activity("running", 5) # gets extra hedons

  perform_activity("running", 2) # no extra hedons

• If three stars are offered within the span of 2 hours, the user loses interest, and will not get additional hedons due to stars for the rest of the simulation.
