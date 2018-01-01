applicants_prefer_list = [
    [2, 3, 1],
    [3, 1, 2],
    [2, 3, 1],
    [1, 2, 3],
    [1, 3, 2]
]
universities_prefer_list = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 1],
    [4, 5, 1, 2, 3]

]
applications_counter = []
applicants_matched = []
universities_matched = []
for i in range(len(applicants_prefer_list)):
    applications_counter.append(0)
for i in range(len(applicants_prefer_list)):
    applicants_matched.append(0)
for i in range(len(universities_prefer_list)):
    universities_matched.append(0)


def inverse_arr(arr):
    temp_arr = arr[:]
    arr_inverse = []
    for k in range(len(temp_arr)):
        arr_inverse.append(0)
    for k in range(len(temp_arr)):
        arr_inverse[temp_arr[k]-1] = k+1
    return arr_inverse

########################################
inverted_universities_prefer_list = [[[] for j in range(len(applicants_prefer_list))] for i in range(len(universities_prefer_list))]
for j in range(len(universities_prefer_list)):
    inverted_universities_prefer_list[j] = inverse_arr(universities_prefer_list[j])
print "Inverted University Preference List to Student wise: ",inverted_universities_prefer_list

for i in range(len(applicants_prefer_list)):
    print "Trying to find a good partner for applicant #", i+1
    for j in range(len(universities_prefer_list)):
        if universities_matched[applicants_prefer_list[i][j]-1] == 0:
            print "applicant #", i+1, "likes to be with university #", applicants_prefer_list[i][j]
            print "university #", applicants_prefer_list[i][j], " isn\'t matched to anybody.\nSo applicant #", i+1, \
                " became matched with university #", applicants_prefer_list[i][j]
            applications_counter[i] += 1
            applicants_matched[i] = applicants_prefer_list[i][j]
            universities_matched[applicants_prefer_list[i][j]-1] = i+1
            break
        else:
            print "Applicant #", i+1, "likes university #", applicants_prefer_list[i][j]
            print "But university #", applicants_prefer_list[i][j], " is already matched."
            applications_counter[i] += 1
            university = applicants_prefer_list[i][j]
            matching = universities_matched[applicants_prefer_list[i][j]-1]
            new_applicant = i+1
            accepted = 0
            temp=universities_prefer_list[applicants_prefer_list[i][j]-1]
            temp2=temp[:]
            inverse = inverted_universities_prefer_list[applicants_prefer_list[i][j]-1]
            print "University #", applicants_prefer_list[i][j], " has to choose between applicant #", i+1, " and applicant #", matching
            print "Here is the list of university #", applicants_prefer_list[i][j], "\'s preferences"
            print universities_prefer_list[applicants_prefer_list[i][j]-1]
            print "And here is the inverse list corresponding to it"
            print inverse
            print "i = ", i, "-", "inverse[i] is : ", inverse[i], "matching = ", matching, " - and inverse[matching] is : ", inverse[matching]
            if inverse[i] < inverse[matching-1]:
                print "University #", applicants_prefer_list[i][j], "prefers to be with applicant #", i+1
                accepted = 1
            if accepted == 1:
                applicants_matched[matching-1] = 0
                universities_matched[university-1] = new_applicant
                applicants_matched[new_applicant-1] = university
                break
            else:
                print "University #", applicants_prefer_list[i][j], "prefers to be with applicant #", matching
                print "So, The application was rejected!"
                continue

########################################
print "\n"
print "First iteration was finished... The results : "
print "applicants matched: ", applicants_matched
print "universities matched: ", universities_matched
print "Number of applications each: ", applications_counter
print "\n"
########################################
def some_applicant_is_alone_but_hasnt_applied_to_all_universities():
    result = []
    for i in range(len(applicants_matched)):
        if applicants_matched[i] == 0:
            if applications_counter[i] < len(universities_matched):
                result.append(True)
                result.append(i)
                return result
    result.append(False)
    result.append(-1)
    return result

condition = some_applicant_is_alone_but_hasnt_applied_to_all_universities()
while True in condition:
    the_applicant = some_applicant_is_alone_but_hasnt_applied_to_all_universities()
    the_applicant = the_applicant[1]
    the_first_university_he_hasnt_applied_yet = applications_counter[the_applicant]
    the_applicants_prefer_list = applicants_prefer_list[the_applicant]
    i = the_applicant
    print "It turns out applicant #", i+1, "is alone and hasn\'t applied to all universities."
    for j in range(the_first_university_he_hasnt_applied_yet, len(the_applicants_prefer_list)):
        print "\n"
        print "Applicant #", i+1, "likes university #", applicants_prefer_list[i][j]
        print "But university #", applicants_prefer_list[i][j], " is already matched."
        print "\n"
        applications_counter[i] += 1
        university = applicants_prefer_list[i][j]
        matching = universities_matched[applicants_prefer_list[i][j]-1]
        new_applicant = i+1
        accepted = 0
        temp = universities_prefer_list[applicants_prefer_list[i][j]-1]
        temp2 = temp[:]
        inverse = inverted_universities_prefer_list[applicants_prefer_list[i][j]-1]
        print "University #", applicants_prefer_list[i][j], " has to choose between applicant #", i+1, " and applicant #", matching
        print "\n"
        print "Here is the list of university #", applicants_prefer_list[i][j], "\'s preferences"
        print ""
        print universities_prefer_list[applicants_prefer_list[i][j]-1]
        print "\n"
        print "And here is the inverse list corresponding to it"
        print ""
        print inverse
        print "\n"
        print "i = ", i, "-", "inverse[i] is : ", inverse[i], "matching = ", matching, " - and inverse[matching] is : ", inverse[matching-1]
        if inverse[i] < inverse[matching-1]:
            print "\n"
            print "University #", applicants_prefer_list[i][j], "prefers to be with applicant #", i+1
            accepted = 1
        if accepted == 1:
            applicants_matched[matching-1] = 0
            universities_matched[university-1] = new_applicant
            applicants_matched[new_applicant-1] = university
            break
        else:
            print "\n"
            print "University #", applicants_prefer_list[i][j], "prefers to be with applicant #", matching
            print "So, The application was rejected!"
            print "\n\n"
            continue
    condition = some_applicant_is_alone_but_hasnt_applied_to_all_universities()

########################################
print "\n"
print "The final result: "
print "applicants matched: ", applicants_matched
print "universities matched: ", universities_matched
print "Number of applications each: ", applications_counter
