survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
new_count = []
new_list = []

num1 = []
for j in range(len(choices)):
    first_count = 0
    second_count = 0
    if choices[j] == 1 :
        first_count = 3
    elif choices[j] == 2 :
        first_count = 2
    elif choices[j] == 3 :
        first_count = 1
    elif choices[j] == 4 :
        first_count, second_count = 0,0
    elif choices[j] == 5 :
        second_count = 1
    elif choices[j] == 6 :
        second_count = 2
    elif choices[j] == 7:
        second_count = 3

    new_count.append([first_count, second_count])


new_survey = []
for i in range(len(survey)):
    if new_count[i][0] != 0:
        new_survey += (survey[i][0] * new_count[i][0])
    elif new_count[i][1] != 0 :
        new_survey += (survey[i][1] * new_count[i][1])


R_cnt = sum(s.count('R') for s in new_survey)
T_cnt = sum(s.count('T') for s in new_survey)
C_cnt = sum(s.count('C') for s in new_survey)
F_cnt = sum(s.count('F') for s in new_survey)
J_cnt = sum(s.count('J') for s in new_survey)
M_cnt = sum(s.count('M') for s in new_survey)
A_cnt = sum(s.count('A') for s in new_survey)
N_cnt = sum(s.count('N') for s in new_survey)

result = []
new_survey = [item for sublist in new_survey for item in sublist]

# for i in range(len(new_survey_filtered)):
#     result += new_survey_filtered[i][0]
#     result += new_survey[0]
answer = [0,0,0,0]

if R_cnt >= T_cnt:
    answer[0] = 'R'
else :
    answer[0] = 'T'
if C_cnt >= F_cnt :
    answer[1] = 'C'
else :
    answer[1] = 'F'
if J_cnt >= M_cnt :
    answer[2] = 'J'
else :
    answer[2] = 'M' 
if A_cnt >= N_cnt :
    answer[3] = 'A'
else :
    answer[3] = 'N'



answer = ''.join(answer)
print(answer)

