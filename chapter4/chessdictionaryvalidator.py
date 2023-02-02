def chessvalidator(dict):
    black=0
    white=0
    pawnb=0
    pawnw=0
    x=list(dict.keys())
    y=list(dict.values())
    if 'bking' not in x:
        print("no king")
        return False
    if 'wking' not in b:
        print("no king")
        return False
    for i in y:
        i[0]=='b'
        black+=1
    for i in y:
        i[0]=='w'
        white+=1
    if black>=17:
        print("too many pieces")
        return False
    if white>=17:
        print("too many pieces ")
        return False
    for i in y:
        if i=='bpawn':
            pawnb+=1
        if i=='wpawn':
            pawnw+=1
        if pawnb or pawnw >=9:
            print("too many pawn")
            return False
    for i in x:
        if int(i[0])>=9:
            print("no space")
            return False
        if i[1] !='a' or i[1] !='b' or i[1] !='c' or i[1] !='d' or i[1] !='e' or i[1] !='f' or i[1] !='h':
            print('no space')
            return False
    for i in y:
        if i[0] != 'w' or i[0] !='b':
            print("wrong piece")
            return False
    v=('pawn','knight','bishop','rook','queen','king')
    for i in y:
        if i[1:] not in v:
            print('wrong')
            return False
pieceposition={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
chessvalidator(pieceposition)
            
        
    