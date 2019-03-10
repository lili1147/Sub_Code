'''
分析每个类型总体的赞助商数目。
{'Publishing': 1787424, 'Film & Video': 3824855, 'Music': 2393851, 'Food': 1142292, 'Design': 5634937, 'Crafts': 193255, 'Games': 9016021, 'Comics': 1172736, 'Fashion': 1135661, 'Theater': 471100, 'Art': 942057, 'Photography': 360663, nan: 2784, 'Technology': 4312849, 'Dance': 144964, 'Journalism': 154269, ' 50 Years in the Making': 20, ' Retro Gaming art.': 0, ' Fearless Swimwear Boutique"': 200, ' M.ercury E.dition)': 26, ' 2010"': 280, ' EUNIVERSITY ONLINE"': 1, ' Raised Garden Beds Made of Pallets!"': 50, ' mammoth projects."': 0, ' Kingdom of Heaven.': 1, '000 Miles & You"': 255, ' Good for your skin': 435, ' Spirits': 401, ' Demons ': 750, ' co-created opera"': 425, ' Divine Wisdom': 1}


分析每年不同类型的众筹赞助商数目的变化
2010年——2017年的变化
'''
# import csv
# import numpy as np
# import pandas as pd

# data = pd.read_csv('../ks-projects-201612.csv', usecols=[3, 10])

# # print(data)
# dic = {}

# for item in np.arange(0, len(data)):
#     try:
#         data1 = data.loc[item].values
#         # print(data)
#         data_type = data1[0]
#         nums = int(data1[1])
#         # print(data_type)
#         # print(nums)

#         if data_type in dic.keys():
#             dic[data_type] += nums
#             #print(nums)
#         else:
#             dic[data_type] = nums
#             #print('else')
#     except ValueError:
#         pass
# print(dic)


import numpy as np
import pandas as pd
import csv

# 对金额的分析
data = pd.read_csv('../ks-projects-201612.csv', usecols=[2, 3])

# print(data)

Publish = {}
Music = {}
Film_Video = {}
Photography = {}
Technology = {}
Journalism = {}
Art = {}
Food = {}
Games = {}


for item in np.arange(0, len(data)):
    # print(data.loc[item].values)
    data_type = data.loc[item].values[0]
    data_main_type = data.loc[item].values[1]

    if data_main_type == 'Publishing':
        if data_type != data_main_type:
            if data_type in Publish.keys():
                Publish[data_type] += 1
            else:
                Publish[data_type] = 1

    elif data_main_type == 'Music':
        if data_type != data_main_type:
            if data_type in Music.keys():
                Music[data_type] += 1
            else:
                Music[data_type] = 1

    elif data_main_type == 'Film & Video':
        if data_type != data_main_type:
            if data_type in Film_Video.keys():
                Film_Video[data_type] += 1
            else:
                Film_Video[data_type] = 1

    elif data_main_type == 'Photography':
        if data_type != data_main_type:
            if data_type in Photography.keys():
                Photography[data_type] += 1
            else:
                Photography[data_type] = 1

    elif data_main_type == 'Technology':
        if data_type != data_main_type:
            if data_type in Technology.keys():
                Technology[data_type] += 1
            else:
                Technology[data_type] = 1

    elif data_main_type == 'Journalism':
        if data_type != data_main_type:
            if data_type in Journalism.keys():
                Journalism[data_type] += 1
            else:
                Journalism[data_type] = 1

    elif data_main_type == 'Art':
        if data_type != data_main_type:
            if data_type in Art.keys():
                Art[data_type] += 1
            else:
                Art[data_type] = 1

    elif data_main_type == 'Food':
        if data_type != data_main_type:
            if data_type in Food.keys():
                Food[data_type] += 1
            else:
                Food[data_type] = 1

    elif data_main_type == 'Games':
        if data_type != data_main_type:
            if data_type in Games.keys():
                Games[data_type] += 1
            else:
                Games[data_type] = 1


print(Publish)
print('-----')
print(Music)
print('-----')
print(Film_Video)
print('-----')
print(Photography)
print('-----')
print(Technology)
print('-----')
print(Journalism)
print('-----')
print(Art)
print('-----')
print(Food)
print('-----')
print(Games)


