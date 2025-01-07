import os

class State:
    def __init__(self):
        unix_path = str('/home/ej/logicCLOCK/logic_ref')
        ntpath = str(r'C:\Users\ej\.vscode\code\logicCLOCK\logic_ref')
        if os.name == 'posix': logic_ref_path = unix_path
        else: logic_ref_path = ntpath

        self.logic_ref_path = logic_ref_path
    
    def logic_ref(self):
        """
        Returns logic_ref path.
        """
        return str(self.logic_ref_path)

    
    def reader(self, line=int()):
        with open(self.logic_ref_path, 'r') as ref:
            lines = ref.readlines()
            return bool(int(lines[line]))
        
    def writer(self, line=int(), value=int()):
        lines = []
        with open(self.logic_ref_path, 'r') as ref:
            lines = ref.readlines()
        
        lines[line] = str(f'{value}\n')

        with open(self.logic_ref_path, 'w') as ref:
            ref.writelines(lines)