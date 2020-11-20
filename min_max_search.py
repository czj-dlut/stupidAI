def weight(maps,x,y,Axis_X,Axis_Y,color):
    if (maps[x-Axis_X][y-Axis_Y]==color):
        return 0
    if (maps[x][y]== maps[x+Axis_X][y+Axis_Y] == maps[x+Axis_X*2][y+Axis_Y*2] == maps[x+Axis_X*3][y+Axis_Y*3] ==maps[x+Axis_X*4][y+Axis_Y*4]==color):
        return 50000
    if (maps[x+Axis_X][y+Axis_Y] == maps[x+Axis_X*2][y+Axis_Y*2] == maps[x+Axis_X*3][y+Axis_Y*3]==maps[x+Axis_X*4][y+Axis_Y*4] == color) and (maps[x][y]==maps[x+Axis_X*5][y+Axis_Y*5]==-1):
        return 10000
    if (maps[x+Axis_X][y+Axis_Y] == maps[x+Axis_X*2][y+Axis_Y*2] == maps[x+Axis_X*3][y+Axis_Y*3]==color) and (maps[x][y]==maps[x+Axis_X*4][y+Axis_Y*4]==-1):
        return 1000
    if (maps[x+Axis_X][y+Axis_Y] == maps[x+Axis_X*2][y+Axis_Y*2] == color) and (maps[x][y]==maps[x+Axis_X*3][y+Axis_Y*3]==-1): 
        return 100       
    if (maps[x+Axis_X][y+Axis_Y] ==color) and(maps[x][y]==maps[x+Axis_X*2][y+Axis_Y*2]==-1):
        return 10
    if (maps[x+Axis_X][y+Axis_Y] == maps[x+Axis_X*2][y+Axis_Y*2] == maps[x+Axis_X*3][y+Axis_Y*3]==maps[x+Axis_X*4][y+Axis_Y*4] == color) and (maps[x][y]!=maps[x+Axis_X*5][y+Axis_Y*5]) and ((maps[x][y]==(not(color))) or (maps[x+Axis_X*5][y+Axis_Y*5]==(not(color)))):  
        return 1000 
    if (maps[x+Axis_X][y+Axis_Y] == maps[x+Axis_X*2][y+Axis_Y*2] == maps[x+Axis_X*3][y+Axis_Y*3] == color) and (maps[x][y]!=maps[x+Axis_X*4][y+Axis_Y*4]) and ((maps[x][y]==(not(color)) or (maps[x+Axis_X*4][y+Axis_Y*4]==(not(color))))): 
        return 100
    if (maps[x+Axis_X][y+Axis_Y] == maps[x+Axis_X*2][y+Axis_Y*2] == color) and (maps[x][y]!=maps[x+Axis_X*3][y+Axis_Y*3]) and ((maps[x][y]==(not(color)) or (maps[x+Axis_X*3][y+Axis_Y*3]==(not(color))))):
        return 10
    if (maps[x+Axis_X][y+Axis_Y] == color) and (maps[x][y]!=maps[x+Axis_X*2][y+Axis_Y*2]) and ((maps[x][y]==(not(color)) or (maps[x+Axis_X*2][y+Axis_Y*2]==(not(color))))):
        return 1
    return 0

def value(maps,color):
    score=0
    for i in range(1,20):
        for j in range(1,20):
            score+=(weight(maps,i,j,0,1,color)+weight(maps,i,j,1,0,color)+weight(maps,i,j,1,1,color)+weight(maps,i,j,1,-1,color))
    return score
    
def around(maps,x,y):
    t=False
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if (maps[i][j]==0) or (maps[i][j]==1):
                t=True
                break
    return t

def AI_search(map):    
    map_virt=map
    MAX=-100000        #max搜索
    for x0 in range(1,20):
        for y0 in range(1,20):
            cut_alpha=False
            if (around(map_virt,x0,y0) and (map_virt[x0][y0]==-1)):
                map_virt[x0][y0]=1
                if value(map_virt,1)>=50000:
                    MAX=100000
                    (x_decision,y_decision)=(x0,y0)
                    map_virt[x0][y0]=-1 
                MIN=100000                  #        min搜索
                for x in range(1,20):
                    for y in range(1,20):
                        if around(map_virt,x,y) and (map_virt[x][y]==-1):
                            map_virt[x][y]=0
                            if (value(map_virt,0)>=10000) and (value(map_virt,1)<10000):
                                MIN=-100000
                                print("hello")
                                cut_alpha=True
                                map_virt[x][y]=-1
                                break
                            cut_beta=False
                            MAX_2=-100000 
                            for i in range(1,20):
                                for j in range(1,20):
                                    if around(map_virt,i,j) and (map_virt[i][j]==-1):
                                        map_virt[i][j]=1
                                        if (MAX_2<(value(map_virt,1)-value(map_virt,0))):       #估值函数
                                            MAX_2=(value(map_virt,1)-value(map_virt,0))
                                        map_virt[i][j]=-1
                                    if (MIN<MAX_2):
                                        cut_beta=True
                                        break
                                if cut_beta:
                                    break
                            if MIN>MAX_2:
                                MIN=MAX_2
                            map_virt[x][y]=-1
                            if MAX>MIN:       #alpha剪枝
                                cut_alpha=True
                                break
                    if cut_alpha:
                        break   
                if MAX<MIN:
                    MAX=MIN
                    (x_decision,y_decision)=(x0,y0)
                map_virt[x0][y0]=-1
    return x_decision,y_decision
            

                    




