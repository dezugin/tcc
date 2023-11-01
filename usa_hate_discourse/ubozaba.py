import json
tweets_file = "/home/zezin/Documents/tcc/elusa/tweets.jsonl"
final_file = "/home/zezin/Documents/tcc/elusa/week3d1.jsonl"
final_file2 = "/home/zezin/Documents/tcc/elusa/week3d2.jsonl"
final_file3 = "/home/zezin/Documents/tcc/elusa/week3d3.jsonl"
final_file4 = "/home/zezin/Documents/tcc/elusa/week3d4.jsonl"
final_file5 = "/home/zezin/Documents/tcc/elusa/week3d5.jsonl"
final_file6 = "/home/zezin/Documents/tcc/elusa/week3d6.jsonl"
final_file7 = "/home/zezin/Documents/tcc/elusa/week3d7.jsonl"
with open(tweets_file, 'r') as file, open(final_file, 'a') as outfile, open(final_file2, 'a') as outfile2, open(final_file3, 'a') as outfile3,open('count.txt', 'a') as countfile,open(final_file4, 'a') as outfile4,open(final_file5, 'a') as outfile5,open(final_file6, 'a') as outfile6,open(final_file7, 'a') as outfile7:
    for idx, line in enumerate(file):
        #if idx == 3:
        #    break
        data = json.loads(line)
        timestamp = data['tweet']['created_at']['$date']
        #print(timestamp)
        if timestamp < 1476792000000 and timestamp >= 1476705600000:#day 1#1 17-10/26-09 12 pm 
            outfile.write(json.dumps(data) + '\n')
        if timestamp < 1476878400000 and timestamp >= 1476792000000:#day 2#2 18-10 12 pm 
            outfile2.write(json.dumps(data) + '\n')
        if timestamp < 1476964800000 and timestamp >= 1476878400000:#day 3#3 19-10 12 pm 
            outfile3.write(json.dumps(data) + '\n')
        if timestamp < 1477051200000 and timestamp >= 1476964800000:#day 4#1 20-10 12 pm 
            outfile4.write(json.dumps(data) + '\n')
        if timestamp < 1477137600000 and timestamp >= 1477051200000:#day 5#2 21-10 12 pm 
            outfile5.write(json.dumps(data) + '\n')
        if timestamp < 1477224000000 and timestamp >= 1477137600000:#day 6#3 22-10 12 pm 
            outfile6.write(json.dumps(data) + '\n')
        if timestamp < 1477310400000 and timestamp >= 1477224000000:#day 7#3 23-10 12 pm 
            outfile7.write(json.dumps(data) + '\n')
        """
                if timestamp < 1475841600000 and timestamp >= 1475755200000:#day 1#1 06-10/26-09 12 pm 
            outfile.write(json.dumps(data) + '\n')
        if timestamp < 1475928000000 and timestamp >= 1475841600000:#day 2#2 07-10 12 pm 
            outfile2.write(json.dumps(data) + '\n')
        if timestamp < 1476014400000 and timestamp >= 1475928000000:#day 3#3 08-10 12 pm 
            outfile3.write(json.dumps(data) + '\n')
        if timestamp < 1476100800000 and timestamp >= 1476014400000:#day 4#1 09-10 12 pm 
            outfile4.write(json.dumps(data) + '\n')
        if timestamp < 1476187200000 and timestamp >= 1476100800000:#day 5#2 10-10 12 pm 
            outfile5.write(json.dumps(data) + '\n')
        if timestamp < 1476273600000 and timestamp >= 1476187200000:#day 6#3 11-10 12 pm 
            outfile6.write(json.dumps(data) + '\n')
        if timestamp < 1476360000000 and timestamp >= 1476273600000:#day 7#3 12-10 12 pm 
            outfile7.write(json.dumps(data) + '\n')
                if timestamp < 1474675200000 and timestamp >= 1474588800000:#day 1#1 23-09/26-09 12 pm 
            outfile.write(json.dumps(data) + '\n')
        if timestamp < 1474761600000 and timestamp >= 1474675200000:#day 2#2 24-09 12 pm 
            outfile2.write(json.dumps(data) + '\n')
        if timestamp < 1474848000000 and timestamp >= 1474761600000:#day 3#3 25-09 12 pm 
            outfile3.write(json.dumps(data) + '\n')
        if timestamp < 1474934400000 and timestamp >= 1474848000000:#day 4#1 26-09 12 pm 
            outfile4.write(json.dumps(data) + '\n')
        if timestamp < 1475020800000 and timestamp >= 1474934400000:#day 5#2 27-09 12 pm 
            outfile5.write(json.dumps(data) + '\n')
        if timestamp < 1475107200000 and timestamp >= 1475020800000:#day 6#3 28-09 12 pm 
            outfile6.write(json.dumps(data) + '\n')
        if timestamp < 1475193600000 and timestamp >= 1475107200000:#day 7#3 29-09 12 pm 
            outfile7.write(json.dumps(data) + '\n')
        """
        countfile.write(str(idx)+"\n")  
        print(idx)