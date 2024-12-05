class wonkCSV():
    def wonkCSV(file):
        file = str(file)
        if type(file) != str: raise ValueError('File not in string format.')
        if file.endswith('.csv') != True: raise ValueError("File is not in csv format.")
        try: opened = open(file, 'r')
        except: raise PermissionError("Cannot open file. Check permissions.")

        file_lines = []
        with open(file, 'r') as file_opened:
            for line in file_opened.readlines():
                line = str(line).replace('\n', '')
                file_lines.append(line)
        
        return file_lines