#defining the function
def calc_average(list_of_values):
    if leng(list_of_values)==0:
        raise ValueError("No values input")
    total=0
    for i in range(len(list_of_values) + 1):
        total=total+i
    average=total/len(list_of_values)
    return average

#the below is what we call the calling program (program that will call the function above)
try:
    list_of_values=(1,2,3,4,5)
    avg=calc_average(list_of_values)
    print("First average: {}".format(avg))
    other_list_of_values=()
    avg=calc_average(other_list_of_values)
    print("Second average: {}".format(avg))
Except ValueError:
    print("Function didn't like our input!")

    


