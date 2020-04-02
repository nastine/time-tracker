import datetime


class Tracker:

    def __init__(self, file_name, encoding='utf-8'):
        self.txt_file = open(file_name, 'w', encoding=encoding)

    def __enter__(self):
        return self

    def start_training(self):
        the_start = datetime.datetime.utcnow()
        return(the_start)

    def write_time(self, action):
        self.txt_file.write(f'{datetime.datetime.utcnow()}: {action}\n')

    def start_excercise(self):
        act = input('Начинаем? (нажмите "Enter")')
        start = datetime.datetime.utcnow()
        return start

        

    def end_excercise(self):
        act = input('Закончили? (нажмите "Enter")')
        end = datetime.datetime.utcnow()
        return end

        
    def beak_excecise(self):
        act = input('Отдохнули? (нажмите "Enter")')
        beak_ex = datetime.datetime.utcnow()
        return beak_ex

        
    def delta_training(self, start, end):
        delta = end - start
        self.txt_file.write(f'Время упражнений:{str(delta.seconds)} секунд\n')

    def delta_rest(self, break_ex, end):
        delta = break_ex - end
        self.txt_file.write(f'Время отдыха:{str(delta.seconds)} секунд\n')

    def bye_bye(self, the_start):
        the_end = datetime.datetime.utcnow()
        delta = the_end - the_start
        print(f'Время начала тренировки: {the_start.strftime("%H:%M:%S")}. \nВремя окончания тренировки: {the_end.strftime("%H:%M:%S")}.\
             \nОбщее время тренировки - {delta.seconds // 3600}:{(delta.seconds % 3600) // 60}:{delta.seconds % 60}.')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.write_time(f'error: {exc_val}')
        
        self.txt_file.close()

def welcome():
    with open('welcome.txt') as file:
        print(file.read())

def exercise(f):
    
    start = f.start_excercise()
    end = f.end_excercise()
    f.delta_training(start, end)
    beak_ex = f.beak_excecise()
    f.delta_rest(beak_ex, end)
    another_ex = input('Хотите выполнить ещё одно упражнение? (y/n)')
    if another_ex == 'y':
        exercise(f)
    else:
        print(f'\nВот статистика по Вашей тренировке: \n')  

def statistics(f):
    with open("training.txt") as stat:
        time = list(stat.read().split("\n"))
        whole_training = {}
        for lines in time:
            while lines != '':
                name = lines.split(":")[0]
                time_sec = lines.split(":")[1]
                time_sec = time_sec.split()
                if name not in whole_training:
                    whole_training[name] = int(time_sec[0])
                else:
                    whole_training[name] += int(time_sec[0])
                break
        for activities, times in whole_training.items():
            print(f'{activities} - {times // 3600}:{(times % 3600) // 60}:{times % 60}')


if __name__ == '__main__':
    with Tracker('training.txt') as f:
        welcome()
        the_start = f.start_training()
        exercise(f)
        f.bye_bye(the_start)
    statistics(f)
    print("\nВы сегодня хорошо поработали. До следующей тренировки!")

            