__author__ = 'Arman Malekzade'
men_prefer_list = [
    [2, 3, 1],
    [3, 1, 2],
    [2, 3, 1],
    [1, 2, 3],
    [1, 3, 2]
]
women_prefer_list = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 1],
    [4, 5, 1, 2, 3]

]
proposals_counter = []
men_engaged = []
women_engaged = []
for i in range(len(men_prefer_list)):
    proposals_counter.append(0)
for i in range(len(men_prefer_list)):
    men_engaged.append(0)
for i in range(len(women_prefer_list)):
    women_engaged.append(0)


def inverse_arr(arr):
    temp_arr = arr[:]
    arr_inverse = []
    for k in range(len(temp_arr)):
        arr_inverse.append(0)
    for k in range(len(temp_arr)):
        arr_inverse[temp_arr[k]-1] = k+1
    return arr_inverse

#######################################################################################################################
# FIRST ITERATION - BEGIN                                                                                             #
#######################################################################################################################

for i in range(len(men_prefer_list)):
    print "Trying to find a good partner for Man #", i+1
    for j in range(len(women_prefer_list)):
        if women_engaged[men_prefer_list[i][j]-1] == 0:
            print "Man #", i+1, "likes to be with Woman #", men_prefer_list[i][j]
            print "Woman #", men_prefer_list[i][j], " isn\'t engaged to anybody.\nSo Man #", i+1, \
                " became engaged with Woman #", men_prefer_list[i][j]
            proposals_counter[i] += 1
            men_engaged[i] = men_prefer_list[i][j]
            women_engaged[men_prefer_list[i][j]-1] = i+1
            break
        else:
            print "Man #", i+1, "likes Woman #", men_prefer_list[i][j]
            print "But Woman #", men_prefer_list[i][j], " is already engaged."
            proposals_counter[i] += 1
            woman = men_prefer_list[i][j]
            fiance = women_engaged[men_prefer_list[i][j]-1]
            new_proposer = i+1
            accepted = 0
            temp=women_prefer_list[men_prefer_list[i][j]-1]
            temp2=temp[:]
            inverse = inverse_arr(temp2)
            print "Woman #", men_prefer_list[i][j], " has to choose between Man #", i+1, " and Man #", fiance
            print "Here is the list of Woman #", men_prefer_list[i][j], "\'s preferences"
            print women_prefer_list[men_prefer_list[i][j]-1]
            print "And here is the inverse list corresponding to it"
            print inverse
            print "i = ", i, "-", "inverse[i] is : ", inverse[i], "fiance = ", fiance, " - and inverse[fiance] is : ", inverse[fiance]
            if inverse[i] < inverse[fiance-1]:
                print "Woman #", men_prefer_list[i][j], "prefers to be with Man #", i+1
                accepted = 1
            if accepted == 1:
                men_engaged[fiance-1] = 0
                women_engaged[woman-1] = new_proposer
                men_engaged[new_proposer-1] = woman
                break
            else:
                print "Woman #", men_prefer_list[i][j], "prefers to be with Man #", fiance
                print "So, The proposal was rejected!"
                continue


#######################################################################################################################
# FIRST ITERATION - END                                                                                               #
#######################################################################################################################
print "First iteration was finished... The results : "
print "Men Engaged: ", men_engaged
print "Women Engaged: ", women_engaged
print "Number of proposals: ", proposals_counter
#######################################################################################################################
# DO THEY REALLY DESERVE TO BE ALONE? - BEGIN                                                                         #
#######################################################################################################################
def some_man_is_alone_but_hasnt_proposed_to_all_women():
    result = []
    for i in range(len(men_engaged)):
        if men_engaged[i] == 0:
            if proposals_counter[i] < len(women_engaged):
                result.append(True)
                result.append(i)
                return result
    result.append(False)
    result.append(-1)
    return result

condition = some_man_is_alone_but_hasnt_proposed_to_all_women()
while True in condition:
    the_man = some_man_is_alone_but_hasnt_proposed_to_all_women()
    the_man = the_man[1]
    the_first_woman_he_hasnt_proposed_yet = proposals_counter[the_man]
    the_mans_prefer_list = men_prefer_list[the_man]
    i = the_man
    print "It turns out Man #", i+1, "is alone and hasn\'t proposed to all women."
    for j in range(the_first_woman_he_hasnt_proposed_yet, len(the_mans_prefer_list)):
        print "Man #", i+1, "likes Woman #", men_prefer_list[i][j]
        print "But Woman #", men_prefer_list[i][j], " is already engaged."
        proposals_counter[i] += 1
        woman = men_prefer_list[i][j]
        fiance = women_engaged[men_prefer_list[i][j]-1]
        new_proposer = i+1
        accepted = 0
        temp = women_prefer_list[men_prefer_list[i][j]-1]
        temp2 = temp[:]
        inverse = inverse_arr(temp2)
        print "Woman #", men_prefer_list[i][j], " has to choose between Man #", i+1, " and Man #", fiance
        print "Here is the list of Woman #", men_prefer_list[i][j], "\'s preferences"
        print women_prefer_list[men_prefer_list[i][j]-1]
        print "And here is the inverse list corresponding to it"
        print inverse
        print "i = ", i, "-", "inverse[i] is : ", inverse[i], "fiance = ", fiance, " - and inverse[fiance] is : ", inverse[fiance-1]
        if inverse[i] < inverse[fiance-1]:
            print "Woman #", men_prefer_list[i][j], "prefers to be with Man #", i+1
            accepted = 1
        if accepted == 1:
            men_engaged[fiance-1] = 0
            women_engaged[woman-1] = new_proposer
            men_engaged[new_proposer-1] = woman
            break
        else:
            print "Woman #", men_prefer_list[i][j], "prefers to be with Man #", fiance
            print "So, The proposal was rejected!"
            continue
    condition = some_man_is_alone_but_hasnt_proposed_to_all_women()


#######################################################################################################################
# DO THEY REALLY DESERVE TO BE ALONE? - END                                                                           #
#######################################################################################################################

print "The final result: "
print "Men engaged: ", men_engaged
print "Women engaged: ", women_engaged
print "Number of proposals: ", proposals_counter
