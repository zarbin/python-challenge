# Python Challenge - Module 3 Homework
Module 3 Challenge for UTA DataViz Bootcamp

# PyBank

The purpose of this assignment is to read in an external CSV file, Loop through each row, and produce financial analysis that are outputted to both the termainal and into a text file. 

The biggest challenge was tracking the changes of P&L over the entire period and keeping greatest increase/decrease in profit stored for output at the ned.  

I used a somewhat complicated conditional (if statement) to manage this but I think there is a more elegant solution. Below are my finals results. 

**PyBank Results Screenshot**

![image](https://user-images.githubusercontent.com/36682023/200943430-01eed6cb-30b1-4eec-8e66-1ec45e7bd276.png)

# PyPull

The purpose of this assignment is to read in an external CSV file, Loop through each row, and produce polling results that are outputted to both the termainal and into a text file. 

Using a dictionary to store a key pair that tracks unique political contender and their respective vote count seems like an elegant and effecient solution to me. 

```python
#Use dictionary to tally votes per candidate as we loop through  
#check if candidate is in dictionary.  If not add new dict key, if present increment their vote count
if row[2] not in vote_results.keys():
  vote_results[row[2]] = 1
else:
  vote_results[row[2]] += 1
```

**PyPull Results Screenshot**

![image](https://user-images.githubusercontent.com/36682023/200943598-c12c34c6-648b-4ed8-b222-1ccaeee84321.png)
