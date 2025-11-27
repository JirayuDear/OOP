import json
def add_score(subject_score,student,subject,score):
    try:
        for i in range(len(data)):
            data[i] = data[i].strip()
        subject_score = data[0].replace("'", '"')
        subject_score = json.loads(subject_score)
        student = data[1].strip().strip("'") 
        subject = data[2].strip().strip("'") 
        score = (data[3].strip().strip("'"))

        if subject_score == "" or student == "" or subject == "" or score == "":
            return {}
        if int(score) < 0:
            return "Invalid"
        
        if student in subject_score:
            subject_score[student][subject] = int(score)
            return subject_score
        elif student not in subject_score and subject_score == {}:
            subject_score = {student: {subject:int(score)}}
            return subject_score
    except:
        return 'Invalid'
    
def calc_average_score(subject_score):
    average_score = {}
    if not subject_score:
        return "Invalid"
    try:
        for student, scores in subject_score.items():
            Sum = sum(scores.values())
            count = len(scores)
            student_id = student
            avg = Sum / count
            average_score[student_id] = f"{avg:.2f}"
        return (f"{str(subject_score)}, Average score: {str(f'{average_score}')}")
    except:
        return 'Invalid'    
        
try:
    data = input().split('|')
    result = add_score(data[0],data[1],data[2],data[3])
    result_last = calc_average_score(result)
    print(result_last)
except:
    print('Invalid')