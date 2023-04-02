class Board:
    def __init__(self, rows, columns):
        self.rows = 7
        self.columns = 6
        self.board = [[None for _ in range(columns)] for _ in range(rows)]

    def place_piece(self, row, column, piece):
        self.board[row][column] = piece

    def move_piece(self, row, column, new_row, new_column):
        piece = self.board[row][column]
        self.board[new_row][new_column] = piece
        self.board[row][column] = None

    def get_piece(self, row, column):
        return self.board[row][column]

    def fusion(self, row, column):
        pass  # Implementar la lógica de fusión de piezas aquí
