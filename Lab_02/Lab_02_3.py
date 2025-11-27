def add_score(subject_score,subject,score):
    subject_score = {}
    count = 0
    check = 0
    if int(score) < 0 or subject == "''":
        count = 1
        data[2] = 0
    
    data[0] = data[0].strip('{}')
    
    data[0] = data[0].split(',')
    
    for i in range(len(data[0])):
        data[0][i] = data[0][i].split(':')

    flattened_index_0 = data[0] 
    flattened_index_0 = [item for _ in flattened_index_0 for item in _] 

    data[0] = flattened_index_0
    for i in range(0,len(data[0])-1):
        if subject == data[0][i]:
            del data[0]
            check = 1
    for i in range(0,len(data[0])-1):
        if not (check >= 1):
            data.extend(data[0])
            del data[0]
            check = 1

    for i in range(len(data)-1):
        data[i] = str(data[i])
        data[i] = data[i].strip()
        if data[i] == "''" or data[i] == "['']":
            del data[i]
    
    for i in range(0,len(data)-1,2):
        data[i] = data[i].strip("'")
    for i in range(1,len(data),2):
        data[i] = int(data[i])
    if count != 1:
        for i in range(2, len(data)-1, 2):  
            subject_score[data[i]] = data[i+1]
        subject_score[data[0]] = data[1]
    
    def calc_average_score():
        item = (len(data)/2)
        sum = 0

        for i in range(1,len(data),2):
            sum = sum+int(data[i])

        average = sum/item
        print(f"{str(subject_score).rstrip()}, Average score: {str(f'{average:.2f}')}")

    calc_average_score()
    
data = input().split('|')
for i in range(len(data)):
    data[i] = data[i].strip()
add_score(data[0],data[1],data[2])