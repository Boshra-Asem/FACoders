Homework_Week_4


grade_one= {'Sami':    [19, 18, 19.5, 30, 10],
  'Ahmad':   [15, 14, 16, 21, 7],
  'Faris':   [18, 19, 17, 26, 9],
  'Salem':   [20, 20, 19, 30, 10],
  'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana':  [17, 19, 20, 28, 9],
  'Dina':  [18.5, 19.5, 20, 29, 10],
  'Maha':  [20, 20, 18, 26, 9],
  'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima':  [18, 19, 18, 26, 9],
    'Tala':  [20, 20, 19, 29, 10],
    'Lamar': [19, 20, 18, 26, 9],
    'Rola':  [15, 14, 16, 19, 7],
    'Naya':  [9, 6, 11, 14, 7],
    'Dalal': [1, 5, 2, 6, 7],
    'Ola':   [19.5, 20, 20, 29.5, 10]}

def students_names(sClass):
if sClass == 'grade_one':
sGrade_one = list(grade_one.keys())
return sGrade_one
elif sClass == 'grade_two':
sGrade_two = list(grade_two.keys())
return sGrade_two
elif sClass == 'grade_three':
sGrade_three = list(grade_three.keys())
return sGrade_three
else:
return 'This is wrong Class'

def student_score(sClass,sName):
if sClass == 'grade_one':
if sName in grade_one:
sMarks = grade_one.get(sName)
sSumMarks = sum(sMarks)
return sSumMarks
else:
return 'This is wrong Name'

elif sClass == 'grade_two':
if sName in grade_two:
sMarks = grade_two.get(sName)
sSumMarks = sum(sMarks)
return sSumMarks
else:
return 'This is wrong Name'

elif sClass == 'grade_three':
if sName in grade_three:
sMarks = grade_three.get(sName)
sSumMarks = sum(sMarks)
return sSumMarks
else:
return 'This is wrong Name'
else:
return 'This is wrong Class'

def student_count(sClass):
if sClass == 'grade_one':
sList = list(grade_one.keys())
sCounter = len(sList)
return sCounter
elif sClass == 'grade_two':
sList = list(grade_two.keys())
sCounter = len(sList)
return sCounter
elif sClass == 'grade_three':
sList = list(grade_three.keys())
sCounter = len(sList)
return sCounter
else:
return 'This is wrong Class'


print('Choose one: students_names, student_score, students_count')
sFunction = input()

if sFunction == 'students_names':
print('Enter student\'s class')
print('grade_one, grade_two, grade_three')
sClass=input()
print(students_names(sClass))

elif sFunction == 'student_score':
print('Enter student\'s class')
print('grade_one, grade_two, grade_three')
sClass=input()
print('Enter student\'s Name')
sName=input()
print(student_score(sClass,sName))

elif sFunction == 'students_count':
print('Enter student\'s class')
print('grade_one, grade_two, grade_three')
sClass=input()
print(student_count(sClass))

else:
print('This is wrong Function!')

print('Enter \'Done\' if you finished or \'More\' to continue')
sDone = input()

while sDone == 'More':
print('Choose one: students_names, student_score, students_count')
s_New_Function = input()

if s_New_Function == 'students_names':
print('Enter student\'s class')
print('grade_one, grade_two, grade_three')
sClass=input()
print(students_names(sClass))

elif s_New_Function == 'student_score':
print('Enter student\'s class')
print('grade_one, grade_two, grade_three')
sClass=input()
print('Enter student\'s Name')
sName=input()
print(student_score(sClass,sName))

elif s_New_Function == 'students_count':
print('Enter student\'s class')
print('grade_one, grade_two, grade_three')
sClass=input()
print(student_count(sClass))

else:
print('This is wrong Function!')

print('Enter \'Done\' if you finished or \'More\' to continue')
sDone = input()

if sDone == 'Done':
break

print('Thanks for your Effort')
