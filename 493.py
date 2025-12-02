#https://aceptaelreto.com/problem/statement.php?id=493

# stuck on this one for a while

# hardcode the 7 tetris pieces
# create  a rotation function to rotate 
# precompute or compute at the moment the rotations

# read the cols and pieces
# init some repr of the board
# read each pieces (id, rotation, position)

# some ideas:
# do it normally
# only track cols as a list of the highest position in each of them, compute placements acordingly
# represent pieces as how much height in each col. harder rotation though
# use square repres for easier transposition

pieces = {
    1: [
        [1,1,1,1]],

    2: [[1,0,0],
        [1,1,1]],

    3: [[0,0,1],
        [1,1,1]],

    4: [[1,1],
        [1,1]],

    5: [[0,1,1],
        [1,1,0]],

    6: [[0,1,0],
        [1,1,1]],

    7: [[1,1,0],
        [0,1,1]]
}

class Tetris():
    
    def __init__(self, cols, pieces):
        self.cols = cols
        self.pieces = pieces
        self.board = [[0 for _ in range(cols)]]
        self.highest_occupied_row = 0

    def place(self, piece, pos):
        '''Placement is based on the given piece's lowest left corner's column'''

        # check if enough vertical space, else add more

        # idea: each placement, we can track the highest point and store it
        # we can also always add extra 4 height ( the max possible height)

        if self.highest_occupied_row < len(piece):
            # TODO check if this is right
            lacking_rows = abs(self.highest_occupied_row - len(piece))
            self.board.extend(([0]*self.cols) * lacking_rows)

        # scan-search for available placements in the columns
        nand = lambda x, y: 0b1 ^ (x & y) # xor(1, (x and y)) = not(x and y)
        low_col, hi_col = pos, pos + len(piece[-1])
        
        result =  None # TODO to break in special cases, must check

        # we search for the first to fail and place it on the previous row
        for idx, row in enumerate(self.board):
            
            result = idx 

            boolmask = [nand(x, y) for x, y in 
                zip(row[low_col : hi_col], piece[-1])]
            
            if not all(boolmask):
                result -= 1
                break
            else: 
                continue

        if (new_hi := row - len(piece)) < self.highest_occupied_row:
            self.highest_occupied_row = new_hi
            
        # now, we need to insert a n x m matrix (piece) in the board matrix
        # iter over the cols and row seq until completion

        # not directly the result, since it's the piece's lower left corner
        result -= len(piece)-1 # reduce by the piece's length to get upper left corner
        for i in range(result, result + len(result[0])): # if the row was p.x., 3, iter between (3, 3+len(p[0]))
            for i in range(pos):
                self.board[result][row] = ...# TODO


    def test_scan_search(self, piece, pos):
        '''this should return the lowest valid row to place the piece
        Assumes the board matrix is big enough, doesn't place the piece '''

        # scan-search for available placements in the columns
        nand = lambda x, y: 0b1 ^ (x & y) # xor(1, (x and y)) = not(x and y)
        low_col, hi_col = pos, pos + len(piece[-1]) 
        result =  None # TODO to break in special cases, must check

        # we search for the first to fail and place it on the previous row
        for idx, row in enumerate(self.board):
            
            result = idx 

            boolmask = [nand(x, y) for x, y in 
                 zip(row[low_col : hi_col], piece[-1])]
            
            # boolmask = []
            # for x, y in zip(row[low_col : hi_col], piece[-1]):
            #     t = nand(x, y)
            #     print(t)
            #     boolmask.append(t)
            
            print("Mask for each row: ", idx, boolmask)
            
            if not all(boolmask):
                result -= 1
                break
            else: 
                continue

        return result


    def rotate(self, id, rot):
        '''turn rows into columns "clockwise".
        Rot is degrees, either 0, 90, 180, 270.'''
        # FIXME THIS SHOULD BE COUTER CLOCKWISE!!!
            
        piece = self.pieces[id]
        for _ in range(rot//90):
            
            n, m = len(piece), len(piece[0]) # rows and cols
            max_n = n - 1

            # create new matrix with inverted dims
            new = [[0]*n for _ in range(m)]

            for idx in range(m*n): # get row and col idxs, swap old and new
                i, j = idx//m, idx%m
                new[j][max_n-i] = piece[i][j]

            piece = new
        
        return piece

    def get_col_heights(self):
        ...

    def __str__(self):
        '''for debugging'''
        return "\n".join([str(i) for i in self.board])
       

    def _place(self, piece, row, col):
        '''assume row and col are top left corner of piece for now'''
       
        assert col <= self.cols - len(piece[0]), "Col Out of bounds"
        assert row <= len(self.board) - len(piece), "Row out of bounds"

        start_col, end_col = col, col + len(piece[0])

        # TODO might need reversing if row is bottom left
        for idx, r in enumerate(piece):
            self.board[idx+row][start_col:end_col] = r # TODO MUST RECALCULATE THIS

    def NEW_place():
        # new approach: change piece representation:
        # then, just add up for each column, and youre good to go.
        # # TODO piece rotates COUTERCLOCKWISE
        pieces = {
            1: {
                0: [1,1,1,1],
                90: [4],
                180: [1,1,1,1],
                270: [4]
            },
            2: {
                0: [2,1,1],
                90: [1,3],
                180: [2,2,2],
                270: [3,3]
            },
            3: {
                0: [1,1,2],
                90: [3,3],
                180: [2,2,2],
                270: [3,1]
            },
            4: {
                0: [2,2],
                90: [2,2],
                180: [2,2],
                270: [2,2]
            },
            5: {
                0: [1,2,2],
                90: [],
                180: [],
                270: []
            },
            2: {
                0: [],
                90: [],
                180: [],
                270: []
            }
        }
        # we can check the pieces "bounding box" against the board starting from there,
        # and if all the results of nand

    def _extend_board(self, n):
        self.board.extend([[0 for _ in range(self.cols)] for _ in range(n)])


def test_placing():
    t = Tetris(5, pieces)
    t._extend_board(9)
    print(t)

    print()
    x = t.rotate(2, 90)
    t._place(x, 7, 0)
    t._place(t.pieces[4], 6, 3)
    print(t)

def test_scan():
    t = Tetris(5, pieces)
    t._extend_board(9)

    x = t.rotate(1, 90)
    t._place(x, 6, 0)
    t._place(t.pieces[3], 8, 2)
    print(t)

    p = t.rotate(1, 0)
    print()
    for i in p:
        print(i)
    
    col = 1
    print(" ^^^  placing in col: ", col)
    valid_row = t.test_scan_search(p, col)

    print(valid_row)


test_scan()
    

    



# t._place(2, 8, 0)
# print(t)


# test piece rotation
# for piece in pieces:
#     rot1 = t.rotate(piece, 90)
#     for row in rot1:
#         print(row)
#     rot2 = t.rotate(piece, 180)
#     for row in rot2:
#         print(row)
#     print()

# main loop
# while n_c_p := int(input().split()) != [0,0]:
#     n_col, n_piec = n_c_p 

#     board = Tetris(n_col, pieces)

#     for _ in range(n_piec):
#         id, rot, pos = int(input().split())
        
#         piece = board.rotate(id, rot)

#         board.place(piece, pos)

#         heights : list = board.get_col_heights()

#         print(*heights)
        




