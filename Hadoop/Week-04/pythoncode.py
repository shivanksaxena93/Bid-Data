import MySQLdb as my
db=my.connect(host="127.0.0.1",user="root",passwd="itmd521",db="itmd521")
cursor=db.cursor()
f = open("1985.txt","r") #opens file with name of "test.txt"
myList = []
print("Fields are getting inserting")
for line in f:
        no_mention= line[0:4]
        Identifierforstation(UN)= line[4:10]
        StationSeq(WBAN)=line[10:15]
        SpeedofObs=line[15:23]
        TimeofObs=line[23:27]
       	notknown=line[27]
        degreeoflatitudeness=line[28:34]
        degreeoflongitudness=line[34:41]
        randomdata=line[41:46]
        Heightfromsealvl=line[46:51]
        Fieldholdingplace1=line[51:56]
        Fieldholdingplace2=line[56:60]
        directionofwind=line[60:63]
        codequality1=line[63]
        holdingplace1=line[64]
        holdingplace2=line[65:69]
	      holdingplace3=line[69]
        holdingplace4=line[70]
        holdingplaceforceiling= line[70:75]
        place_quality_code= line[76]
        holdingplace5= line[77]
        distanceofvisibility=line[78:84]
        codequality2=line[84]
        holdingplace6=line[85]
        holdingplace7=line[86]
        tempofair=line[87:92]
        codequality3=line[92]
        tempofdew=line[93:98]
        codequality4=line[99]
        atmoshphericpressure=line[99:104]
        codequality5=line[105]
        sql= "insert into record VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"% \
(no_mention,Identifierforstation(UN),StationSeq(WBAN),SpeedofObs,TimeofObs,notknown,degreeoflatitudeness,degreeoflongitudeness,randomdata,Heightfromsealvl,Fieldholdingplace1,Fieldholdingplace2,directionofwind,codequality,holdingplace1,holdingplace2,holdingplace3,holdingplace4,holdingplaceforceiling,place_quality_code,holdingplace5,distanceofvisibility,codequality2,holdingplace6,holdingplace7,tempofair,codequality3,tempofdew,codequality4,atmoshphericpressure,codequality5)
        number_of_rows=cursor.execute(sql)
        db.commit()
        #myList.append(randomdata)
        #myList.append(holdingplace3)
        #myList.append(holdingplace3)
f.close()
db.close()
print("Fields Inserted")
