Problem: 
You are in charge of a server that needs to run some submitted tasks on a first-come, first-served basis. Each day, you can dedicate the server to run these tasks for at most T minutes. Given the time each task takes, you want to know how many of them will be finished today.

Consider the following example:

Assume T=180 and the tasks take 45, 30, 55, 20, 80 and 20 minutes (in the order that they are submitted). Then, only four tasks can be completed. The first four tasks can be completed because they take 150 minutes, but not the first five, because they take 230 minutes which is greater than 180. Notice that although there is enough time to perform the sixth task (which takes 20 minutes) after completing the fourth task, you cannot do that because the fifth task is not done yet.

Input

The input consists of a two lines. 

The first line contains two integers n and T.
1 ≤ n ≤ 50 is the number of tasks 
1 ≤ T ≤ 500 is the total amount of execution time available. 

The second line contains n positive integers, separated by spaces, smaller than 100, indicating how long each task takes in order they are submitted (the same order they must be evaluated in).
1 < n < 100 - the input looks like this:
n n n n n 

Output
Display (by printing) the number of tasks that can be completed in T minutes on a first-come, first-served basis.

Sample Input 1
6 180
45 30 55 20 80 20

Sample Output 1
4


Sample Input 2
10 60
20 7 10 8 10 27 2 3 10 5

Sample Output 2
5




Solution: 
def server_time_check(task_config, task_times):
  task_config = task_config.split()
  
  num_of_tasks = int(task_config[0])
  max_time = int(task_config[1])
  task_times = task_times.split()
  
  current_time = 0
  current_tasks = 0
  
  for index in range(num_of_tasks):
    if int(task_times[index]) + current_time <= max_time:
      current_time = int(task_times[index]) + current_time
      current_tasks = 1 + current_tasks
    else:
      break
  print(current_tasks)




Process: 
split task_config to get each variable
split task_times to a list 
create variable for time of tasks we can complete 
create a variable for amount of task completed
for loop through the list of time tasks
	if time of task var + list at the index < 180, 
	    then add to var and 1 to amount of task completed var
	else, break from the for loop 
return the tasked completed var


