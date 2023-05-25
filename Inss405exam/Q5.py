user1=input ('Enter final grade for User1:')
user2=input ('Enter final grade for User2:')
user3=input ('Enter final grade for user3:')
user4=input ('Enter final grade for user4:')
user5=input ('Enter final grade for user5:')
user6=input ('Enter final grade for user6:')
user7=input ('Enter final grade for user7:')


sum = int(user1) + int(user2) + int(user3) + int(user4) + int(user5) + int(user6) + int(user7)
print(sum)
average_score =int(sum)/7
print(average_score)


if average_score >= 90:
    print('A')
elif average_score >= 80:
    print('B')
elif average_score >= 70:
     print('C')
elif average_score >= 60:
    print('D')
elif average_score >= 50:
    print('E')
else:
    print ('F')




