import sys

if __name__ == "__main__":
    inputFile = open(sys.argv[1],'r')
    n = int(inputFile.readline()) # test cases
    counter = 1
    for line in inputFile:
        numbers = line.strip().split(" ")
        c = float(numbers[0]) # cookies
        f = float(numbers[1]) # rate per farm
        x = float(numbers[2]) # target
        rate = 2
        bestTime = x / rate
        timeToCookie = (c / rate)
        rate += f
        while bestTime >= timeToCookie + (x / rate):
            bestTime = timeToCookie + (x / rate)
            timeToCookie = timeToCookie + (c / rate) 
            rate += f
        print "Case #{0}: {1}".format(counter, bestTime)
        counter += 1
