# import usefull libraries.
import urllib.request
from bs4 import BeautifulSoup
import json


def getContent():
    host = "https://www.ucdenver.edu"
    # target site url
    url = "http://www.ucdenver.edu/pages/ucdwelcomepage.aspx"
    # requesting the url for data
    request = urllib.request.Request(url)
    # get the html, whole page
    htmlpage = urllib.request.urlopen(request).read()
    # pass html data page to b sop
    bsoup = BeautifulSoup(htmlpage, 'html.parser')
    # Find a site table (???) from 'docResponsive'
    main_table = bsoup.find("div", attrs={'id': 'docResponsive'})
    # Now we go into main_table and get every a element in it which has a class "title"
    links = main_table.find_all("a", class_="navbar-link")

    # from each link extract the text of link and the link itself
    # this is the disctionary to store my links
    mylinks = dict()
    count = 1
    for link in links:
        title = link.text
        url = link['href']
        if "http" in url:
            mylinks[title] = url
        else:
            url = host + "" + url
            mylinks[title] = url
        print(">> " + str(count) + " [" + url + "] ")
        count += 1
    return mylinks


def main():
    mylinks = dict()
    mylinks = getContent()

    with open('links.json', 'w') as links:
        json.dump(mylinks, links, indent=5)


main()