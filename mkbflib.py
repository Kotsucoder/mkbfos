class BrainFProgram:
    def __init__(self, path: str):
        """
        An object representing a BrainF program with the ability to execute each instruction.
        """
        self.__instructions = self.__load_program(path)
        self.__instruction_pointer = 0
        self.__loop_set = self.__get_loop_set()
        self.__memory = [0 for i in range(0, 100000)]
        self.__memory_pointer = 0
        self.__memory_length = 10000

    def __load_program(self, path: str) -> list[str]:
        """
        Loads the BF program from the file at the given path.
        """
        with open(path, "r") as file:
            full_code = file.read()
        valid_chars = ['>', '<', '+', '-', '.', ',', '[', ']']
        short_code = []
        for char in full_code:
            if char in valid_chars:
                short_code.append(char)
        return short_code
    
    def __get_loop_set(self) -> dict[int, int]:
        """
        Grabs the indexes for the starts and ends of each loop and pairs them together in a dictionary.
        """
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
    
    def __move_right(self):
        """
        Moves the memory pointer one cell to the right.
        """
        self.__memory_pointer += 1
        if self.__memory_pointer >= self.__memory_length:
            self.__memory_pointer = 0

    def __move_left(self):
        """
        Moves the memory pointer one cell to the left.
        """
        self.__memory_pointer -= 1
        if self.__memory_pointer < 0:
            self.__memory_pointer = self.__memory_length - 1
    
    def __increment(self):
        """
        Increments the value at the current memory cell.
        """
        self.__memory[self.__memory_pointer] += 1
        if self.__memory[self.__memory_pointer] > 255:
            self.__memory[self.__memory_pointer] = 0
    
    def __decrement(self):
        """
        Decrements the value at the current memory cell.
        """
        self.__memory[self.__memory_pointer] -= 1
        if self.__memory[self.__memory_pointer] < 0:
            self.__memory[self.__memory_pointer] = 255
    
    def __output(self):
        """
        Outputs the character at the current memory cell.
        """
        char = chr(self.__memory[self.__memory_pointer])
        print(char, end="")

    def __input(self):
        """
        Takes in a char input and saves it's ASCII number to the current memory cell.
        """
        valid = False
        print()
        while not valid:
            try:
                value = ord(input("> ")[0])
                if value >= 0 and value <= 255:
                    valid = True
            except IndexError:
                continue


if __name__ == "__main__":
    helloworld = BrainFProgram("helloworld.bf")