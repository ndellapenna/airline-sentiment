#******************************************************************************
# airlines.py
#******************************************************************************
# Name: Nadia Della Penna
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#none
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#Any comment line that features two hashtags was personally used
#during the debugging process.
# =============================================================================
# The purpose of this project is was to further my understanding of the pandas 
# library. This is a useful way for brand managers to keep up with the public's 
# feelings about a particular service, product, or company. Rather than taking the 
# time to read through a catalog of 4000 tweets, a program such as this can save one 
# time in evaluating unquantified fields as such. 
# =============================================================================

import pandas as pd

#conv_dict method below is used to convert any two column file into a dictionary.
def conv_dict(f):
    f1 = open(f, "r") 
    f1_split = f1.read().split()
##    print(f1_split)
    f1_key_list = []
    f1_val_list =[]
    for i in range(len(f1_split)):
        if i ==0 or i%2==0:
            f1_key_list.append(f1_split[i])
        else:
            f1_val_list.append(f1_split[i])
##    print(f1_key_list, f1_val_list, "**")
    #This program will return a dict.
    return dict(zip(f1_key_list,f1_val_list)) 

#predict_st method will be used to predict the overall sentiment of a tweet.
def predict_st (tweet): 
    
    #The three files I have created are formatted as a two column list, featuring
    #specific keywords and their respective values are converted below to assist
    #in evaluating a estimated sentimental value.  
    neg_words = conv_dict("negwords_c.txt")               
    neut_words = conv_dict("neutwords_c.txt")
    pos_words = conv_dict("poswords_c.txt")
    
    #Running sums will be useful to evaluate each individual tweet.
    neg_sum = 0
    neut_sum = 0
    pos_sum = 0
    
    #We will iterate through our tweet, word by word, to scan for sentiment
    #keyword matches.
    word_list= list(tweet.split())
    for word in word_list: #This for-loop below will update our running sums.
        word = word.lower() #Used to account for identity.
        if word in neg_words:
            neg_sum+= float(neg_words[word])
        elif word in neut_words:
            neut_sum +=float(neut_words[word])
        elif word in pos_words:
            pos_sum+= float(pos_words[word])
            
    #Ultimately, this function will return whether a tweet is qualified as 
    #negative, neutral, positive or tie, which depend on our running 
    #sums from above.         
    if neg_sum > neut_sum and neg_sum > pos_sum:
        return "negative"
    elif neut_sum > neg_sum and neut_sum > pos_sum:
        return "neutral"
    elif pos_sum > neg_sum and pos_sum > neut_sum:
        return "positive"
    else:
        return "tie" 

#Below, this program will keep track of the total number of negative, neutral, 
#positive, or "tied" tweets.
tot_neg = 0
tot_neut = 0
tot_pos= 0    
tot_tie=0    
    
tweet_df= pd.read_csv("tweet_c.csv")
##print(tweet_df.columns)
text_col = tweet_df["text"]
##print(text_col)

for i in text_col:
    if predict_st(i)== "negative":
        tot_neg+=1
    elif predict_st(i)== "neutral":
        tot_neut+=1
    elif predict_st(i)== "positive":
        tot_pos+=1
    else:
        tot_tie+=1

print("Tweet Sentiments \n{0:9}: {1}".format('Positive', tot_pos))
print("{0:9}: {1}".format('Neutral',tot_neut))
print("{0:9}: {1}".format('Negative',tot_neg))

