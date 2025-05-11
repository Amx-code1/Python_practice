if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list = []
    i,j,k = 0,0,0
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if ((i+j+k) != n):
                    list.append([i,j,k])
            k += 1
        j += 1
    k += 1
                    
    print(list)
  
                
                    
    
