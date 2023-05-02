"""
    name:  Abdallah Derbala
    
"""
from collections import defaultdict
from functools import reduce


# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


def Average(lst):
    return round(reduce(lambda a, b: a + b, lst) / len(lst), 2)


def main():
    file_name = input()
    averages = defaultdict(dict)
    with open(file_name, 'r') as file:
        file.readline()
        for line in file:
            time, n, answer, _, type = line.split(',')
            time = int(float(time))
            answer = float(answer)
            if 'exact' not in type:
                if time not in averages[n]:
                    averages[n][time] = [answer]
                else:
                    averages[n][time].append(answer)
    for size in averages:
        for time in averages[size]:
            averages[size][time] = Average(averages[size][time])
    output = open("averages.csv", 'x')
    output0 = ""
    output1 = ""
    output5 = ""
    output10 = ""
    output30 = ""
    output60 = ""
    output300 = ""
    output600 = ""
    output1200 = ""


    for i in averages:
        for time in averages[i]:
            if time == 0:
                output0 += f"{i},{averages[i][time]}\n"
            elif time == 1:
                output1 += f"{i},{averages[i][time]}\n"
            elif time == 5:
                output5 += f"{i},{averages[i][time]}\n"
            elif time == 10:
                output10 += f"{i},{averages[i][time]}\n"
            elif time == 30:
                output30 += f"{i},{averages[i][time]}\n"
            elif time == 60:
                output60 += f"{i},{averages[i][time]}\n"
            elif time == 300:
                output300 += f"{i},{averages[i][time]}\n"
            elif time == 600:
                output600 += f"{i},{averages[i][time]}\n"
            elif time == 1200:
                output1200 += f"{i},{averages[i][time]}\n"
    output.write("Time,0\nSize,Average\n")
    output.write(output0)

    output.write("Time,1\nSize,Average\n")
    output.write(output1)

    output.write("Time,5\nSize,Average\n")
    output.write(output5)

    output.write("Time,10\nSize,Average\n")
    output.write(output10)

    output.write("Time,30\nSize,Average\n")
    output.write(output30)

    output.write("Time,60\nSize,Average\n")
    output.write(output60)

    output.write("Time,300\nSize,Average\n")
    output.write(output300)

    output.write("Time,600\nSize,Average\n")
    output.write(output600)

    output.write("Time,1200\nSize,Average\n")
    output.write(output1200)
            


if __name__ == "__main__":
    main()