myList = list()
output = []
# list_type = ['mixed', 'integer', 'string']
sum = 0
str_output = ''
myList = raw_input("please enter a list:")
output = myList.split(",")
for x in range(len(output)):
    try:
        sum += int(output[x])
        # list_type[1] = True
    except ValueError:
        str_output += output[x]
        # list_type[2] = True




if sum > 0 and str_output != '':
    print ("Mixed type of list")
elif sum >0 and str_output =='':
    print ("Integer type of list")
elif sum ==0 and str_output != '':
    print ("string type of list")

if sum > 0:
    print "Sum:", sum

if str_output != '':
    print str_output


#
#
#
# if list_type == 'integer' and not list_type == 'string':
#     print ("The list you entered is of integer type")
#     print ("Sum: ", sum)
# elif list_type == 'string' and not list_type == 'integer':
#     print ("The list you entered is of string type")
#     print ("string:", str_output)
# elif list_type == 'mixed':
#     print ("the list you entered is of mixed type")
#     print ("Sum: ", sum)
#     print ("string:", str_output)
#
# else:
#     print ("something went wrong...")
#

#

#
# try:
#     map(int, output)
#     int_output = output;
# except ValueError:
#     str_output = output
#
#
# for x in range(len(output)):
#     print(output[x], "is of type", type(output[x]))
# for x in range(len(int_output)):
#     print(int_output[x], "is of type", type(int_output[x]))
#
# # print output
# print int_output
# print str_output
