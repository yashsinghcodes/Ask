import requests

def main():
	location = input("Enter Your City Name: ")

	res = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+location+"&APPID=8daef122aca4c4d9d40408fb5566bb65")

	data = res.json()

	co = data['main'] ['temp']

	temp_max = data['main'] ['temp_max']

	temp_min = data['main'] ['temp_min']

	conditions = data['weather'] [0] ['main']

	co = co - 273.15

	co = "%.2f" % co

	temp_min = temp_min - 273.15

	temp_max = temp_max - 273.15

	temp_min = "%.2f" % temp_min

	temp_max = "%.2f" % temp_max
	
	print("Your conditions were: "+conditions)

	print("The current temp is: "+str(co)+" in celsius")

	print("The max temp will: "+temp_max+"and temp_min"+temp_min)

	return conditions,temp_min,temp_max

main()
