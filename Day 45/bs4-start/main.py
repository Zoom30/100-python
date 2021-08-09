from bs4 import BeautifulSoup
import requests
import random

##CHALLENGE##
#Getting top 100 "must watch" movies from empireonline.com

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
eo_web_page = response.text

soup = BeautifulSoup(eo_web_page, "html.parser")
# print(soup.prettify)


# getting all movie titles

all_movie_title = soup.find_all(name = "h3", class_="titleText")

print(len(all_movie_title))

#======================================================================================================

# response = requests.get(url="https://news.ycombinator.com/news")
# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, "html.parser")

# #getting article titles
# all_story_links = soup.find_all(name = "a", class_="storylink", href=True)
# title_list = []
# for link in all_story_links:
#     title_list.append(link.string)
# # print(title_list)

# #getting article link
# link_list = []
# for link in all_story_links:
#     link_list.append(link["href"])
# # print(link_list)


# #getting article upvote counts
# all_upvote_counts = soup.find_all(name="span", class_="score")
# upvote_list = []
# for count in all_upvote_counts:
#     #1. get hold of the number of counts with 'count.string' e.g "167 points"
#     #2. since it's of type string, split it with .split() to get only the numbers
#     #3. convert the 'string' number to 'int' number
#     upvote_list.append(int(count.string.split()[0]))

# # print(upvote_list)

# #finding the title, link and upvote number for the highest upvoted news
# print(title_list)
# print(link_list)
# print(upvote_list)
# max_vote = max(upvote_list)
# index_of_max_vote = upvote_list.index(max_vote)
# print(f"""
# Title: {title_list[index_of_max_vote]}
# Link: {link_list[index_of_max_vote]}
# Upvote Count: {max_vote}
# """)











# with open(file="Day 45/bs4-start/website.html") as file:
#     x = file.read()

# soup = BeautifulSoup(x, "html.parser")
# all_anchor_tag = soup.findAll(name="a")
# for tag in all_anchor_tag:
#     print(tag.get("href"))


# heading = soup.find(name="h1", id="name")
# print(heading.string)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.string)
# company_url = soup.select_one(selector="p a")
# name = soup.select_one(selector="#name")
# print(name)


# #selecting all elements that have 'class="heading'

# all_heading = soup.select(selector=".heading")
# print(all_heading)

