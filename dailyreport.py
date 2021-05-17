import csv
def produceReport(list):
    content = ''
    header = open("header.txt", "r")
    beeffile= open('dailyreport.csv', mode='w', newline='')
    beef_writer = csv.writer(beeffile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for l in list:
        content += '<tr>'
        content += '<td>'+l.name+'</td>'
        content += '<td>'+l.shop+'</td>'
        content += '<td>'+l.price+'</td>'
        content += '<td>'+l.uprice+'</td>'
        content += '<td><a href=\"'+ l.url+'\">'+l.url+'</a></td>'
        content += '</tr>'
        beef_writer.writerow([l.name,l.shop,l.price,l.uprice,l.url])
    footer = open("footer.txt", "r")
    #print(header.read()) 
    f = open("dailyreport.html", "w")
    f.write(header.read()+content+footer.read())
    f.close()

if __name__ == "__main__":
    produceReport(list())