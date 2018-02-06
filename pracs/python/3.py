class Donor:
    donors = []
    def Input(self, Name, DateOfBirth, Address, Phone, BloodGroup):
        self.__Name = Name
        self.__DateOfBirth = DateOfBirth
        self.__Address = Address
        self.__Phone = Phone
        self.__BloodGroup = BloodGroup
    @staticmethod
    def Append(donor):
        Donor.donors.append(donor)
    def Show(self):
        print({
            "Name": self.__Name, 
            "DateOfBirth": self.__DateOfBirth, 
            "Address": self.__Address, 
            "Phone": self.__Phone, 
            "BloodGroup": self.__BloodGroup
        })
    @staticmethod
    def Search(bloodGroup):
        matches = []
        for donor in Donor.donors:
            if(donor.BloodGroup==bloodGroup):
                matches.append(donor)
        return matches