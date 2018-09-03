import lab05_util
restaurants = lab05_util.read_yelp('yelp.txt')

def print_info(restaurant):
    print(restaurant[0]+'('+restaurant[5]+')')
    print('\t'+''.join(restaurant[3].split('+')[0]))
    print('\t'+''.join(restaurant[3].split('+')[1]))
    total = 0
    for n in restaurant[6]:
        total+=n

    if len(restaurant[6])<3:
        ave = total/len(restaurant[6])

    elif len(restaurant[6])>=3:
        restaurant[6].sort()
        ave = (total-\
           restaurant[6][0]-\
           restaurant[6][len(restaurant[6])-1])\
        /(len(restaurant[6])-2)

    if ave>=0 and ave<2:
        print("This restaurant is rated bad, based on",len(restaurant[6]),"reviews.")
    elif ave>=2 and ave<3:
        print("This restaurant is rated average, based on",len(restaurant[6]),"reviews.")
    elif ave>=3 and ave<4:
        print("This restaurant is rated above average, basedd on",len(restaurant[6]),"reviews.")
    elif ave>=4 and ave<=5:
        print("This restaurant is rated very good, base on",len(restaurant[6]),"reviews.")        


number = int(input("Enter an id of a restaurant => "))
def yours_restaurant(number):
    for n in range(len(restaurants)-1):
        if n == number:
            return restaurants[number]
    return False
if yours_restaurant(number) == False:
    print("Restaurant not find")
else:
    print_info(yours_restaurant(number))
    
