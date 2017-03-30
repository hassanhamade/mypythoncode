def calc_average(list_of_values):
    if len(list_of_values)==0:
        # ValueError is an existing exception built into Python.
        # What we are doing here is just raising it at a particular point in the code. Python itself by
        # default would have NOT raised this exception as for him, an empty list of values is not a problem.
        # It only becomes a pb (and Python will raise another exception for this) when later in the code,
        # we try to divide by the length of this empty list. We, as a programmer, however want to avoid this
        # division by zero situation in the first place so we're going to raise an exception much earlier.
        raise ValueError("No values inputed")
    total=0
    for i in range(len(list_of_values)):
        total=total+list_of_values[i]
    average=total/len(list_of_values)
    return average

try:
    list1=[10,20,30,40,50]
    avg=calc_average(list1)
    print("First average: {}".format(avg))
    list4=c
    avg=calc_average(list4)
    print("First average: {}".format(avg))
    list3=["a","b","c","d"]
    avg=calc_average(list3)
    print("Third average: {}".format(avg))
    list2=[]
    avg=calc_average(list2)
    print("Second average: {}".format(avg))
except ValueError:
    print("Error: you've entered an empty list")
except NameError:
    print("Input for the 'calc_average' function is not valid")
except TypeError:
    print("You have entered non valid arguments")
except:
    print("Got some kind of error")
else:
    print("Everything went great")
finally:
    print("Final block called")
    
        
    
        
    
    
        
    