'''
{'Poetry': 1218, 'Nonfiction': 7388, 'Art Books': 2218, 'Fiction': 8224, 'Radio & Podcasts': 800, 'Periodicals': 1139, 'Young Adult': 650, 'Anthologies': 265, "Children's Books": 5634, 'Calendars': 243, 'Academic': 706, 'Zines': 284, 'Translations': 126, 'Literary Journals': 218, ' so don\'t blame it on me."': 1, ' A Christmas Story (Canceled)': 1, " the first of the Jack-to guides where novices write the how-to's": 1, ' Where do we go when we are seventy-six.': 1, 'photos by Shell Sheddy': 1, ' BEYOND RANA PLAZA': 1, ' How To Protect Yourself': 1, ' The Enchanted Saga (Canceled)': 1, ' Trauma Affected Genes': 1, ' A guide for the Explorer in everyone!': 1, ' From Cradle To Grave/Bridging The Gap Of Misconception': 1, ' an epic new sci-fi!': 1, ' 2017 Short Story Anthology': 1}
-----
{'Indie Rock': 5364, 'Pop': 3024, 'Rock': 6333, 'Jazz': 1657, 'Electronic Music': 1907, 'Metal': 622, 'Hip-Hop': 3465, 'World Music': 1839, 'Punk': 261, 'Classical Music': 2372, 'Country & Folk': 4042, 'R&B': 357, 'Blues': 226, 'Faith': 892, 'Latin': 104, 'Kids': 235, 'Chiptune': 33, ' exploring the genes of songwriting': 1, ' Music Without Borders': 1, ' Marc & Mary sing together at last!': 1, ' Girl Power Tour Benefit Concert': 1, ' Music Album (Canceled)': 1, ' The North (2015)': 1, ' Living for Music Dying for Love': 1, ' Volume 2': 1, ' Songs by & about her + Stories': 1, ' The Re-Birth Recordings': 1, ')': 1, ' Solo project for Dave Broyles': 1, ' The Gravity of Our Commitment': 1, ' Recording Soundtracks': 1, ' donate and receive a Cigar Box Guitar': 1, ' Season 1': 1, ' Help Turn Up The Volume In The Arts!': 1, ' A southern Tour': 1, ' Still Singing For Haiti': 1, ' Forgotten Flag: the debut album.': 1, ' Manic Song-stronaut Materializes Album With Mind': 1, ' future cd project ': 1, ' the Sound of Souls': 1, ' Tour & CD Release': 1, ' 2 full length CDs!': 1, " 'Take Me Away' ... Become a part of Team Kerrin!": 1}
-----
{'Narrative Film': 4953, 'Documentary': 14854, 'Webseries': 5336, 'Family': 276, 'Shorts': 11663, 'Drama': 1714, 'Action': 605, 'Comedy': 1740, 'Animation': 2254, 'Movie Theaters': 194, 'Fantasy': 271, 'Music Videos': 591, 'Experimental': 459, 'Horror': 1032, 'Science Fiction': 597, 'Thrillers': 596, 'Festivals': 227, 'Television': 820, 'Romance': 159, ' A Ten Year Retrospective': 1, ' Help a Struggling Artist!': 1, ' Time to Die': 1, ' a film by Valeria Berumen': 1, ' a TV show': 1, ' a day in the life of a champion': 1, ' The Sobering Truth': 1, ' Right and Wrong': 1, ' a film by Arius Blaze': 1, ' reclaimed wood to fit your lifestyle.': 1, ' a short film': 1, ' a new feature film': 1, ' Bleed For Us.': 1, ' Detroit : Into The Future': 1, ' Enriching Lives by Sharing Simple Truth-Video1': 1, ' Part 1': 1, ' Head in the Clouds': 1}
-----
{'Photobooks': 1204, 'Fine Art': 644, 'People': 943, 'Animals': 218, 'Places': 648, 'Nature': 488, ' Through the lens and back again...': 1, ' uniquely depicted through the lens of an ipad': 1, ' Human Connection Through Emotions': 1, ' photographs and sounds of the French Maghrebi': 1, ' A Different Themes': 1, ' Our Unsung Heros': 1, ' plexi cubes combining manmade and nature': 1, ' In this country of ours.': 1, ' an exhibition of photographic narratives.': 1, ' in Color and Black/White': 1, ' Look Closer  - A photographic e-book': 1, ' Cultural traditions & celebration': 1, ' portraits of Columbus musicians': 1, ' a photographic journal by Cynthia Manuszak': 1, ' a photo journey through time.': 1, ' a bike quest in New Zealand': 1}
-----
{'Hardware': 3144, 'Gadgets': 2165, 'Web': 3192, 'Apps': 4848, 'Software': 2547, 'Flight': 358, 'Makerspaces': 192, 'Fabrication Tools': 195, 'Sound': 485, 'DIY Electronics': 697, 'Camera Equipment': 299, '3D Printing': 554, 'Wearables': 899, 'Space Exploration': 259, 'Robots': 454, ' Inflatable Paddle and Surf Boards': 1, ' Connecting Communities (Canceled)': 1, ')=': 1, ' Tap. Paint. Love!': 1, ' Clothing with Memory': 1, ' A Space Mission On A Budget': 1, 'An Explanation of Nature': 1, ' Anti-Kidnapping Mobile App. (Canceled)': 1, ' Be heard Be inspired': 1, ' The Community Pin Board Event App': 1, ' Go Green': 1, ' an all-new electric recumbent trike': 1}
-----
{'Print': 598, 'Video': 337, 'Web': 1023, 'Photo': 170, 'Audio': 317, ' INVEST.': 1, ' Overcome It': 1, ' Saving the history of our military bases.': 1, ' The Trip for Life': 1}
-----
{'Public Art': 2833, 'Illustration': 2321, 'Painting': 2860, 'Ceramics': 228, 'Sculpture': 1621, 'Mixed Media': 2390, 'Digital Art': 1113, 'Performance Art': 2007, 'Installations': 386, 'Conceptual Art': 910, 'Textiles': 197, 'Video Art': 154, ' a mosaic re-creation using McDonalds cups': 1, ' Ecological Activism and Art- exhibition and events': 1, nan: 1, ' Reprint of unique deck': 1, ' FACES OF ARTISTRY': 1, ' We-are-Legion!': 1, 's Summer Carnival) (Canceled)': 1, ' An Expeditionary Residency': 1, ' a lino print to celebrate Duet racing in fastnet': 1, ' Space for Creativity & Community': 1, ' 1st Birthday Celebration!': 1, ' into an Oil Painting': 1, ' Art Festival': 1, ' Think Differently': 1, ' from the Canvas of a Broken Heart?Painting': 1, ' Beautifully Handcrafted Art Cards': 1, ' AN ART INSTALLATION': 1}
-----
{'Restaurants': 2283, 'Drinks': 1897, 'Food Trucks': 1457, 'Cookbooks': 438, "Farmer's Markets": 350, 'Events': 558, 'Spaces': 324, 'Community Gardens': 258, 'Farms': 966, 'Vegan': 420, 'Bacon': 205, 'Small Batch': 1466, ' Join Our Brewery in the Shade': 1, ' neighbors buy it': 1, ' Feeding Local': 1, ' Real Bay Area Street Food': 1, ' Delivering your daily bread.': 1, ' Family Nutrition': 1, ' while creating jobs for others': 1, ' Give the Gift of Spices and Flowers': 1, ' Baking Cookies and Changing Lives': 1, ' A World First!': 1, ' Where The Villains Go.': 1, ' A (Cook)Book That Shows You How.': 1, ' give them a try!': 2, ' A Novel Gastropub and Bicycle Outfitter': 1, ' a mobile food venue to feed your soul': 1, ' Pure & Simple.': 1, ' A Chocolofier! The next evolution for us': 1, ' Big Diehl Peppers': 1, ' A Journey Inside Culinary Obsession': 1, ' the road to The Cuppin Cake Truck.': 1, ' Evolution Of The Brewpub': 1, ' Grocery Store Expansion': 1, ' ready to juice.': 1, ')': 1, ' what the people crave!': 1, ' Culinae!': 1, ' A Manual For Serious Food Enthusiasts': 1, ' Inspire the Night': 1}
-----
{'Tabletop Games': 10660, 'Video Games': 10021, 'Mobile Games': 1422, 'Playing Cards': 1757, 'Puzzles': 185, 'Live Games': 853, 'Gaming Hardware': 330, ' Soyez un Champion': 1, ' The Game of Deception': 1, ' 7: As Above So Below': 1}
'''
