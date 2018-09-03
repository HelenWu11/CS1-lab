""" 
    This is the skeleton to demonstrate how to put Lab 10 together. 
    It provides an example to show the use of doctest. Note the function,
    addone(x) presented below has an additional 4 lines after 
    the normal function description. The lines beginning with '>>>'
    indicate examples of how the function can be called, and 
    the lines immediately after represent the expected return
    from the call. So, for example, 'addone(1)' should return '2'
    and 'addone(0) should return 1. These lines provide examples
    for a potential user of the lab10 module, but more importantly
    for this lab, they work with the doctest module to allow us to
    do automated testing. 
    
    Look at the file 'test_driver.py' for an example of how to use
    this testing information. Then come back here and change 
    the answer for one or both of the addone examples to 
    an incorrect value and run the testing again to see how a failing
    test is reported.
"""


L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
if __name__ == "__main__":       
    def closest1(L1):
        '''
        closest1() returns two numbers that closest
        L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]    
        >>>closest1(L1)
        5.4 4.3
        '''
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
    
    
    '''
    def closest2(List): 
        
        closest2() returns two numbers that closest
        >>>closest2(L1)
        4.3 5.4
              
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
            
    
   
'''

