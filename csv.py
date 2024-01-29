import csv
field=["name","branch","ear","cgpa"]
rows=[["abhoi","cs","46","2.3"],
      ["abhilasha","sd","55","2.3"]]
filename="university records.csv"
with open("university records.csv","w")as csvfile:
    csvwriter= csv.writer(csvfile)
    
    
