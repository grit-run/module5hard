from time import time, sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return hash(self.password)

    def __eq__(self, other):
        if isinstance(User, other):
            return self.password == other.password
        return False


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.current_user = None
        self.users = {}
        self.videos = {}

    def log_in(self, nick, passw):
        if nick in self.users.keys() and self.users[nick][0] == passw:
            self.current_user = nick
        else:
            print("wrong", self.users[nick][0])

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user.nickname not in self.users.keys():
            self.users[user.nickname] = [user.password, user.age]
            self.log_in(nickname, password)
        else:
            print('Пользователь {} уже существет'.format(nickname))

    #
    def add(self, *args):
        for arg in args:
            if isinstance(arg, Video):
                if arg.title not in self.videos:
                    self.videos[arg.title] = arg.duration, arg.time_now, arg.adult_mode

    def get_videos(self, search_word):
        movie_name_list = []
        for key in self.videos.keys():
            if search_word.lower() in key.lower():
                movie_name_list.append(key)
        return movie_name_list

    def watch_video(self, movie_name):
        if self.current_user is not None:

            if self.get_videos(movie_name):
                print(movie_name)
                if self.videos[movie_name][2] is True and self.users[self.current_user][1] <= 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    self.log_out()

                else:
                    for i in range(1, self.videos[movie_name][0] + 1):
                        print(i, end=" ")
                        sleep(0.5)
                    print("Конец видео")

            else:
                print("Такого фильма нет")
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Странные дни', 7, adult_mode=True)

# Добавление видео
ur.add(v1, v2, v3)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print(ur.get_videos('ни'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video("Странные дни")        # доп.проверка
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
