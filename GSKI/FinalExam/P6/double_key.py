class DoubleKeyContainer:
    def __init__(self):
        self.phones = {}
        self.ids = {}
    
    def add_contact(self, id, name, phone):
        if id in self.ids.keys():
            self.remove(id)
        if phone in self.phones.keys():
            self.remove(self.phones[phone])
        self.ids[id] = [phone, name]
        self.phones[phone] = id
    
    def get_name_by_id(self, id):
        if id in self.ids.keys():
            return self.ids[id][1]
        return None
    
    def get_name_by_phone(self, phone):
        if phone in self.phones.keys():
            return self.get_name_by_id(self.phones[phone])
        return None

    def remove(self, id):
        try:
            self.phones.pop(self.ids[id][0])
            self.ids.pop(id)
        except:
            pass

if __name__ == "__main__":

    print("TESTING DOUBLE KEY - MAKE BETTER TESTS!!!\n")

    dkc = DoubleKeyContainer()
    dkc.add_contact(23, "Kári", 23543)
    dkc.add_contact(21, "Sigurður", 12342153)
    dkc.add_contact(13, "Kristmundur", 63567356)
    dkc.add_contact(87, "Eysteinn", 73345)
    dkc.add_contact(3, "Hrafn", 93543)

    print(dkc.get_name_by_id(13))
    print(dkc.get_name_by_phone(23543))
    print(dkc.get_name_by_id(87))
    print(dkc.get_name_by_phone(73345))
    dkc.remove(87)
    print(dkc.get_name_by_id(87))
    print(dkc.get_name_by_phone(73345))