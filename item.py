class Item:
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_item_name(self, name):
        self.name = name

    def get_item_name(self):
        return self.name
    
    def set_item_description(self, description):
        self.description = description
    
    def get_item_description(self):
        return self.description

    def describe(self):
        print(f"The [{self.name}] is here - {self.description}")

    
        


    
