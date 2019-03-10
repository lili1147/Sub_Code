'''
统计词频
画出词云
'''

import pandas as pd
import csv
import numpy as np
import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator


# data = pd.read_csv('../ks-projects-201612.csv', usecols=['main_category '])
# dict = {}
# l = np.arange(0, len(data))
# for item in l:
#     name = data.loc[item].values[0]
#     # print(name)
#     if name in dict.keys():
#         dict[name] += 1
#     else:
#         dict[name] = 1

dict = {'Publishing': 34164, 'Film & Video': 57546, 'Music': 46643, 'Food': 21148, 'Design': 23745, 'Crafts': 7167, 'Games': 27899, 'Comics': 8737, 'Fashion': 18309, 'Theater': 9948, 'Art': 23921, 'Photography': 9657, 'Technology': 26036, 'Dance': 3362, 'USD': 415, 'Journalism': 4061, 'Metal': 1, 'Cookbooks': 1, 'Web': 9, 'Shorts': 13, 'Plays': 1, 'GBP': 35, 'Hardware': 6, 'Playing Cards': 3, 'World Music': 4, 'Thrillers': 1, 'Mobile Games': 3, 'Camera Equipment': 2, 'EUR': 50, 'Classical Music': 4, 'Conceptual Art': 5, 'Nonfiction': 29, 'Product Design': 32, 'Documentary': 29, 'Video Games': 12, ' 50 Years in the Making': 1, 'Country & Folk': 7, 'Performance Art': 5, 'Mixed Media': 11, 'Comic Books': 2, ' Retro Gaming art.': 1, 'Places': 3, 'Events': 1, 'Fiction': 35, 'Tabletop Games': 15, 'Video': 2, 'Small Batch': 3, "Children's Books": 18, 'Poetry': 6, 'Public Art': 3, 'Art Books': 10, 'Drama': 2, 'Apparel': 10, 'Sculpture': 6, 'DIY': 2, 'CAD': 18, 'Hip-Hop': 7, ' Fearless Swimwear Boutique"': 1, 'Accessories': 2, 'People': 1, 'Webseries': 7, 'Interactive Design': 1, 'SEK': 6, 'Periodicals': 6, 'Vegan': 1, 'Indie Rock': 7, 'Academic': 3, 'Pop': 5, ' M.ercury E.dition)': 1, 'NZD': 3, 'Faith': 1,
        'Jazz': 4, 'Space Exploration': 3, 'Performances': 2, 'Digital Art': 6, 'Narrative Film': 8, ' 2010"': 1, 'Apps': 7, 'AUD': 8, 'Installations': 3, 'MXN': 2, ' EUNIVERSITY ONLINE"': 1, 'Pet Fashion': 1, 'Restaurants': 3, 'Rock': 3, ' Raised Garden Beds Made of Pallets!"': 1, 'Software': 5, 'Drinks': 1, 'Architecture': 3, 'Photobooks': 1, 'Textiles': 1, ' mammoth projects."': 1, 'Fine Art': 2, 'Food Trucks': 2, ' Learn': 1, 'Wearables': 1, 'Gaming Hardware': 1, 'Civic Design': 1, ' Kingdom of Heaven.': 1, 'Zines': 2, 'Musical': 1, 'Graphic Design': 3, 'Ready-to-wear': 2, '000 Miles & You"': 1, 'Print': 3, 'Horror': 3, 'Animation': 2, 'NOK': 2, 'Flight': 1, ' pants': 1, 'Illustration': 5, 'Festivals': 1, 'Radio & Podcasts': 1, 'DKK': 1, 'Action': 1, 'Young Adult': 2, 'DIY Electronics': 1, 'Painting': 4, 'Webcomics': 1, 'Television': 2, '3D Printing': 1, 'Audio': 1, 'Jewelry': 1, 'Woodworking': 1, 'Electronic Music': 2, ' and Improve your Camera"': 1, ' Good for your skin': 1, ' Spirits': 1, 'R&B': 1, 'Robots': 1, ' Italy': 1, ' soccer': 1, 'Nature': 2, ' Demons ': 1, 'Literary Journals': 1, ' co-created opera"': 1, ' Divine Wisdom': 1, 'Farms': 1, 'CHF': 1, ' Restore Pride': 1, 'SGD': 1, 'Kids': 1}


# file = open('num_words.txt', 'r')
# string = file.read()
# print(type(string))
# dic = json.loads(string)
# print(dic)
# print(type(dic))
image = Image.open('tim.png')
graph = np.array(image)
wc = WordCloud(font_path='./fonts/simhei.ttf', background_color='white',
               max_words=200, mask=graph, min_font_size=10)
wc.generate_from_frequencies(dict)
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off")
plt.show()
wc.to_file('dream4.png')


# import jieba.analyse
# from PIL import Image, ImageSequence
# import numpy as np
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, ImageColorGenerator


# dict = {
#     'name': 10,
#     'sex': 4,
#     'gender': 12,
#     'beauty': 50,
#     'lady': 42,
#     'boy': 20
# }

# image = Image.open('tim.png')
# graph = np.array(image)
# wc = WordCloud(font_path='./fonts/simhei.ttf', background_color='White', max_words=50, mask=graph)
# wc.generate_from_frequencies(dict)
# image_color = ImageColorGenerator(graph)
# plt.imshow(wc)
# plt.imshow(wc.recolor(color_func=image_color))
# plt.axis("off")
# plt.show()
# wc.to_file('dream2.png')
