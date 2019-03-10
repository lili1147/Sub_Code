import csv
from pyecharts import Line, Page


page = Page()


def compare(type, now_type, year, now_year, count):
    if(type == now_type and year == now_year):
        count += 1

    return count


def result():
    with open('../ks-projects-201801.csv', 'r', encoding='gbk', errors='ignore') as file_2018:
        reader_2018 = csv.reader(file_2018)

        count18_2009_Pub = 0
        count18_2009_Fil = 0
        count18_2009_Mus = 0
        count18_2009_Foo = 0
        count18_2009_Des = 0
        count18_2009_Cra = 0
        count18_2009_Gam = 0
        count18_2009_Com = 0
        count18_2009_Fas = 0
        count18_2009_The = 0
        count18_2009_Art = 0
        count18_2009_Pho = 0
        count18_2009_Thc = 0
        count18_2009_Dan = 0
        count18_2009_Jou = 0

        count18_2010_Pub = 0
        count18_2010_Fil = 0
        count18_2010_Mus = 0
        count18_2010_Foo = 0
        count18_2010_Des = 0
        count18_2010_Cra = 0
        count18_2010_Gam = 0
        count18_2010_Com = 0
        count18_2010_Fas = 0
        count18_2010_The = 0
        count18_2010_Art = 0
        count18_2010_Pho = 0
        count18_2010_Thc = 0
        count18_2010_Dan = 0
        count18_2010_Jou = 0

        count18_2011_Pub = 0
        count18_2011_Fil = 0
        count18_2011_Mus = 0
        count18_2011_Foo = 0
        count18_2011_Des = 0
        count18_2011_Cra = 0
        count18_2011_Gam = 0
        count18_2011_Com = 0
        count18_2011_Fas = 0
        count18_2011_The = 0
        count18_2011_Art = 0
        count18_2011_Pho = 0
        count18_2011_Thc = 0
        count18_2011_Dan = 0
        count18_2011_Jou = 0

        count18_2012_Pub = 0
        count18_2012_Fil = 0
        count18_2012_Mus = 0
        count18_2012_Foo = 0
        count18_2012_Des = 0
        count18_2012_Cra = 0
        count18_2012_Gam = 0
        count18_2012_Com = 0
        count18_2012_Fas = 0
        count18_2012_The = 0
        count18_2012_Art = 0
        count18_2012_Pho = 0
        count18_2012_Thc = 0
        count18_2012_Dan = 0
        count18_2012_Jou = 0

        count18_2013_Pub = 0
        count18_2013_Fil = 0
        count18_2013_Mus = 0
        count18_2013_Foo = 0
        count18_2013_Des = 0
        count18_2013_Cra = 0
        count18_2013_Gam = 0
        count18_2013_Com = 0
        count18_2013_Fas = 0
        count18_2013_The = 0
        count18_2013_Art = 0
        count18_2013_Pho = 0
        count18_2013_Thc = 0
        count18_2013_Dan = 0
        count18_2013_Jou = 0

        count18_2014_Pub = 0
        count18_2014_Fil = 0
        count18_2014_Mus = 0
        count18_2014_Foo = 0
        count18_2014_Des = 0
        count18_2014_Cra = 0
        count18_2014_Gam = 0
        count18_2014_Com = 0
        count18_2014_Fas = 0
        count18_2014_The = 0
        count18_2014_Art = 0
        count18_2014_Pho = 0
        count18_2014_Thc = 0
        count18_2014_Dan = 0
        count18_2014_Jou = 0

        count18_2015_Pub = 0
        count18_2015_Fil = 0
        count18_2015_Mus = 0
        count18_2015_Foo = 0
        count18_2015_Des = 0
        count18_2015_Cra = 0
        count18_2015_Gam = 0
        count18_2015_Com = 0
        count18_2015_Fas = 0
        count18_2015_The = 0
        count18_2015_Art = 0
        count18_2015_Pho = 0
        count18_2015_Thc = 0
        count18_2015_Dan = 0
        count18_2015_Jou = 0

        count18_2016_Pub = 0
        count18_2016_Fil = 0
        count18_2016_Mus = 0
        count18_2016_Foo = 0
        count18_2016_Des = 0
        count18_2016_Cra = 0
        count18_2016_Gam = 0
        count18_2016_Com = 0
        count18_2016_Fas = 0
        count18_2016_The = 0
        count18_2016_Art = 0
        count18_2016_Pho = 0
        count18_2016_Thc = 0
        count18_2016_Dan = 0
        count18_2016_Jou = 0

        count18_2017_Pub = 0
        count18_2017_Fil = 0
        count18_2017_Mus = 0
        count18_2017_Foo = 0
        count18_2017_Des = 0
        count18_2017_Cra = 0
        count18_2017_Gam = 0
        count18_2017_Com = 0
        count18_2017_Fas = 0
        count18_2017_The = 0
        count18_2017_Art = 0
        count18_2017_Pho = 0
        count18_2017_Thc = 0
        count18_2017_Dan = 0
        count18_2017_Jou = 0

        count18_2018_Pub = 0
        count18_2018_Fil = 0
        count18_2018_Mus = 0
        count18_2018_Foo = 0
        count18_2018_Des = 0
        count18_2018_Cra = 0
        count18_2018_Gam = 0
        count18_2018_Com = 0
        count18_2018_Fas = 0
        count18_2018_The = 0
        count18_2018_Art = 0
        count18_2018_Pho = 0
        count18_2018_Thc = 0
        count18_2018_Dan = 0
        count18_2018_Jou = 0

        for line18 in reader_2018:

            count18_2009_Pub = compare('Publishing', line18[3], '2009', line18[5][:4], count18_2009_Pub)
            count18_2009_Fil = compare('Film & Video', line18[3], '2009', line18[5][:4], count18_2009_Fil)
            count18_2009_Mus = compare('Music', line18[3], '2009', line18[5][:4], count18_2009_Mus)
            count18_2009_Foo = compare('Food', line18[3], '2009', line18[5][:4], count18_2009_Foo)
            count18_2009_Des = compare('Design', line18[3], '2009', line18[5][:4], count18_2009_Des)
            count18_2009_Cra = compare('Crafts', line18[3], '2009', line18[5][:4], count18_2009_Cra)
            count18_2009_Gam = compare('Games', line18[3], '2009', line18[5][:4], count18_2009_Gam)
            count18_2009_Com = compare('Comics', line18[3], '2009', line18[5][:4], count18_2009_Com)
            count18_2009_Fas = compare('Fashion', line18[3], '2009', line18[5][:4], count18_2009_Fas)
            count18_2009_The = compare('Theater', line18[3], '2009', line18[5][:4], count18_2009_The)
            count18_2009_Art = compare('Art', line18[3], '2009', line18[5][:4], count18_2009_Art)
            count18_2009_Pho = compare('Photography', line18[3], '2009', line18[5][:4], count18_2009_Pho)
            count18_2009_Thc = compare('Technology', line18[3], '2009', line18[5][:4], count18_2009_Thc)
            count18_2009_Dan = compare('Dance', line18[3], '2009', line18[5][:4], count18_2009_Dan)
            count18_2009_Jou = compare('Journalism', line18[3], '2009', line18[5][:4], count18_2009_Jou)

            count18_2010_Pub = compare('Publishing', line18[3], '2010', line18[5][:4], count18_2010_Pub)
            count18_2010_Fil = compare('Film & Video', line18[3], '2010', line18[5][:4], count18_2010_Fil)
            count18_2010_Mus = compare('Music', line18[3], '2010', line18[5][:4], count18_2010_Mus)
            count18_2010_Foo = compare('Food', line18[3], '2010', line18[5][:4], count18_2010_Foo)
            count18_2010_Des = compare('Design', line18[3], '2010', line18[5][:4], count18_2010_Des)
            count18_2010_Cra = compare('Crafts', line18[3], '2010', line18[5][:4], count18_2010_Cra)
            count18_2010_Gam = compare('Games', line18[3], '2010', line18[5][:4], count18_2010_Gam)
            count18_2010_Com = compare('Comics', line18[3], '2010', line18[5][:4], count18_2010_Com)
            count18_2010_Fas = compare('Fashion', line18[3], '2010', line18[5][:4], count18_2010_Fas)
            count18_2010_The = compare('Theater', line18[3], '2010', line18[5][:4], count18_2010_The)
            count18_2010_Art = compare('Art', line18[3], '2010', line18[5][:4], count18_2010_Art)
            count18_2010_Pho = compare('Photography', line18[3], '2010', line18[5][:4], count18_2010_Pho)
            count18_2010_Thc = compare('Technology', line18[3], '2010', line18[5][:4], count18_2010_Thc)
            count18_2010_Dan = compare('Dance', line18[3], '2010', line18[5][:4], count18_2010_Dan)
            count18_2010_Jou = compare('Journalism', line18[3], '2010', line18[5][:4], count18_2010_Jou)

            count18_2011_Pub = compare('Publishing', line18[3], '2011', line18[5][:4], count18_2011_Pub)
            count18_2011_Fil = compare('Film & Video', line18[3], '2011', line18[5][:4], count18_2011_Fil)
            count18_2011_Mus = compare('Music', line18[3], '2011', line18[5][:4], count18_2011_Mus)
            count18_2011_Foo = compare('Food', line18[3], '2011', line18[5][:4], count18_2011_Foo)
            count18_2011_Des = compare('Design', line18[3], '2011', line18[5][:4], count18_2011_Des)
            count18_2011_Cra = compare('Crafts', line18[3], '2011', line18[5][:4], count18_2011_Cra)
            count18_2011_Gam = compare('Games', line18[3], '2011', line18[5][:4], count18_2011_Gam)
            count18_2011_Com = compare('Comics', line18[3], '2011', line18[5][:4], count18_2011_Com)
            count18_2011_Fas = compare('Fashion', line18[3], '2011', line18[5][:4], count18_2011_Fas)
            count18_2011_The = compare('Theater', line18[3], '2011', line18[5][:4], count18_2011_The)
            count18_2011_Art = compare('Art', line18[3], '2011', line18[5][:4], count18_2011_Art)
            count18_2011_Pho = compare('Photography', line18[3], '2011', line18[5][:4], count18_2011_Pho)
            count18_2011_Thc = compare('Technology', line18[3], '2011', line18[5][:4], count18_2011_Thc)
            count18_2011_Dan = compare('Dance', line18[3], '2011', line18[5][:4], count18_2011_Dan)
            count18_2011_Jou = compare('Journalism', line18[3], '2011', line18[5][:4], count18_2011_Jou)

            count18_2012_Pub = compare('Publishing', line18[3], '2012', line18[5][:4], count18_2012_Pub)
            count18_2012_Fil = compare('Film & Video', line18[3], '2012', line18[5][:4], count18_2012_Fil)
            count18_2012_Mus = compare('Music', line18[3], '2012', line18[5][:4], count18_2012_Mus)
            count18_2012_Foo = compare('Food', line18[3], '2012', line18[5][:4], count18_2012_Foo)
            count18_2012_Des = compare('Design', line18[3], '2012', line18[5][:4], count18_2012_Des)
            count18_2012_Cra = compare('Crafts', line18[3], '2012', line18[5][:4], count18_2012_Cra)
            count18_2012_Gam = compare('Games', line18[3], '2012', line18[5][:4], count18_2012_Gam)
            count18_2012_Com = compare('Comics', line18[3], '2012', line18[5][:4], count18_2012_Com)
            count18_2012_Fas = compare('Fashion', line18[3], '2012', line18[5][:4], count18_2012_Fas)
            count18_2012_The = compare('Theater', line18[3], '2012', line18[5][:4], count18_2012_The)
            count18_2012_Art = compare('Art', line18[3], '2012', line18[5][:4], count18_2012_Art)
            count18_2012_Pho = compare('Photography', line18[3], '2012', line18[5][:4], count18_2012_Pho)
            count18_2012_Thc = compare('Technology', line18[3], '2012', line18[5][:4], count18_2012_Thc)
            count18_2012_Dan = compare('Dance', line18[3], '2012', line18[5][:4], count18_2012_Dan)
            count18_2012_Jou = compare('Journalism', line18[3], '2012', line18[5][:4], count18_2012_Jou)

            count18_2013_Pub = compare('Publishing', line18[3], '2013', line18[5][:4], count18_2013_Pub)
            count18_2013_Fil = compare('Film & Video', line18[3], '2013', line18[5][:4], count18_2013_Fil)
            count18_2013_Mus = compare('Music', line18[3], '2013', line18[5][:4], count18_2013_Mus)
            count18_2013_Foo = compare('Food', line18[3], '2013', line18[5][:4], count18_2013_Foo)
            count18_2013_Des = compare('Design', line18[3], '2013', line18[5][:4], count18_2013_Des)
            count18_2013_Cra = compare('Crafts', line18[3], '2013', line18[5][:4], count18_2013_Cra)
            count18_2013_Gam = compare('Games', line18[3], '2013', line18[5][:4], count18_2013_Gam)
            count18_2013_Com = compare('Comics', line18[3], '2013', line18[5][:4], count18_2013_Com)
            count18_2013_Fas = compare('Fashion', line18[3], '2013', line18[5][:4], count18_2013_Fas)
            count18_2013_The = compare('Theater', line18[3], '2013', line18[5][:4], count18_2013_The)
            count18_2013_Art = compare('Art', line18[3], '2013', line18[5][:4], count18_2013_Art)
            count18_2013_Pho = compare('Photography', line18[3], '2013', line18[5][:4], count18_2013_Pho)
            count18_2013_Thc = compare('Technology', line18[3], '2013', line18[5][:4], count18_2013_Thc)
            count18_2013_Dan = compare('Dance', line18[3], '2013', line18[5][:4], count18_2013_Dan)
            count18_2013_Jou = compare('Journalism', line18[3], '2013', line18[5][:4], count18_2013_Jou)

            count18_2014_Pub = compare('Publishing', line18[3], '2014', line18[5][:4], count18_2014_Pub)
            count18_2014_Fil = compare('Film & Video', line18[3], '2014', line18[5][:4], count18_2014_Fil)
            count18_2014_Mus = compare('Music', line18[3], '2014', line18[5][:4], count18_2014_Mus)
            count18_2014_Foo = compare('Food', line18[3], '2014', line18[5][:4], count18_2014_Foo)
            count18_2014_Des = compare('Design', line18[3], '2014', line18[5][:4], count18_2014_Des)
            count18_2014_Cra = compare('Crafts', line18[3], '2014', line18[5][:4], count18_2014_Cra)
            count18_2014_Gam = compare('Games', line18[3], '2014', line18[5][:4], count18_2014_Gam)
            count18_2014_Com = compare('Comics', line18[3], '2014', line18[5][:4], count18_2014_Com)
            count18_2014_Fas = compare('Fashion', line18[3], '2014', line18[5][:4], count18_2014_Fas)
            count18_2014_The = compare('Theater', line18[3], '2014', line18[5][:4], count18_2014_The)
            count18_2014_Art = compare('Art', line18[3], '2014', line18[5][:4], count18_2014_Art)
            count18_2014_Pho = compare('Photography', line18[3], '2014', line18[5][:4], count18_2014_Pho)
            count18_2014_Thc = compare('Technology', line18[3], '2014', line18[5][:4], count18_2014_Thc)
            count18_2014_Dan = compare('Dance', line18[3], '2014', line18[5][:4], count18_2014_Dan)
            count18_2014_Jou = compare('Journalism', line18[3], '2014', line18[5][:4], count18_2014_Jou)

            count18_2015_Pub = compare('Publishing', line18[3], '2015', line18[5][:4], count18_2015_Pub)
            count18_2015_Fil = compare('Film & Video', line18[3], '2015', line18[5][:4], count18_2015_Fil)
            count18_2015_Mus = compare('Music', line18[3], '2015', line18[5][:4], count18_2015_Mus)
            count18_2015_Foo = compare('Food', line18[3], '2015', line18[5][:4], count18_2015_Foo)
            count18_2015_Des = compare('Design', line18[3], '2015', line18[5][:4], count18_2015_Des)
            count18_2015_Cra = compare('Crafts', line18[3], '2015', line18[5][:4], count18_2015_Cra)
            count18_2015_Gam = compare('Games', line18[3], '2015', line18[5][:4], count18_2015_Gam)
            count18_2015_Com = compare('Comics', line18[3], '2015', line18[5][:4], count18_2015_Com)
            count18_2015_Fas = compare('Fashion', line18[3], '2015', line18[5][:4], count18_2015_Fas)
            count18_2015_The = compare('Theater', line18[3], '2015', line18[5][:4], count18_2015_The)
            count18_2015_Art = compare('Art', line18[3], '2015', line18[5][:4], count18_2015_Art)
            count18_2015_Pho = compare('Photography', line18[3], '2015', line18[5][:4], count18_2015_Pho)
            count18_2015_Thc = compare('Technology', line18[3], '2015', line18[5][:4], count18_2015_Thc)
            count18_2015_Dan = compare('Dance', line18[3], '2015', line18[5][:4], count18_2015_Dan)
            count18_2015_Jou = compare('Journalism', line18[3], '2015', line18[5][:4], count18_2015_Jou)

            count18_2016_Pub = compare('Publishing', line18[3], '2016', line18[5][:4], count18_2016_Pub)
            count18_2016_Fil = compare('Film & Video', line18[3], '2016', line18[5][:4], count18_2016_Fil)
            count18_2016_Mus = compare('Music', line18[3], '2016', line18[5][:4], count18_2016_Mus)
            count18_2016_Foo = compare('Food', line18[3], '2016', line18[5][:4], count18_2016_Foo)
            count18_2016_Des = compare('Design', line18[3], '2016', line18[5][:4], count18_2016_Des)
            count18_2016_Cra = compare('Crafts', line18[3], '2016', line18[5][:4], count18_2016_Cra)
            count18_2016_Gam = compare('Games', line18[3], '2016', line18[5][:4], count18_2016_Gam)
            count18_2016_Com = compare('Comics', line18[3], '2016', line18[5][:4], count18_2016_Com)
            count18_2016_Fas = compare('Fashion', line18[3], '2016', line18[5][:4], count18_2016_Fas)
            count18_2016_The = compare('Theater', line18[3], '2016', line18[5][:4], count18_2016_The)
            count18_2016_Art = compare('Art', line18[3], '2016', line18[5][:4], count18_2016_Art)
            count18_2016_Pho = compare('Photography', line18[3], '2016', line18[5][:4], count18_2016_Pho)
            count18_2016_Thc = compare('Technology', line18[3], '2016', line18[5][:4], count18_2016_Thc)
            count18_2016_Dan = compare('Dance', line18[3], '2016', line18[5][:4], count18_2016_Dan)
            count18_2016_Jou = compare('Journalism', line18[3], '2016', line18[5][:4], count18_2016_Jou)

            count18_2017_Pub = compare('Publishing', line18[3], '2017', line18[5][:4], count18_2017_Pub)
            count18_2017_Fil = compare('Film & Video', line18[3], '2017', line18[5][:4], count18_2017_Fil)
            count18_2017_Mus = compare('Music', line18[3], '2017', line18[5][:4], count18_2017_Mus)
            count18_2017_Foo = compare('Food', line18[3], '2017', line18[5][:4], count18_2017_Foo)
            count18_2017_Des = compare('Design', line18[3], '2017', line18[5][:4], count18_2017_Des)
            count18_2017_Cra = compare('Crafts', line18[3], '2017', line18[5][:4], count18_2017_Cra)
            count18_2017_Gam = compare('Games', line18[3], '2017', line18[5][:4], count18_2017_Gam)
            count18_2017_Com = compare('Comics', line18[3], '2017', line18[5][:4], count18_2017_Com)
            count18_2017_Fas = compare('Fashion', line18[3], '2017', line18[5][:4], count18_2017_Fas)
            count18_2017_The = compare('Theater', line18[3], '2017', line18[5][:4], count18_2017_The)
            count18_2017_Art = compare('Art', line18[3], '2017', line18[5][:4], count18_2017_Art)
            count18_2017_Pho = compare('Photography', line18[3], '2017', line18[5][:4], count18_2017_Pho)
            count18_2017_Thc = compare('Technology', line18[3], '2017', line18[5][:4], count18_2017_Thc)
            count18_2017_Dan = compare('Dance', line18[3], '2017', line18[5][:4], count18_2017_Dan)
            count18_2017_Jou = compare('Journalism', line18[3], '2017', line18[5][:4], count18_2017_Jou)

            count18_2018_Pub = compare('Publishing', line18[3], '2018', line18[5][:4], count18_2018_Pub)
            count18_2018_Fil = compare('Film & Video', line18[3], '2018', line18[5][:4], count18_2018_Fil)
            count18_2018_Mus = compare('Music', line18[3], '2018', line18[5][:4], count18_2018_Mus)
            count18_2018_Foo = compare('Food', line18[3], '2018', line18[5][:4], count18_2018_Foo)
            count18_2018_Des = compare('Design', line18[3], '2018', line18[5][:4], count18_2018_Des)
            count18_2018_Cra = compare('Crafts', line18[3], '2018', line18[5][:4], count18_2018_Cra)
            count18_2018_Gam = compare('Games', line18[3], '2018', line18[5][:4], count18_2018_Gam)
            count18_2018_Com = compare('Comics', line18[3], '2018', line18[5][:4], count18_2018_Com)
            count18_2018_Fas = compare('Fashion', line18[3], '2018', line18[5][:4], count18_2018_Fas)
            count18_2018_The = compare('Theater', line18[3], '2018', line18[5][:4], count18_2018_The)
            count18_2018_Art = compare('Art', line18[3], '2018', line18[5][:4], count18_2018_Art)
            count18_2018_Pho = compare('Photography', line18[3], '2018', line18[5][:4], count18_2018_Pho)
            count18_2018_Thc = compare('Technology', line18[3], '2018', line18[5][:4], count18_2018_Thc)
            count18_2018_Dan = compare('Dance', line18[3], '2018', line18[5][:4], count18_2018_Dan)
            count18_2018_Jou = compare('Journalism', line18[3], '2018', line18[5][:4], count18_2018_Jou)

            value1_Pub = [count18_2009_Pub, count18_2010_Pub, count18_2011_Pub, count18_2012_Pub, count18_2013_Pub,
                          count18_2014_Pub, count18_2015_Pub, count18_2016_Pub, count18_2017_Pub, count18_2018_Pub]
            value1_Fil = [count18_2009_Fil, count18_2010_Fil, count18_2011_Fil, count18_2012_Fil, count18_2013_Fil,
                          count18_2014_Fil, count18_2015_Fil, count18_2016_Fil, count18_2017_Fil, count18_2018_Fil]
            value1_Mus = [count18_2009_Mus, count18_2010_Mus, count18_2011_Mus, count18_2012_Mus, count18_2013_Mus,
                          count18_2014_Mus, count18_2015_Mus, count18_2016_Mus, count18_2017_Mus, count18_2018_Mus]
            value1_Foo = [count18_2009_Foo, count18_2010_Foo, count18_2011_Foo, count18_2012_Foo, count18_2013_Foo,
                          count18_2014_Foo, count18_2015_Foo, count18_2016_Foo, count18_2017_Foo, count18_2018_Foo]
            value1_Des = [count18_2009_Des, count18_2010_Des, count18_2011_Des, count18_2012_Des, count18_2013_Des,
                          count18_2014_Des, count18_2015_Des, count18_2016_Des, count18_2017_Des, count18_2018_Des]
            value1_Cra = [count18_2009_Cra, count18_2010_Cra, count18_2011_Cra, count18_2012_Cra, count18_2013_Cra,
                          count18_2014_Cra, count18_2015_Cra, count18_2016_Cra, count18_2017_Cra, count18_2018_Cra]
            value1_Gam = [count18_2009_Gam, count18_2010_Gam, count18_2011_Gam, count18_2012_Gam, count18_2013_Gam,
                          count18_2014_Gam, count18_2015_Gam, count18_2016_Gam, count18_2017_Gam, count18_2018_Gam]
            value1_Com = [count18_2009_Com, count18_2010_Com, count18_2011_Com, count18_2012_Com, count18_2013_Com,
                          count18_2014_Com, count18_2015_Com, count18_2016_Com, count18_2017_Com, count18_2018_Com]
            value1_Fas = [count18_2009_Fas, count18_2010_Fas, count18_2011_Fas, count18_2012_Fas, count18_2013_Fas,
                          count18_2014_Fas, count18_2015_Fas, count18_2016_Fas, count18_2017_Fas, count18_2018_Fas]
            value1_The = [count18_2009_The, count18_2010_The, count18_2011_The, count18_2012_The, count18_2013_The,
                          count18_2014_The, count18_2015_The, count18_2016_The, count18_2017_The, count18_2018_The]
            value1_Art = [count18_2009_Art, count18_2010_Art, count18_2011_Art, count18_2012_Art, count18_2013_Art,
                          count18_2014_Art, count18_2015_Art, count18_2016_Art, count18_2017_Art, count18_2018_Art]
            value1_Pho = [count18_2009_Pho, count18_2010_Pho, count18_2011_Pho, count18_2012_Pho, count18_2013_Pho,
                          count18_2014_Pho, count18_2015_Pho, count18_2016_Pho, count18_2017_Pho, count18_2018_Pho]
            value1_Thc = [count18_2009_Thc, count18_2010_Thc, count18_2011_Thc, count18_2012_Thc, count18_2013_Thc,
                          count18_2014_Thc, count18_2015_Thc, count18_2016_Thc, count18_2017_Thc, count18_2018_Thc]
            value1_Dan = [count18_2009_Dan, count18_2010_Dan, count18_2011_Dan, count18_2012_Dan, count18_2013_Dan,
                          count18_2014_Dan, count18_2015_Dan, count18_2016_Dan, count18_2017_Dan, count18_2018_Dan]
            value1_Jou = [count18_2009_Jou, count18_2010_Jou, count18_2011_Jou, count18_2012_Jou, count18_2013_Jou,
                          count18_2014_Jou, count18_2015_Jou, count18_2016_Jou, count18_2017_Jou, count18_2018_Jou]

    attr2 = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
    line2 = Line("2009至2018年初各众筹项目类型数量变化情况", title_pos="center", width=1200)
    line2.use_theme('dark')
    line2.add("Publishing", attr2, value1_Pub, is_smooth=True, legend_pos="%80", legend_orient="vertical")
    line2.add("Film & Video", attr2, value1_Fil, is_smooth=True, legend_pos="%80", legend_orient="vertical")
    line2.add("Music", attr2, value1_Mus, is_smooth=True, legend_pos="%80", legend_orient="vertical")
    line2.add("Food", attr2, value1_Foo, is_smooth=True, legend_pos="%80", legend_orient="vertical")
    line2.add("Design", attr2, value1_Des, is_smooth=True, legend_pos="%80", legend_orient="vertical")
    line2.add("Crafts", attr2, value1_Cra, is_smooth=True, legend_pos="%80", legend_orient="vertical")
    line2.add("Games", attr2, value1_Gam, is_smooth=True, legend_pos="%80", legend_orient="vertical")
    line2.add("Comics", attr2, value1_Com, is_smooth=True, legend_pos="%80", legend_orient="vertical")
    line2.add("Fashion", attr2, value1_Fas, is_smooth=True, legend_pos="%80", legend_orient="vertical")
    line2.add("Theater", attr2, value1_The, is_smooth=True, legend_pos="%80", legend_orient="vertical")
    line2.add("Art", attr2, value1_Art, is_smooth=True, legend_pos="%80", legend_orient="vertical")
    line2.add("Photography", attr2, value1_Pho, is_smooth=True, legend_pos="%80", legend_orient="vertical")
    line2.add("Technology", attr2, value1_Thc, is_smooth=True, legend_pos="%80", legend_orient="vertical")
    line2.add("Dance", attr2, value1_Dan, is_smooth=True, legend_pos="%80", legend_orient="vertical")
    line2.add("Journalism", attr2, value1_Jou, is_smooth=True, legend_pos="%80", legend_orient="vertical")

    page.add(line2)
    page.render()


result()
