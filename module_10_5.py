from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline().strip()
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_l = datetime.now()

for i in filenames:
    read_info(i)

end_l = datetime.now()
print(end_l - start_l)

# Многопроцессный
if __name__ == '__main__':

    start_m = datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end_m = datetime.now()

    print(end_m - start_m)