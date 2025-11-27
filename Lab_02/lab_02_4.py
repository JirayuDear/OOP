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
            print("Invalid")
            return
        if int(score) < 0:
            print("Invalid")
            return 
        
        if student in subject_score:
            subject_score[student][subject] = int(score)
        elif student not in subject_score and subject_score == {}:
            subject_score = {student: {subject:int(score)}}

        if not subject_score:
            print('Invalid')
            return

        def calc_average_score():
            Sum = sum(subject_score[student].values())
            count = len(subject_score[student])
            average = Sum / count
            average_score = {student: f"{average:.2f}"}
            return print(f"{str(subject_score)}, Average score: {str(f'{average_score}')}")

        calc_average_score()    
    except:
        print('Invalid')
        return    
try:
    data = input().split('|')
    result = add_score(data[0],data[1],data[2],data[3])
except:
    print('Invalid')