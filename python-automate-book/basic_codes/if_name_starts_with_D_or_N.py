#coding=UTF-8
def is_friend(name_friend):
    return name_friend[0] == 'D' or name_friend[0] == 'N'
print is_friend('Daniel')
print is_friend('Ned')
print is_friend('Moe')
