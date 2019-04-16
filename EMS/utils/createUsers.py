from random import randint, choice, choices
import sys
sys.path.append('..')
from backstage.models import User, Announcement, Dept


the_name_list = ['Aaron', 'Abel', 'Abraham', 'Adam', 'Adrian', 'Aidan', 'Alva', 'Alex', 'Alexander', 'Alan', 'Albert',
                 'Alfred', 'Andrew', 'Andy', 'Angus', 'Anthony', 'Apollo', 'Arnold', 'Arthur', 'August', 'Austin',
                 'Marcus', 'Marcy', 'Mark', 'Marks', 'Mars', 'Marshal', 'Martin', 'Marvin', 'Mason', 'Matthew', 'Max',
                 'Michael', 'Mickey', 'Mike', 'Nathan', 'Nathaniel', 'Neil', 'Nelson', 'Nicholas', 'Nick', 'Noah',
                 'Norman', 'Randall', 'Randal', 'Randolph', 'RandyRandallRandolph', 'Ray', 'Raymond', 'Reed', 'Rex',
                 'Richard', 'Richie', 'Rick', 'Ricky', 'Ritchie', 'Riley', 'Robert', 'Robin', 'Robert', 'Robinson', 'Robinson', 'Rock',
                 'Roger', 'Ronald', 'Rowan', 'Roy', 'Ryan', 'Jack', 'Jackson', 'Jacob', 'James', 'Jacob', 'Jason', 'Jay',
                 'Jeffery', 'Jerome', 'Jerry', 'Gerald', 'Jeremiah', 'Jerome', 'Jesse', 'JimJames', 'Jimmy', 'James', 'Joe', 'Joseph',
                 'John', 'Johnny', 'Jonathan', 'Jordan', 'JoseJoseph', 'Joshua', 'Justin']


def init_dept():
    pass


def add_user(f:int, t:int, years=None):
    """

    :param f: number from f
    :param t: number to t
    """
    id = ''
    depset = Dept.objects.all()
    if years:
        prefix = years
        for cnt in range(f, t):
            suffix = '%06d' % cnt
            id = str(prefix) + str(suffix)
            nickname = choice(the_name_list)
            psw = nickname + 'password'
            sex = choice(['male', 'female'])
            email = id + '@mail.buct.edu.cn'
            sty = prefix
            endy = str(int(prefix) + 4)
            grant = choice(['0', '1', '2', '3'])
            u = User.objects.create(
                codename=id,
                password=psw,
                nickname=nickname,
                sex=sex,
                email=email,
                start_year=sty,
                end_year=endy,
                grant=grant,
                department=choice(depset)
            )
            u.save()
    else:
        for cnt in range(f, t):
            prefix = randint(1990, 2020)
            suffix = '%06d' % cnt
            id = str(prefix) + str(suffix)
            nickname = choice(the_name_list)
            psw = nickname + 'password'
            sex = choice(['male', 'female'])
            email = id + '@mail.buct.edu.cn'
            sty = prefix
            endy = str(int(prefix) + 4)
            grant = choice(['0', '1', '2', '3'])
            u = User.objects.create(
                codename=id,
                password=psw,
                nickname=nickname,
                sex=sex,
                email=email,
                start_year=sty,
                end_year=endy,
                grant=grant,
                department=choice(depset)
            )
            u.save()


if __name__ == '__main__':
    add_user(11100, 11120)
    pass
