import subprocess
from time import clock
from functools import reduce

commands = [
    'sleep 3',
    'ls -l /',
    'find /',
    'sleep 4',
    'find /usr',
    'date',
    'sleep 5',
    'uptime'
]

commands = list(map(lambda string: string.split(' '), commands))
times = []

for command in commands:
    proc = subprocess.Popen(command)
    startTime = clock()
    i = 0
    while proc.poll() == None:
        i += 1

    endTime = clock()
    deltaTime = endTime - startTime
    print("Time Elasped", deltaTime)
    times.append(deltaTime)

print()
print("************ Command Timings **************")
print()

for index, time in enumerate(times):
    fstr = "Command #{}: {:<9} ".format(index, reduce(lambda n0, n1: n0 + ' ' + n1, commands[index]))
    print(fstr, end='')
    print("took about {:04.4f} seconds".format(time))

print()
print("*********** Time Analysis ************")
print()
totalTime = reduce(lambda n0, n1: n0 + n1, times)
averageTime =  totalTime / len(times)
print("Average time: {:04.4f} seconds".format(averageTime))
print("Minimum time: {:04.4f} seconds".format(min(times)))
print("Maximum time: {:04.4f} seconds".format(max(times)))
print("Total elasped time: {:04.4f} seconds".format(totalTime))
print()
