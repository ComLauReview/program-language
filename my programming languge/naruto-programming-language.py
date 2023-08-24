import sys

print('Hi , Welcome to NARUTO !!! ')
print('........HELLO.........')
print('')
print('Selection Language , pls! "(vi ) or (en)" ')



#language programming 
def select_language():
    selectfl = input()
    if selectfl == 'vi':
        print('Da thiet lap ngon ngu tieng Viet! ')
    if selectfl == 'en':
        print('Set up English Language sucessfully!')


select_language()
print('............................')
def help_command_vi():
    print('Ban can ho tro command nao?')
    print('1: Lenh ')
    print('2: Kieu du lieu')
    helpcmd = input()
    if helpcmd == '1':
        print('In lenh ra man hinh: In')
        print('Bien : Bien ')
        print('Cau dieu kien : cdk ')
    if helpcmd == '2':
        print('Kieu Du lieu SO: so')
        print('Kieu Du lieu Chuoi: chuoi ')
print('')
print('Ban co can ho tro lenh khong?  (co) or (ko) ')
helpcm = input()
if helpcm == 'co':
    help_command_vi()
if helpcm == 'ko':
    print('..............')

print('')
print('Ban can mo trinh soan thao lenh hay khong? (co) or (ko) ')

openide = input()




#ide naruto:

def ide():
    ide_cmd = input()

    #In CODE
    if ide_cmd == 'In':
        In = input()
        print(In)

    #Bien CODE
    if ide_cmd == 'Bien':
        print('Ban muon tao them bao nhieu bien? ')
        Sobien = input()
        if SoBien == '1':
            Va = input()
        if SoBien == '2':
            Vl1 = input()
            Vl2= input()
            Va = [Vl1 , Vl2]
            



if openide == 'co':
    ide()
if openide ==" ko":
    sys.exit()

