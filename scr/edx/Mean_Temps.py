mean_temps = open("scr/mean_temp.txt", 'a+')
mean_temps.write("Rio de Janeiro,Brazil,30.0,18.0\n")
mean_temps.seek(0)
headings = mean_temps.readline()
split_header = headings.split(',')
city_temp = mean_temps.readline()
while city_temp:
    city_temp.strip('\n')
    split_list = city_temp.split(',')
    print(split_header[0] + " of " + split_list[0] + " " + split_header[2] + " is " + split_list[2] + " Celsius")
    city_temp = mean_temps.readline()
mean_temps.close()