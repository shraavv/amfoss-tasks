from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.espncricinfo.com/live-cricket-score').text 

soup = BeautifulSoup(source,'lxml')

division = soup.find('div')

file = open('livescore.csv','w',newline='')
csv_writer = csv.writer(file)

script = division.find('script',type='application/ld+json')
code = script.string

length = len(code)

dic = code[0:length+1]

my_dic = eval(dic)

date_ = division.find('div', class_='ds-flex ds-justify-between ds-items-center')
date = date_.find('div', class_='ds-text-tight-xs ds-truncate ds-text-typo-mid3').text

details=[]
count = 0
for team in division.find_all('div', class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1'):
    if count<2:
        try:
            overs = team.span.text
            details.append(overs)
            runs = team.strong.text
            details.append(runs)
        except:
            pass
        count+=1
    else:
        break

list_count = len(details)

status_ = division.find('p', class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo')
status = status_.span.text

if list_count >= 2:
    title=my_dic['name']
    team_details=title.split('vs')
    line2 = team_details[0]
    title_ = team_details[1]
    title_ = title_.split(' ')
    line3 = title_[1]
    line4=''
    for i in details:
        line4 += i
    line5=status
    line6=date
    data=[line2,line3,line4,line5,line6]
    csv_writer.writerow(data)
else:
    line1='no live score available :('
    line2='please try again later'
    csv_writer.writerow([line1,line2])

file.close()
