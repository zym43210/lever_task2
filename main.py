from functools import total_ordering

@total_ordering
class Version:

    
    
    def __init__(self, version):
        self.version=version.split(".")

    
  
    def __eq__(self, other):
        if len(self.version)==len(other.version):
            result_of_check=0
            for first_version, second_version in zip(self.version, other.version):

                if first_version==second_version:
                    result_of_check+=1
                else: 
                    result_of_check=0
            if result_of_check==len(self.version):
                return True
            else:
                return False
        
    def __lt__(self,other):
        
        
        extra_splitted_list1=Version.extra_split(self.version)
        extra_splitted_list2=Version.extra_split(other.version)
        ready_for_operations_list1=Version.to_numbers_format(extra_splitted_list1)
        ready_for_operations_list2=Version.to_numbers_format(extra_splitted_list2)
        
       
        if len(ready_for_operations_list1)==len( ready_for_operations_list2) and Version.common_part_less(ready_for_operations_list1, ready_for_operations_list2):
        
            return True
        elif len(ready_for_operations_list1)<len(ready_for_operations_list2) and Version.common_part_equal( ready_for_operations_list1, ready_for_operations_list2):
            
            return True

        
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
   
    def common_part_less(list1,list2):
            for list_step_1, list_step_2 in zip(list1, list2):
                if list_step_1<list_step_2:
                    return True
    def common_part_equal(list1,list2):
            for list_step_1, list_step_2 in zip(list1, list2):
                if list_step_1==list_step_2:
                    return True
    
   

       

def main():
    to_test = [
        ('1.0.0', '2.0.0'),
        ('1.0.0', '1.42.0'),
        ('1.2.0', '1.2.42'),
        ('1.1.0-alpha', '1.2.0-alpha.1'),
        ('1.0.1-beta', '1.0.10-alpha.beta'),
        ('1.0.0','1.0.0-rc.1'),
    ]

    for version_1, version_2 in to_test:
        print(version_1)
        print(version_2)
        
        assert Version(version_1) < Version(version_2), 'lt failed'
        assert Version(version_2) > Version(version_1), 'gt failed'
        assert Version(version_2) != Version(version_1), 'neq failed'


if __name__ == "__main__":
    main()