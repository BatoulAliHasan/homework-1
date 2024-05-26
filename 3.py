import json
user_name = input("Enter your name: ")
infile = 'questions.txt'
outfile = 'result.json'
questions = []
answers=[]
with open(infile, 'r') as s:
    lines = s.readlines()
    for i in range(0, len(lines), 2):
        question = lines[i].strip()
        answer = lines[i+1].strip()
        questions.append(question)
        answers.append(answer)
mark = 0
for i in questions:
    s = input(i)
    if s.lower() == answers[questions.index(i)].lower():
        mark += 1
d={"name":user_name,"mark":str(mark)}
with open(outfile, 'w') as f:
    json.dump(d, f)

print(f"{user_name}, your score is: {mark}/{len(questions)}")
