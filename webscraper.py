def main():
    import urllib
    from urllib.parse import urlparse
    from bs4 import BeautifulSoup

    song = input("Enter a song: ")
    
    song = song.replace(" ", "+")
    searchUrl = 'https://www.google.com/search?q=ultimate-guitar%3A+' + song
    headers={'User-Agent':'user_agent'}
    gReq = urllib.request.Request(searchUrl,None,headers)
    gResp = urllib.request.urlopen(gReq).read()
    soup = BeautifulSoup(gResp, "lxml")
    gElem = soup.select('.r a')
    gUrl = gElem[0].get('href')
    gParsed = urllib.parse.parse_qs(gUrl)
    
    gtUrl = urllib.request.urlopen(gParsed['/url?q'][0])
    gtSoup = BeautifulSoup(gtUrl, "lxml")

    chords = gtSoup('pre')
    fileName = song.replace("+", "_")
    chords = str(chords).replace(u'\u2013',u' ')
    with open(str(fileName)+".html", "w") as file:
        file.write(str(chords))
    
main()