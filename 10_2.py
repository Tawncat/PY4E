# This program counts the distribution of the hour of the day for each of the messages.
# You can pull the hour from the “From” line by finding the time string and then splitting
# that string into parts using the colon character. Once you have accumulated the
# counts for each hour, print out the counts, one per line, sorted by hour as shown below.

fhand = open('mbox-short.txt')
times = dict()

for line in fhand :
    words = line.split()

    if len(words) == 0 or words[0] != 'From' or len(words) < 5 :
        continue

    for word in words :
        search = ':' in word

        if search == True :
            time = word.split(':')
            #print(time)
            times[time[0]] = times.get(time[0], 0) + 1

tmp = list()
for key, value in list(times.items()) :
    tmp.append((key, value))

tmp.sort()


for key, value in tmp :
    print(key, value)
