import re

def Repetes(x):
    word = x.splitlines()
    max = 0
    eachLength = []
    output = ''
    for k in word:
        char = []
        max_of_this = 0
        for i in k:
            if not i in char:
                char.append(i)
            results = re.findall(i + "+", k)
            a = len(sorted(results)[len(results) - 1])
            if (max < a):
                max = a
            if (max_of_this < a):
                max_of_this = a
        eachLength.append(max_of_this)

    i = 0

    for j in eachLength:
        if j >= max:
            # print(word[i])
            output += word[i] + "\n"
        i += 1
    return output


word = """
89273777416
89273777167
89273776902
89273778915
89273778982
89273774216
89273771708
89273772982
89273775302
89273775244
89273777007
89273778140
89273778817
89273770487
89273772728
89273773272
89273777273
89273779341
89273779862
89273772225
"""

print(Repetes(word))
