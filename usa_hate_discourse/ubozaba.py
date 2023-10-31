import json
tweets_file = "/home/zezin/Documents/tcc/elusa/tweets.jsonl"
final_file = "/home/zezin/Documents/tcc/elusa/week1d1.jsonl"
final_file2 = "/home/zezin/Documents/tcc/elusa/week1d2.jsonl"
final_file3 = "/home/zezin/Documents/tcc/elusa/week1d3.jsonl"
final_file4 = "/home/zezin/Documents/tcc/elusa/week1d4.jsonl"
final_file5 = "/home/zezin/Documents/tcc/elusa/week1d5.jsonl"
final_file6 = "/home/zezin/Documents/tcc/elusa/week1d6.jsonl"
final_file7 = "/home/zezin/Documents/tcc/elusa/week1d7.jsonl"
with open(tweets_file, 'r') as file, open(final_file, 'a') as outfile, open(final_file2, 'a') as outfile2, open(final_file3, 'a') as outfile3,open('count.txt', 'a') as countfile,open(final_file4, 'a') as outfile4,open(final_file5, 'a') as outfile5,open(final_file6, 'a') as outfile6,open(final_file7, 'a') as outfile7:
    for idx, line in enumerate(file):
        #if idx == 3:
        #    break
        data = json.loads(line)
        timestamp = data['tweet']['created_at']['$date']
        #print(timestamp)
        if timestamp < 1474675200000 and timestamp >= 1474588800000:#day 1#1 23-09/26-09 12am 
            outfile.write(json.dumps(data) + '\n')
        if timestamp < 1474761600000 and timestamp >= 1474675200000:#day 2#2 24-09 12am 
            outfile2.write(json.dumps(data) + '\n')
        if timestamp < 1474848000000 and timestamp >= 1474761600000:#day 3#3 25-09 12am 
            outfile3.write(json.dumps(data) + '\n')
        if timestamp < 1474934400000 and timestamp >= 1474848000000:#day 4#1 26-09 12am 
            outfile4.write(json.dumps(data) + '\n')
        if timestamp < 1475020800000 and timestamp >= 1474934400000:#day 5#2 27-09 12am 
            outfile5.write(json.dumps(data) + '\n')
        if timestamp < 1475107200000 and timestamp >= 1475020800000:#day 6#3 28-09 12am 
            outfile6.write(json.dumps(data) + '\n')
        if timestamp < 1475193600000 and timestamp >= 1475107200000:#day 7#3 29-09 12am 
            outfile7.write(json.dumps(data) + '\n')
        countfile.write(str(idx)+"\n")  
        print(idx)