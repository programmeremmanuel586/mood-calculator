


def get_score(score, user_input):
    if user_input == "A":
        score += 1
        return score
    elif user_input=="B":
        score += 2
        return score
    elif user_input=="C":
        score += 3
        return score

def get_mood(score):
    mood = ""
    if score >= 3 and score <=4:
        mood = "Sad"
    elif score >= 5 and score <=7:
        mood= "Happy"
    elif score >= 8 and score <=10:
        mood= "Meh"
    return mood
        
    
    




# def user_mood():
#     if request.method=='Get':
#         q1=userdata['value']
#         q2=userdata['value']
#         q3=userdata['value']
#         total= q1 + q2 + q3
#     if total <= 3:
#         return"Sad"
#     elif total >= 4 and total <= 6:
#         return "Happy"
#     elif total >= 7 and total <= 9:
#         return "Meh"