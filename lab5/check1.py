import lab05_util
restaurants = lab05_util.read_yelp('yelp.txt')
def print_info(restaurant):
    print(restaurant[0]+'('+restaurant[5]+')')
    print('\t'+''.join(restaurant[3].split('+')[0]))
    print('\t'+''.join(restaurant[3].split('+')[1]))
    total = 0
    for n in restaurant[6]:
        total+=n
    ave = total/len(restaurant[6])
    print("Average Score: {:.2f}".format(ave))



print_info(restaurants[0])
print()
print_info(restaurants[4])