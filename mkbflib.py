class BrainFProgram:
    def __init__(self, path):
        self.__instructions = None # Holds the instructions loaded from file
        self.__instruction_pointer = None # Points to the current instruction
        self.__loop_set = None # Holds pointers to each loop beginning and end
        self.__memory = None
        self.__memory_pointer = None