# import the required libraries 
import random 
import matplotlib.pyplot as plt 
    
# store the random numbers in a  
# list 
nums = [] 
mu = 100
sigma = 50
#perturber la valeur de mu on utilisant un bruit gaussian avec 
print(mu)
print(random.gauss(mu, sigma))   



for i in range(100): 
    temp = random.gauss(mu, sigma)
    nums.append(temp) 
        
# plotting a graph 
plt.plot(nums)
plt.hist(nums, bins = 200)