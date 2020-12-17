def getReverseSentece(string, token):
    r = ' '.join(string.split(token)[::-1])
    return r

print(getReverseSentece('Siga a Geek2Code',' '))
print(getReverseSentece('Siga a sua solução nos stories',' '))