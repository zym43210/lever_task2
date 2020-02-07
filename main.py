class Version:
    def __init__(self, version):
        self.version=version.split(".")
    def length_checker(selfobj,otherobj):
        if len(selfobj)>=len(otherobj):
            return True
        else :
            return False
    def __lt__(self,other):

        if(Version.length_checker(self.version,other.version)) :
            pass
        else:
            self.version,other.version=other.version,self.version
        counter_of_secondVer=0;
        for steps in self.version:

            if steps<other.version[counter_of_secondVer]:
                return True
            elif steps>other.version[counter_of_secondVer]:
                return False
            counter_of_secondVer=counter_of_secondVer+1
            

       

def main():
    to_test = [
        ('1.0.0', '2.0.0'),
        ('1.0.0', '1.42.0'),
        ('1.2.0', '1.2.42'),
        ('1.1.0-alpha', '1.2.0-alpha.1'),
        ('1.0.1b', '1.0.10-alpha.beta'),
        ('1.0.0-rc.1', '1.0.0'),
    ]

    for version_1, version_2 in to_test:
        print("kek")
        assert Version(version_1) < Version(version_2), 'le failed'
    


if __name__ == "__main__":
    main()