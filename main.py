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
        assert Version(version_2) != Version(version_1), 'neq failed'


if __name__ == "__main__":
    main()