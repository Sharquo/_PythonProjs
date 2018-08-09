import urllib.request as request


def checkgrammar(word):
    if "cie" in word:
        return False
    elif "ei" in word.replace("cei", ""):
        return False
    else:
        return True


def countwords(url):
    response = request.urlopen(url)
    data = response.read
    text = data.decode('utf-8')
    result = 0

    for word in text.splitlines():
        if not checkgrammar(word):
            result += 1

    print(result)


countwords("https://norvig.com/ngrams/enable1.txt")
