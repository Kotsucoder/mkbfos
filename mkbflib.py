class BrainFProgram:
    def __init__(self, path):
        self.__instructions = self.__load_program(path)
        self.__instruction_pointer = 0
        self.__loop_set = self.__get_loop_set()
        self.__memory = [0 for i in range(0, 100000)]
        self.__memory_pointer = 0

    def __load_program(self, path):
        with open(path, "r") as file:
            full_code = file.read()
        valid_chars = ['+', '-', '.', ',', '[', ']']
        short_code = []
        for char in full_code:
            if char in valid_chars:
                short_code.append(char)
        return short_code
    
    def __get_loop_set(self):
        loop_stack = []
        loop_set = {}
        for index, instruction in enumerate(self.__instructions):
            if instruction == "[":
                loop_stack.append(index)
            if instruction == "]":
                loop_start = loop_stack.pop()
                loop_end = index
                loop_set[loop_start] = loop_end
                loop_set[loop_end] = loop_start
        return loop_set


if __name__ == "__main__":
    helloworld = BrainFProgram("helloworld.bf")