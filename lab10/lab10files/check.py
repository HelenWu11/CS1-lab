import random
import time

L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
if __name__ == "__main__":
    def closest1(L1):
        if len(L1)<2:
            return None,None
        else:
            cloest = []
            for n in range(len(L1)):
                for item in L1[n:]:
                    if item != L1[n]:
                        differ = abs(L1[n]-item)
                        cloest.append((differ,L1[n],item))
            cloest.sort()
            return cloest[0][1],cloest[0][2]
        
    (x,y) = closest1(L1)
    print(x, y)    
    

    def closest2(List): 
        list_copy = List.copy()
        list_copy.sort()
        differ = abs(list_copy[0]-list_copy[1])
        close1 = list_copy[0]
        close2 = list_copy[1]
        for n in range(len(list_copy)-1):
            if abs(list_copy[n]-list_copy[n+1])<differ:
                differ = abs(list_copy[n]-list_copy[n+1])
                close1,close2 = list_copy[n],list_copy[n+1]
        return close1,close2
    
    (a,b) = closest2(L1)
    print(a,b)           
    


#check3
if __name__ == "__main__":
    n = int(input("Enter a value to test==>"))
    values = []
    i = 0
    while i<n:
        values.append(random.uniform(0.0,n))
        i += 1
    
    
    s1 = time.time()
    (s1x,s2y) = closest1(values)
    t1 = time.time()-s1
    print("Ver1: closest({:.2f},{:.2f}); time: {:.3f} seconds".format(s1x,s2y,t1))
    
    s2 = time.time()
    (s2x,s2y) = closest2(values)
    t2 = time.time() - s2
    print("Ver2: closest({:.2f},{:.2f}); time: {:.3f} seconds".format(s2x,s2y,t2))
    
    if t1 < t2:
        print('t1')
        print(closest1(L1))
    else:
        print('t2')
        print(closest2(L1))
   