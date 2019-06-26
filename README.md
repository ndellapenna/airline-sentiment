# airline-sentiment

##Evaluate sentiment of customer tweets

This simple script can be used to gauge the feelings consumers express via 
Twitter. Since it is rather tedious to have someone manually scan each 
individual tweet, this program can be used to estimate the number of positive, 
neutral, and negative tweets submitted my matching found sentimental keywords 
to those in a simple 5 to 6 word dictionary. 

The logic behind the procedure for the program is based on three formulas:

`f_positive` = 0.93(n_great) + 0.87(n_thank)+0.71(n_thanks)+0.53(n_love)+
0.46(n_appreciate)

`f_neutral` =0.74(n_do)+0.68(n_add)+0.62(n_rt)+0.51(n_dm)+0.39(n_can)+
0.26(n_please)

`f_negative` = 1.2(n_worst)+1.08(n_hours)+0.97(n_delay)+0.43(n_no)+0.41(n_why)

After computing each value, the program will output the highest of the three 
values-- e.g if the value of `f_positive` is greater than `f_neutral` and 
`f_negative` the sentiment will 
be _positive_.

In this program, I have used a sentiment analysis dataset that originally 
came from "Crowdflower's Data for Everyone library".

