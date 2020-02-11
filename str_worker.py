
def extra_split(version):
    splitted_list=[]
    for vers_step in version:
            
	    for split_step in vers_step.split("-"):
	    	splitted_list.append(split_step)

    return splitted_list       
def to_numbers_format(my_list):
    prioriti_dict={
    	"alpha":0,
        "beta":1,
        "rc":2
    }

    to_numbers_list=[]

    for list_step in my_list:
        if prioriti_dict.get(list_step)!=None:
            to_numbers_list.append(str(prioriti_dict.get(list_step)))
        else:
            to_numbers_list.append(list_step)
    return to_numbers_list
		