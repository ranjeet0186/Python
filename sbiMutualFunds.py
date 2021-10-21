import requests
import json
import matplotlib.pyplot as plt
source = requests.get(
        'https://www.quandl.com/api/v3/datasets/BSE/BOM532366.json?api_key=Gx6PGxExnasPyA44s1pr')
data = json.loads(source.text)
my_data = data['dataset']['data']
useful_data = [i[1] for i in reversed(my_data)]
#print(useful_data)
#dates = [i[0] for i in my_data]
x_data = [i for i in range(len(useful_data))]
#print(len(x_data))
#print(x_data)
plt.plot(x_data,useful_data)
plt.xlabel("Time")
plt.ylabel('Stock Price')
plt.title('SBI ')
plt.show()
    
