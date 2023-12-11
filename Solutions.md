Some of the code may be modified after submission.

Day 1-9:
Might write up solutions later.

Day 10:
ChatGPT-3.5'd what you see in GPT-Original.py. See 10.py for the actual solution.
Part 1 is self-explanatory. Then, after the preprocessing for day 2 you see in 10.py, I used nvim to replace the bars with the ASCII Box drawing characters as in here: https://gist.github.com/01-1/ba989a502bed38c3cfe48832967b358b#file-asciitable-txt
Then, I used GIMP to flood fill, and manually counted 139 of the squares. I used nvim to select and gedit to count the rest, which you can see in the text file 10q.

Day 11:
First part - generate the grid using transpose, self-explanatory
Second part - just multiply (distance from first part - distance before expansion) * (999999) + distance before expansion

I used GPT *partially* (not fully, as it usually doesn't generate working code) for a few other solutions as well from days 7 onward.
