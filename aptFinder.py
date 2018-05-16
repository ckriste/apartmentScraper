import urllib.request
from bs4 import BeautifulSoup
import MySQLdb
from bs4 import NavigableString

db = MySQLdb.connect("localhost","ckristek","password","apartments" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")
# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Database version : %s " % data)

with open('urls.txt') as inf:
    urls = (line.strip() for line in inf)
    for url in urls:
        request = urllib.request.Request(url)
        html = urllib.request.urlopen(request).read()
        soup = BeautifulSoup(html, "lxml")
        for ul in soup.find_all("div", {"class": "result"}):

            #Find apt name
            name = url.rsplit('/',1)[-1]

            #Find Unit #
            unit = "XXXX"
            #unit = [unit.rsplit('/', 1)[-1]]

            #Find Price Range
            price = ul.select('li[class="price-range"]')
            price = [p.text for p in price]
            price = ''.join(price)

            #Get Web Special
            webSpecial = ul.select('h3[class="webspecial"]')
            webSpecial = [w.text for w in webSpecial]


            #Find move in
            moveIn = ul.select('li[class="move-in-dates"]')
            moveIn = [m.text for m in moveIn]
            moveIn = ''.join(moveIn)

            #Find # of Beds
            bedrooms = ul.select('li[class="beds"]')
            bedrooms = [b.text for b in bedrooms]
            bedrooms = ''.join(bedrooms)

            #Find # of baths
            bath = ul.select('li[class="baths"]')
            bath = [ba.text for ba in bath]
            bath = ''.join(bath)

            #Find sqft
            sqft = ul.select('li[class="sqft"]')
            sqft = [s.text for s in sqft]
            sqft = ''.join(sqft)

            #print("Apartment Name:%s\n \tUnit:%s\n \tPrice:%s\n \tMove In:%s\n \tBedrooms:%s\n \tBathrooms:%s\n \tSQ.FT:%s \n" % (name, unit, price, moveIn,bedrooms, bath, sqft))


            add_apt = ("INSERT INTO apts2 "
                        "(unit, price, name, moveIn,bedrooms,bath,sqft) "
                         "VALUES (%(unit)s, %(price)s, %(name)s, %(moveIn)s, %(bedrooms)s, %(bath)s,%(sqft)s )")

            data_apt = {
                'unit' : unit,
                'price' : price,
                'name': name,
                'moveIn': moveIn,
                'bedrooms': bedrooms,
                'bath': bath,
                'sqft' : sqft,
                }


            cursor.execute(add_apt,data_apt)
            db.commit()


db.close()


#res.find_all("h3")[0].text

#for ul in results:
    #name = ul.find('h5').text
    #address = ul.find("li", attrs={'class':'address'}).text
    #bedrooms = ul.find("li", attrs={'class':'bedrooms'}).text
    #bath = ul.find("li", attrs={'class':'baths'}).text
    #sqft = ul.find("li", attrs={'class':'sqft'}).text

    #add_apt = ("INSERT INTO apts "
              #"(name, address, bedrooms, bath,sqft) "
             #"VALUES (%(name)s, %(address)s, %(bedrooms)s, %(bath)s, %(sqft)s)")

    #data_apt = {
        #'name': name,
        #'address': address,
        #'bedrooms': bedrooms,
        #'bath': bath,
        #'sqft' : sqft,
    #}

    #cursor.execute(add_apt,data_apt)
    #db.commit()

    #print("Total score for %s is %s" % (name, score))

    #print("%s \n \t%s\n \t%s\n \t%s\n \t%s" % (name, address, bedrooms, bath, sqft))
