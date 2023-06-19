class Playboy:
    __body_count = 0
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
        self.girls_slept = []
        self.denials = []
        
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
        
    def find_girl(self):
        full_name = self.get_full_name()
        if full_name not in self.girls_slept:
            self.girls_slept.append(full_name)
            return self.girls_slept
        
        return f"{full_name} is already your girlfriend!"
            
    def break_up(self):
        full_name = self.get_full_name()
        if full_name in self.girls_slept:
            self.girls_slept.remove(full_name)
            return f"You broke up with {full_name}"
        
girl1 = Playboy("Maria", "Popova")
print(girl1.get_full_name())
print(girl1.find_girl())
print(girl1.break_up())

girl2 = Playboy("Anna", "Ilieva")
print(girl2.get_full_name())
print(girl2.find_girl())