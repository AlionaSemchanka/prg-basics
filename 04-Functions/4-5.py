###
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif points>=14:
        grade = 'Good'
    elif points>=10:
        grade = 'Satisfactory'
    elif points<10:
        grade = 'Fail'   
    return grade

test_result = 15
final_grade = pts_to_grade(test_result)
print('You scored 15 points on the test. Your final grade is ', pts_to_grade(test_result))
