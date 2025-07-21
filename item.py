class Item:
    def __init__(self, name, item_type):
        self.name = name
        self.item_type = item_type
        self.description = None

    def set_item_name(self, name):
        self.name = name

    def get_item_name(self):
        return self.name
    
    def set_item_type(self, item_type):
        self.item_type = item_type

    def get_item_type(self):
        return self.item_type
    
    def set_item_description(self, description):
        self.description = description
    
    def get_item_description(self):
        return self.description

    def describe(self):
        print(f"The [{self.name}] is here - {self.description}")
        print(f"This item can be used as a [{self.item_type}]")




    
    
        


    
