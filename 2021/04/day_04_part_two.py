class BingoBoard:
    def __init__(self, board):
        self.board = board
        self.width = len(self.board[0])
        self.height = len(self.board)
        
    def verify_winning_row(self):
        for row in self.board:
            count = 0
            for item in row:
                if item == 'X':
                    count += 1
            if count == self.width:
                return True
        return False

    def verify_winning_column(self):
        for column in range(0,self.width):
            count = 0
            for row in range(0,self.height):
                if self.board[row][column] == 'X':
                    count += 1
            if count == self.height:
                return True
        return False

    def verify_winning_board(self):
        return self.verify_winning_row() or self.verify_winning_column()

    def mark_board(self, number):
        number_found = False
        for row in self.board:
            for item in row:
                if item == number:
                    print("Found number:",number,"in row:",row)
                    number_found = True
                    row[row.index(item)] = 'X'
        return number_found

    def get_score(self, last_number):
        sum = 0
        for row in self.board:
            for item in row:
                try:
                    sum += int(item)
                except:
                    pass
        print("Sum:",sum)
        print("Last number:",last_number)
        print("Score:",sum * int(last_number))
        print(" ")
        return sum * int(last_number)


def play_game(bingo_boards, results):
    for result in results:
        if len(bingo_boards) == 0:
            return True
        print("Drawn number:",result)

        for board in bingo_boards:
            board.mark_board(result)
        for board in bingo_boards:
            if(board.verify_winning_board()):
                print("Winner!")
                print(board.board)
                board.get_score(result)
                bingo_boards.remove(board)

if __name__ == "__main__":
    f = open("input.txt", "r")

    data = []
    for line in f:
        data.append(line)
    
    # Get results and remove unwanted characters
    results = data[0].strip('\n').split(',')
    
    data.pop(0)
    data.pop(0)
    
    # Create a list of bingo boards
    bingo_boards = []
    board = []
    for line in data:
        if line == '\n':
            bingo_boards.append(BingoBoard(board))
            board = []
        else:
            board.append(line.strip('\n').split())

    # Creating last board
    bingo_boards.append(BingoBoard(board))

    play_game(bingo_boards, results)
    
    