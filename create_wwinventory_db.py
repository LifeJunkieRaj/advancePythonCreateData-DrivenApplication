import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd12!")

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE wwinventory")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd12!",
    database="wwinventory")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE inventory (productcode VARCHAR(30), dept VARCHAR(30), supplierid VARCHAR(20), description VARCHAR(255), unitsinstock INTEGER(6), targetinventory INTEGER(6), reorderlevel INTEGER(6), location VARCHAR(20), rack VARCHAR(10), origin VARCHAR(20), unitcost DECIMAL(10,2), retailprice DECIMAL(10,2))")

sql = "INSERT INTO inventory (productcode, dept, supplierid, description, unitsinstock, targetinventory, reorderlevel, location, rack, origin, unitcost, retailprice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = [
    ("bathhw-2","Bathroom","WOODSTOCK","Windsor Model 24 Double Towel Bar Brushed Nickel",22,25,10,"Showroom","2-3a","China",35.00,41.00),
    ("bathhw-3","Bathroom","WOODSTOCK","Windsor Model 24 Single Towel Bar Brushed Nickel",18,25,10,"Showroom","2-3b","China",27.00,31.00),
    ("bathhw-32","Bathroom","MALOOF","4 in. 2-Handle Low-Arc 4 Bathroom Faucet in Vibrant Brushed Nickel",5,25,10,"Showroom","2-3c","China",87.00,109.00),
    ("bathhw-34","Bathroom","WOODSTOCK","Antique 8 in. 2-Handle Low Arc Bathroom Faucet Polished Brass",6,25,10,"Showroom","2-3d","China",388.00,420.00),
    ("bathhw-4","Bathroom","WOODSTOCK","Edinburgh Model 24 Double Towel Bar Brass",6,25,10,"Showroom","2-3c","China",22.00,29.00),
    ("bathhw-5","Bathroom","WOODSTOCK","Edinburgh Model 24 Single Towel Bar Brass",14,25,10,"Showroom","2-3d","China",14.00,19.00),
    ("bathhw-6","Bathroom","WOODSTOCK","Albany Model 24 Double Towel Bar Plastic",8,25,10,"Showroom","2-3e","China",6.00,12.00),
    ("bathhw-7","Bathroom","WOODSTOCK","Albany Model 24 Single Towel Bar Plastic",8,25,10,"Showroom","2-3f","China",5.00,9.00),
    ("deck-32","Deck Patio","KER","White Painted Metal and Glass Patio Chair and Table Set",5,25,10,"Basement","5","Brazil",350.00,425.00),
    ("deck-34","Deck Patio","KER","Black Painted Metal and Glass Patio Chair and Table Set",8,25,10,"Basement","5","Brazil",340.00,415.00),
    ("dk-psg-01","Materials","PUGG","Brilliant Chrome Privacy Knob",15,50,25,"Showroom","3","China",7.50,8.99),
    ("dk-psg-02","Materials","PUGG","Brilliant Brass Privacy Knob",12,50,25,"Showroom","3","China",5.50,7.99),
    ("dk-psg-03","Materials","PUGG","Brilliant Brushed Nickel Privacy Knob",16,50,25,"Showroom","3","China",9.50,10.99),
    ("dk-psg-11","Materials","PUGG","Cosgrove Chrome Privacy Knob",6,50,25,"Showroom","3","China",7.50,8.99),
    ("dk-psg-12","Materials","PUGG","Cosgrove Brass Privacy Knob",12,50,25,"Showroom","3","China",5.50,7.99),
    ("dk-psg-13","Materials","PUGG","Cosgrove Brushed Nickel Privacy Knob",18,50,25,"Showroom","3","China",9.50,10.99),
    ("hinge-12","Hardware","PUGG","Nickel-Plated Face Frame Hinge",35,100,50,"Showroom","11-3a","China",6.32,7.49),
    ("hinge-14","Hardware","PUGG","Self-Closing Face Frame Hinge",88,100,50,"Showroom","11-3b","China",4.32,5.00),
    ("hinge-15","Hardware","PUGG","Self-Closing Face Frame Hinge",88,100,50,"Showroom","11-3b","China",4.32,5.00),
    ("hinge-16","Hardware","WOODSTOCK","Brass Flat-Tipped Butt Hinge",0,100,50,"Showroom","11-3c","Mexico",1.75,2.39),
    ("hinge-18","Hardware","PUGG","Back to Back Wraparound Insert Hinge",64,100,50,"Showroom","11-3d","Mexico",0.99,1.35),
    ("hinge-22","Hardware","PUGG","Soft Close Clip Top Overlay Hinge",12,100,50,"Showroom","11-3e","UK",2.22,3.55),
    ("hinge-24","Hardware","PUGG","Concealed Double Jointed Hinge",45,100,50,"Showroom","11-3f","USA",3.55,5.65),
    ("hinge-25","Hardware","PUGG","Self-Closing Face Frame Hinge",88,100,50,"Showroom","11-3b","China",4.32,5.00),
    ("hinge-26","Hardware","PUGG","Variable Overlay Decorative Hinge",49,100,50,"Showroom","11-3g","USA",2.75,3.55),
    ("hinge-28","Hardware","PUGG","Snap Closing Semi Concealed Hinge",52,100,50,"Showroom","12-3a","Germany",2.29,4.32),
    ("hinge-32","Hardware","PUGG","Brass Butler Tray Table Hinge",45,50,25,"Showroom","12-3b","Mexico",3.23,5.65),
    ("hinge-46","Hardware","PUGG","Slotted 36"" Brass Piano Hinge",22,50,25,"Showroom","13-1a","China",12.43,15.99),
    ("hmdecor-16","Décor","KER","White Faux Wood Blind, 2 in. Slats, 35 in. W x 64 in. L",45,50,25,"Showroom","16","Canada",28.00,33.00),
    ("hmdecor-18","Décor","KER","White Faux Wood Blind, 2 in. Slats, 32 in. W x 64 in. L",12,50,25,"Showroom","16","Canada",26.00,31.00),
    ("hmdecor-2","Décor","KER","Chocolate 7 ft. 7 in x 10 ft. 10 in Indoor and Outdoor Area Rug",12,25,10,"Showroom","4-1a","India",52.43,108.97),
    ("hmdecor-25","Décor","KER","White Faux Wood Blind, 2 in. Slats, 28 in. W x 54 in. L",50,50,25,"Showroom","16","Canada",25.00,29.00),
    ("hmdecor-4","Décor","KER","Ebony 9 Ft. 9 In. x 13 Ft. 9 In. Area Rug",6,25,10,"Showroom","4-1a","India",42.00,56.00),
    ("hmdecor-6","Décor","KER","Daisy Print 7 ft. 9 in. x 10 ft. 10 in. Indoor / Outdoor Area Rug",9,25,10,"Showroom","4-1a","India",67.43,97.99),
    ("hmdecor-8","Décor","KER","Braided 8 ft. x 11 ft. Area Rug",9,25,10,"Showroom","4-1a","India",132.23,199.00),
    ("pak-ashwt-24","Lumber","ARBORHARVEST","Project Pack - 24 Board Feet 3/4 Select White Ash",3,50,5,"Shed A","12","USA",50.00,107.71),
    ("pak-baswd-25","Lumber","ARTURO","Project Pack - 25 Board Feet 3/4 Select Basswood",10,50,5,"Basement","2","USA",40.00,87.52),
    ("pak-btrnt-25","Lumber","GREENE","Project Pack - 25 Board Feet 3/4 Select Butternut",12,50,5,"Shed A","5","USA",52.00,125.66),
    ("pak-chrbk-25","Lumber","LIMBERT","Project Pack - 25 Board Feet 3/4 Select Black Cherry",6,50,5,"Shed B","3","USA",82.00,171.67),
    ("pak-mplhd-23","Lumber","ARTURO","Project Pack - 23 Board Feet 3/4 Select Hard Maple",40,50,5,"Shed B","4","USA",67.00,117.81),
    ("pak-mplrd-25","Lumber","ARTURO","Project Pack - 25 Board Feet 3/4 Select Red Maple",15,50,5,"Shed B","2","USA",56.00,102.10),
    ("pak-oakrd-23","Lumber","NAKASHIMA","Project Pack - 23 Board Feet 3/4 Select Red Oak",23,50,5,"Shed C","4","USA",48.00,109.96),
    ("pak-oakwq-23","Lumber","NAKASHIMA","Project Pack - 23 Board Feet 3/4 Select Quartersawn White Oak",12,50,5,"Shed C","5","USA",78.00,139.13),
    ("pak-oakwt-23","Lumber","NAKASHIMA","Project Pack - 23 Board Feet 3/4 Select White Oak",22,50,5,"Shed C","2","USA",49.00,109.96),
    ("pak-poptu-25","Lumber","UNDERHILL","Project Pack - 25 Board Feet 3/4 Tulip Poplar",23,50,5,"Basement","1","USA",42.00,87.52),
    ("pak-walbk-25","Lumber","NORMS","Project Pack - 25 Board Feet 3/4 Black Walnut",12,50,5,"Shed B","4","USA",81.00,170.54),
    ("win-dbl-3000","Materials","WOODSTOCK","Fenster Double-Hung Vinyl Window 34-1/4 in. x 57-1/4 in., White, Argon",52,100,25,"Mill","5","USA",182.00,203.00),
    ("win-dbl-8000","Materials","WOODSTOCK","Fenster Double-Hung Vinyl Windows, 32 in. x 62 in. White, Argon",22,100,25,"Mill","5","USA",165.00,180.00),
    ("win-dbl-8216","Materials","WOODSTOCK","Fenster Double-Hung Wood Window, 32 in. x 38 in., Natural, Low E",12,100,25,"Mill","5","USA",148.00,167.00),
    ("win-dbl-8217","Materials","WOODSTOCK","Fenster Double-Hung Wood Twin Window, 32 in. x 54 in., Natural, Low E",23,100,25,"Mill","5","USA",387.00,415.00),
    ("win-dbl-9210","Materials","WOODSTOCK","Fenster 21 in. x 45-1/2 in. Venting Deck-Mount Skylight",12,25,10,"Mill","6","USA",750.00,830.00)
]

mycursor.executemany(sql, val)

mydb.commit()
mydb.close()

print(mycursor.rowcount, "record inserted.")
