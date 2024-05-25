exam_weightage=50
activity_weightage=30
sport_weightage=20
total_exam=200
total_activity=90
total_sport=100
exam1=int(input("enter the score : "))
exam2=int(input("enter the score : "))
exam = exam1 + exam2
print("exam = "+str(exam))
activity1 = int(input("enter the value : "))
activity2 = int(input("enter the value : "))
activity3 = int(input("enter the value : "))
activity = activity1 + activity2 +activity3
print("Activity = "+str(activity))
sport = int(input("enter the value 0f sport : "))

exam_percent =(exam*exam_weightage)/total_exam

activity_percent = (activity*activity_weightage)/total_activity

sport_percent = (sport*sport_weightage)/total_sport

total_percent = exam_percent+activity_percent+sport_percent

print("Total percent in exam : "+str(exam_percent))

print("Total percent in activity : "+str(activity_percent))

print("Total percent in sport : "+str(sport_percent))

print("Total percentage : "+str(total_percent))