def common_part_less(list1,list2):
    for list_step_1, list_step_2 in zip(list1, list2):
        if list_step_1<list_step_2:
                return True
def common_part_equal(list1,list2):
    for list_step_1, list_step_2 in zip(list1, list2):
        if list_step_1==list_step_2:
            return True