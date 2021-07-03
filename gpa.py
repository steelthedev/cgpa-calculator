
courses =  [ 'bch310' , 'bch311' , 'bch312' , 'bch313' , 'bch315' , 'pbb313' , 'chm311' , 'ced300' ]


grades = {
    'A':5,
    'B':4,
    'C':3,
    'D':2,
    'F':0
}


courses_credits = {

    'bch310' : 5,
    'bch311' : 2,
    'bch312' : 4,
    'bch313' : 4,
    'bch315' : 2,
    'pbb313': 3,
    'chm311': 4,
    'ced300' : 2,
    'bch321' : 6

}


total_array_grade =[]



total_array_credits = sum(courses_credits.values())

print("Hello I am your friendly GPA calculator")

print()

while True:

    grade_bch310= input("Enter the grade for BCH310 ").upper()
    grade_bch311= input("Enter the grade for BCH311 ").upper()
    grade_bch312= input("Enter the grade for BCH312 ").upper()
    grade_bch313= input("Enter the grade for BCH313 ").upper()
    grade_bch315= input("Enter the grade for BCH315 ").upper()
    grade_pbb313= input("Enter the grade for PBB313 ").upper()
    grade_chm311= input("Enter the grade for CHM311 ").upper()
    grade_ced300= input("Enter the grade for CED300 ").upper()
    grade_bch321= input("Enter the grade for BCH321 ").upper()

    break

total_array_grade.append({
    'BCH310' : grade_bch310,
    'BCH311' : grade_bch311,
    'BCH312' : grade_bch312,
    'BCH313' : grade_bch313,
    'BCH315' : grade_bch315,
    'PBB313' : grade_pbb313,
    'CHM311' : grade_chm311,
    'CED300' : grade_ced300,
    'BCH321'  : grade_bch321

})

def arraygrade():

    for grade in total_array_grade:

        try:

            context ={

            'bch310' : grade["BCH310"],
            'bch311' : grade["BCH311"],
            'bch312' : grade["BCH312"],
            'bch313' : grade["BCH313"],
            'bch315' : grade["BCH315"],
            'pbb313' : grade["PBB313"],
            'chm311' : grade["CHM311"],
            'bch321' : grade["BCH321"],
            'ced300' : grade["CED300"]

            }


        except Exception as e:
            pass



    return context



def calculate(variable):

    context=arraygrade()

    if context[variable] == "A":

        credit_weight = 5  * courses_credits[variable]

        return credit_weight
    elif context[variable] == "B":

        credit_weight = 4  * courses_credits[variable]

        return credit_weight

    elif context[variable] == "C":

        credit_weight = 3  * courses_credits[variable]

        return credit_weight

    elif context[variable] == "D":


        credit_weight = 2  * courses_credits[variable]
        return credit_weight

    elif context[variable] == "F":

        credit_weight = 0  * courses_credits[variable]

        return credit_weight



bch310 = "bch310"
bch311 = "bch311"
bch312 = "bch312"
bch313 = "bch313"
bch315 = "bch315"
pbb313 = "pbb313"
ced300 = "ced300"
bch321 = "bch321"
chm311 = "chm311"



def results():

    #result = []
    points = {
        'bch310' :0 ,
        'bch311' :0 ,
        'bch312' :0,
        'bch313' : 0,
        'bch315' : 0,
        'pbb313' : 0,
        'chm311' :0,
        'ced300' : 0,
        'bch321' : 0,
        }


    bch310_points = calculate(bch310)
    bch311_points = calculate(bch311)
    bch312_points = calculate(bch312)
    bch313_points = calculate(bch313)
    bch315_points = calculate(bch315)
    pbb313_points = calculate(pbb313)
    ced300_points = calculate(ced300)
    bch321_points = calculate(bch321)
    chm311_points = calculate(chm311)

    try:
        points["bch310"] = bch310_points
        points["bch311"] = bch311_points
        points["bch313"] = bch313_points
        points["bch315"] = bch315_points
        points["bch312"] = bch312_points
        points["pbb313"] = pbb313_points
        points["chm311"] = chm311_points
        points["ced300"] = ced300_points
        points["bch321"] = bch321_points
    except:
        pass

    try:
        gpa_result_total = sum(points.values())


        gpa_300_level = gpa_result_total / total_array_credits

        print()

        print()

        print(f"Your 300 level GPA is {gpa_300_level} ")

        print()

    except Exception as e:
        print("Something went wrong somewhere , check your inputs and try again")



results()
