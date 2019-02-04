import requests
from datetime import datetime

def headlinesinindia():
	main_url = "http://newsapi.org/v2/top-headlines?country=in&publishedAt=datetime.date(datetime.now())&language=en&pageSize=10&apiKey=b9359ff3ab4247b9b3623549e2e1e6a0"
    #can add parameter category = business/entertainment/general/health/science/sports/technology.
    #dont mix category param with sources
    #your apikey is required-> get it at:newsapi.org
    #you can add a parameter source and get 30,000+ domains from newsapi.org
    #you can search for a keyword by adding parameter 'q': for eg: ...v2/top-headlines?q=bitcoin...

    #fetch data from main_url
	fetch_data = requests.get(main_url).json()
     
    
	articles = fetch_data["articles"]
     
    #empty lists to get the title description and url of the news 
	title = []
	description = []
	url = []


	
    #add the title/description/url from the news to the corresponding empty list
	for ar in articles:
		title.append(ar["title"])
		description.append(ar["description"])
		url.append(ar["url"])
		
    #display the lists
	for i in range(len(articles)):
		print(i+1, title[i])
		print('\n')
		print('Description:',description[i])
		print('\n')
		print('Url:',url[i])
		print('\n')

#main
if __name__ == '__main__':
    headlinesinindia()			
		




		
		
		
        	



	    
	    
	    	
	   

	
	
		
		
		
    	


			    	
