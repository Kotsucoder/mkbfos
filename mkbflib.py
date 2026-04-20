import sys

class BrainFProgram:
    def __init__(self, path):
        self.__instructions = self.__load_program(path)
        self.__instruction_pointer = 0
        self.__loop_set = None # Holds pointers to each loop beginning and end
        self.__memory = None
        self.__memory_pointer = None

    def __load_program(self, path):
        with open(path, "r") as file:
            full_code = file.read()
        valid_chars = ['+', '-', '.', ',', '[', ']']
        short_code = []
        for char in full_code:
            if char in valid_chars:
                short_code.append(char)
        return short_code
    
    def print_program(self):
        code_str = ""
        for instruction in self.__instructions:
            code_str += instruction
        print(code_str)


if __name__ == "__main__":
    helloworld = BrainFProgram("helloworld.bf")
    helloworld.print_program()