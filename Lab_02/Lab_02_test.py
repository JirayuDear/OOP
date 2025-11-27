import json

def add_score(value):
    subject_score, student, subject, score = value.split("|")
    student = student.strip()
    subject = subject.strip()
    score = score.strip()
    subject_score = subject_score.replace("'",'"')
    subject = subject.replace('"', '').replace("'", "")
    student = student.replace('"', '').replace("'", "")
    sc = {}
    if subject_score == "" or student == "" or subject == "" or score == "":
        return {}
    try:
        sc_dict = json.loads(subject_score)
        if int(score) < 0:
            return "Invalid"
        if student not in sc_dict:
            sc[subject] = int(score)
            sc_dict[student] = sc
        else:
            sc_dict[student][subject] = int(score)
        return sc_dict
    except (SyntaxError, ValueError):
        return "Invalid"

def calc_average_score(subject_score):
    output = {}
    if not subject_score:
        return "Invalid"
    try:
        for student, scores in subject_score.items():
            total = sum(scores.values())
            subjects = len(scores)
            student_id = student
            avg = total / subjects
            output[student_id] = f"{avg:.2f}"
        return str(subject_score) + ", Average score: " + str(output)
    except (SyntaxError, ValueError, AttributeError):
        return "Invalid"

value = input()
subject_score = add_score(value)
output = calc_average_score(subject_score) 
print(output)