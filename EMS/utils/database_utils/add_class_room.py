from backstage.models import ClassRoom

site = ['阶', '']
building = ['A', 'B']
code1 = ['1', '2', '3', '4', '5']
code2 = ['01', '02', '03', '04', '05',
         '06', '07', '08', '09', '10',
         '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20',
         '21', '22', '23', '24', '25',
         ]


def add_big():
    for i in range(2):
        for j in range(3):
            for k in range(5):
                ccrno = site[0] + building[i] + '-' + code1[j] + code2[k]
                ctype = '大'
                cnum = 200
                clr = ClassRoom.objects.create(crno=ccrno, crtype=ctype, contain_num=cnum)
                clr.save()


def add_mid():
    for i in range(2):
        for j in range(5):
            for k in range(11, 25):
                ccrno = building[i] + '-' + code1[j] + code2[k]
                ctype = '中'
                cnum = 120
                clr = ClassRoom.objects.create(crno=ccrno, crtype=ctype, contain_num=cnum)
                clr.save()


def add_small():
    for i in range(2):
        for j in range(5):
            for k in range(11):
                ccrno = building[i] + '-' + code1[j] + code2[k]
                ctype = '小'
                cnum = 50
                clr = ClassRoom.objects.create(crno=ccrno, crtype=ctype, contain_num=cnum)
                clr.save()


if __name__ == '__main__':
    add_big()
    add_mid()
    add_small()
