#word puzzle

puzzle=[
    ["k","e","r","e","m","a","c","a"],
    ["q","w","e","e","m","a","v","a"],
    ["k","e","r","e","m","c","c","a"],
    ["k","e","r","e","i","a","c","a"],
    ["k","e","r","o","m","i","c","a"],
    ["k","e","g","e","m","l","c","a"],
    ["k","l","r","i","l","a","k","a"],
    ["u","e","r","e","m","a","w","x"],
    ]
lenline=len(puzzle[0])
lenpuzzle=len(puzzle)


words=["kerem","ali","avcioglu","xk"]

positions=[]
def solve():

    for word in words:
        ln=len(word)
        for i,line in enumerate(puzzle):
            for j,cell in enumerate(puzzle):
                if (ln+i-1)<lenline:   
                    myword="".join([cell[i+x] for x in range(ln)])
                    if myword==word:
                        print("bulundu yatay",i,j,word)
                    elif myword[::-1]==word:
                        print("bulundu yatay",i,j,word)

                if ln+j-1<lenpuzzle:
                    myword="".join([puzzle[j+x][i] for x in range(ln)])
                    if myword==word:
                        print("bulundu dikey",i,j,word)
                    elif myword[::-1]==word:
                        print("bulundu dikey",i,j,word)

                if (i-ln>0) and j-ln>0 and(ln+i-1)<lenline and ln+j-1<lenpuzzle:
                    myword="".join([puzzle[j+x][i+x] for x in range(ln)])
                    if myword==word:
                        print("bulundu capraz",i,j,word)
                    elif myword[::-1]==word:
                        print("bulundu capraz",i,j,word)

                    myword="".join([puzzle[j-x][i-x] for x in range(ln)])
                    if myword==word:
                        print("bulundu capraz",i,j,word)
                    elif myword[::-1]==word:
                        print("bulundu capraz",i,j,word)

solve()


def get_frees(puzzle,typ,ln):
    frees=[]
    match (typ):
        case "horizontal":
            for i,line in enumerate(puzzle):
                for j,cell in enumerate(puzzle):
                    try:
                        word="".join([cell[i+q] for q in range(ln)])
                        if (ln+i-1)<lenline and word=="":  
                            frees.append((i,j))
                    except:pass

        case "vertical":
            for i,line in enumerate(puzzle):
                for j,cell in enumerate(puzzle):
                    try:
                        word="".join([puzzle[i+q][j] for q in range(ln)])
                        if ln+j-1<lenpuzzle and word=="":
                            frees.append((i,j))
                    except:pass

        case "cross1":
            for i,line in enumerate(puzzle):
                for j,cell in enumerate(puzzle):
                    try:
                        word="".join([puzzle[i+q][j+q] for q in range(ln)])
                        if (i-ln>0) and j-ln>0 and(ln+i-1)<lenline and ln+j-1<lenpuzzle and word=="":
                            frees.append((i,j))
                    except:pass
        case "cross2":
            for i,line in enumerate(puzzle):
                for j,cell in enumerate(puzzle):
                    try:
                        word="".join([puzzle[i-q][j-q] for q in range(ln)])
                        if (i-ln>0) and j-ln>0 and(ln+i-1)<lenline and ln+j-1<lenpuzzle and word=="":
                            frees.append((i,j))
                    except:pass
            

    

    return frees


def update_puzzle(puzzle,typ,val,word,x,y):
    frees=[]
    if val>0:
        pass
    else:
        word=word[::-1]
    match (typ):
        case "horizontal":
            puzzle[y][x:x+len(word)]=word
                
        case "vertical":
            for a in range(len(word)):
                puzzle[y+a][x]=word[a]

        case "cross1":
            for a in range(len(word)):
                puzzle[y+a][x+a]=word[a] 
        case "cross2":
            for a in range(len(word)):
                puzzle[y-a][x-a]=word[a]

    return puzzle
            
    
def show_puzzle(puzzle):
    print("-"*16)
    for x in puzzle:
        print(x)
def generate_puzzle(x,y,words):
    global puzzle
    puzzle=[["" for a in range(x)] for b in range(y)]
    show_puzzle(puzzle)
    import random

    random.shuffle(words)
    assert len(sorted(words,key=len)[-1])<=x and len(sorted(words,key=len)[-1])<=y
    types=["horizontal","vertical","cross1","cross2"]
    random.shuffle(types)
    values=[-1,1]
    random.shuffle(values)
    possibles=[]
    def do(word):
        global puzzle
        for mytype in types:
            for myvalue in values:
                possibles=get_frees(puzzle,mytype,len(word))
                if possibles:
                    pos=random.choice(possibles)
                    puzzle=update_puzzle(puzzle,mytype,myvalue,word,pos[0],pos[1])
                    return
    try:
        for word in words:
            do(word)
    except:
        raise "ERROR!?"
        
        
        

    

    
    
generate_puzzle(8,8,words)
show_puzzle(puzzle)            



                
                    

                    

                
            


    
    
