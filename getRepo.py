import sys
import glob
import os
import re
import time
import random
import urllib.request
from math import exp, fabs, sqrt, log, pi
from subprocess import call
from bs4 import BeautifulSoup

# ######
# Requirements : python3
#                BeautifulSoup4 package
# ######

def getRepos(loc):
    # getRepos : 깃허브 '검색 후 주소'를 받아 repository 목록을 반환한다.
    hrefs = []
    soup = getSoup(loc)
    if (soup == None):
        print ('Warning : ')
        print ('This location  \"' + loc + '\" , has no repository')
        return hrefs
    # repo-list-name 클래스를 가진 내용들을 모은다.
    repos = soup.find_all("h3", class_="repo-list-name")
    # 주소만 모은다.
    for i in repos :
        hrefs.append('https://github.com' + i.find('a').get('href'))
    return hrefs

def getSoup(loc):
    # getSoup : doc 에 html을 받아 BeautifulSoup 형식으로 만든다.
    # python3이라 urllib2가 아닌 urllib.request 이다.
    try:
        doc = urllib.request.urlopen(loc)
    except :
        return None
    return (BeautifulSoup (doc, "lxml"))

def nextPage(soup):
    # nextPage : 깃허브 검색 페이지에서, 다음 페이지의 주소를 반환한다.
    # 다음 페이지가 없을 경우 None 을 반환한다.
    if (soup == None):
        return None
    temp = soup.find('a', class_="next_page")
    if (temp == None):
        return None
    else :
        return ('https://github.com' + (soup.find('a', class_="next_page").get('href')))

def getKeywordLoc_C(keyword):
    # getKeywordLoc_C : 단어를 받아 깃허브에서 C언어 저장소 검색한 주소를 반환한다.
    return ('https://github.com/search?l=C&type=Repositories&utf8=%E2%9C%93&q=' + keyword)

def allRepos_keyword(keyword):
    # allRepos_keyword : 단어를 받아 모든 검색 결과 저장소의 이름을 반환한다.
    # TODO : complete this
    allrepos = []
    loc = getKeywordLoc_C(keyword)
    # while (loc != None):
    return None


# 테스트 코드:
# print(getRepos(getKeywordLoc_C('graph')))
# 윗줄 코드의 주석을 지우고 $ python3 ./getRepo.py 하면
# graph 검색결과 첫번째 페이지의 저장소들의 주소의 배열이 나온다.
