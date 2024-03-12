import b_AthleteClass as ac

generic_athlete = ac.Athlete(6,220,0.2)

Devin = ac.Football_Player(6.2,250,0.15,'quarterback','offense')


print("The height for the generic athlete is:",generic_athlete.get_ht())

#rint("The team of the generic athlete is:",generic_athlete.get_team())

print("The weight for the football player is:",Devin.get_wt())

print("The position of the football player is:",Devin.get_position())
