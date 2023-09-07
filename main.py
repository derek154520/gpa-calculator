participation = [] #setting up lists
classwork = []
quiz = []
test = []
print("Enter class weights (decimal):") #getting user input for weights
print("Participation: ")
p_weight = float(input())
print("Classwork: ")
c_weight = float(input())
print("Quiz: ")
q_weight = float(input())
print("Test: ")
t_weight = float(input())
print()

max_weight = p_weight + c_weight + q_weight + t_weight
if max_weight != 1: #checks to see if all weighted values add up to 1
  print('Please input weights again.')
  print()
  print("Enter class weights (decimal):")
  print("Participation: ")
  p_weight = float(input())
  print("Classwork: ")
  c_weight = float(input())
  print("Quiz: ")
  q_weight = float(input())
  print("Test: ")
  t_weight = float(input())
  print()
  max_weight = p_weight + c_weight + q_weight + t_weight
  if max_weight != 1:
    print('Please restart.')
    exit()

print('Do you have any assignments to enter?') #program will now store user inputs for grades
answer = input()
print()
if answer == 'yes' or answer == 'Yes': 
  print('Please enter the number of assignments you have for each category below.')
  print()
print('Number of participation assignments:') #participation assignments and grades
participation_assignments = int(input())
print()
for k in range(participation_assignments):
  print('Enter the percentage you got for the assignment:')
  grade1 = int(input())
  participation.append(grade1)
  print()

print('Number of classwork assignments:') #classwork assignments and grades
cw_assignments = int(input())
print()
for j in range(cw_assignments):
  print('Enter the percentage you got for the assignment:')
  grade2 = int(input())
  classwork.append(grade2)
  print()
  
print('Number of quiz assignments:') #quiz assignments and grades
quiz_assignments = int(input())
print()
for l in range(quiz_assignments):
  print('Enter the percentage you got for the assignment:')
  grade3 = int(input())
  quiz.append(grade3)
  print()
  
print('Number of test assignments:') #test assignments and grades
test_assignments = int(input())
print()
for h in range(test_assignments):
  print('Enter the percentage you got for the assignment:')
  grade4 = int(input())
  test.append(grade4)
  print()
 
#Calculating the average for each category:
new_p_weight = p_weight * 100
new_p = [element * new_p_weight for element in participation]
p_avg_weight = new_p_weight * len(participation)
final_p = sum(new_p) / p_avg_weight

new_c_weight = c_weight * 100
new_c = [c_element * new_c_weight for c_element in classwork]
c_avg_weight = new_c_weight * len(classwork)
final_c = sum(new_c) / c_avg_weight

new_q_weight = q_weight * 100
new_q = [q_element * new_q_weight for q_element in quiz]
q_avg_weight = new_q_weight * len(quiz)
final_q = sum(new_q) / q_avg_weight

new_t_weight = t_weight * 100
new_t = [t_element * new_t_weight for t_element in test]
t_avg_weight = new_t_weight * len(test)
final_t = sum(new_t) / t_avg_weight

sum_g = sum(new_p) + sum(new_c) + sum(new_q) + sum(new_t)
sum_w = p_avg_weight + c_avg_weight + q_avg_weight + t_avg_weight
quarter_grade = sum_g / sum_w

rounded_p = round(final_p, 2) #rounds the percentage to 2 decimal places
rounded_c = round(final_c, 2)
rounded_q = round(final_q, 2)
rounded_t = round(final_t, 2)
rounded_quarter = round(quarter_grade, 2)

print('Quarter Grade: ' + str(rounded_quarter) + '%') #prints each percentage
print('Participation: ' + str(rounded_p) + '%')
print('Classwork: ' + str(rounded_c) + '%')
print('Quiz: ' + str(rounded_q) + '%')
print('Test: ' + str(rounded_t) + '%')
print()
