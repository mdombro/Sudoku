class Sudoku(): 

    def __init__(self):
        fo = open("sudoku1.txt")  ### PUT FILENAME HERE
        self.sudoku = []
        row=0
        
        for i in range(9):
            self.sudoku.append([])   

        while True:
            stri = fo.read(1)
            if stri == '':
                break
            if stri == '\n':
                row+=1
            if stri != ' ' and stri != '\n' and stri != 'x':
                self.sudoku[row].append(stri)
            elif stri != ' ' and stri != '\n' and stri == 'x':
                self.sudoku[row].append("987654321")
        fo.close() 

    def isUnique(self, cell):
        if cell == '9':
            return True
        elif cell == '8':
            return True
        elif cell == '7':
            return True
        elif cell == '6':
            return True
        elif cell == '5':
            return True
        elif cell == '4':
            return True
        elif cell == '3':
            return True
        elif cell == '2':
            return True
        elif cell == '1':
            return True
        else:
            return False
        
    def rowClear(self, row):
        for a in row:
            if self.isUnique(a):     # only check the unique numbers in a row
                for i in range(9):
                    if self.isUnique(row[i]):   # Skip over the unique numbers
                        pass
                    else:
                        row[i] = row[i].replace(a, '')
        return row
                        
    def ClearRows(self):
        for i in range(9):
            self.sudoku[i] = self.rowClear(self.sudoku[i])

    def colClear(self, col):
        column = self.rowClear(col)
        return column

    def ClearCols(self):
        col = []
        for i in range(9):
            for a in range(9):
                col.append(self.sudoku[a][i])
            col = self.colClear(col)
            for b in range(9):
                self.sudoku[b][i] = col[b]
            col = []   # clear the array

    def boxClear(self, box):
        boxNew = self.rowClear(box)
        return boxNew

    def ClearBoxes(self):
        box = []
        boxCoords = []
        newBox = [] 
        for row in range(3):
            for col in range(3):
                for c in range(9):
                    for d in range(9):
                        if int(c/3) == row and int(d/3) == col:
                            box.append(self.sudoku[c][d])
                            boxCoords.append([c,d])
                newBox = self.boxClear(box)
                for e in range(9):
                    self.sudoku[boxCoords[e][0]][boxCoords[e][1]] = newBox[e]
                box = []
                boxCoords = []
                newBox = []

    def print_sudoku(self, it):
        x = 0
        y = 0
        print("Iteration: ", it)
        for a in range(9):
            for b in self.sudoku[a]:
                if self.isUnique(b):
                    print(b, end=' ')
                else:
                    print('x', end=' ')
                x+=1
                if x == 3:
                    print(' ', end='')
                    x=0
            y+=1
            if y == 3:
                print()
                y=0
            print()
        print()

    def Complete(self):
        flag = True
        for i in range(9):
            for o in range(9):
                if not(self.isUnique(self.sudoku[i][o])):
                    flag = False
        return flag

def main():
    it = 1

    sudoku = Sudoku()
    
    while not(sudoku.Complete()):
        sudoku.ClearRows()
        sudoku.ClearCols()
        sudoku.ClearBoxes()
        sudoku.print_sudoku(it)
        it+=1
        
main()
