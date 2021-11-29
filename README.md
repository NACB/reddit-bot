# reddit bots
###### reddit bots created for CMC's CSCI040 class
###### (The specific requirements for this assignment can be found at the [course webpage](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_04))




## What did the bots do?
These bots ran a madlibs type text generator to create reddit comments promoting certain political candidates. Of the five bots I was running simultaneously, four created pro-Trump comments, and one generated pro-left comments. The text of these comments was inspired by the types of messages seen on fake social media accounts during the 2016 and 2020 elections.

#### Complications
These bots are fully functional, *which is not to say they ran perfectly smoothly*. After obtaining **over 800 valid comments _on each bot_**, the first subreddit being used was banned. After hitting **over 500**, the second subreddit was shut down. Additionally, on *some, but not all* of the bots, the number of valid comments generated began to decrease suddenly and unexpectedly. In light of this, please note that if you run the `bot_counter.py` file yourself, the number of comments may not exactly match those posted below. I continued to run the bots *after* obtaining the required 500 comments per bot in the hope of obtaining 1000 on any one of them. As a result, the outputs may be lower or higher than those saved and recorded below. 

## Photographic Evidence
[This post can be found in the wild here](https://www.reddit.com/r/BotTown2/comments/r0yi9l/comment/hmgkjtn/?utm_source=share&utm_medium=web2x&context=3)
![reddit post](https://github.com/NACB/reddit-bot/blob/main/bot.jpg?raw=true)
I like this post because it looks (both funnily and concerningly enough) like a conversation you would find on a grandmother's facebook page.

## Optional work done
Many of the optional tasks were completed. These are listed below:
- 100 valid comments posted on one bot
- 500 valid comments posted on one bot
- 5 bots run simultaneously, each producing at least 500 valid comments

The task *1000 valid comments posted on one bot* was (frustratingly) nearly achieved, but remained consistently out of reach. Subreddits would either get banned, or bots would invalidate their own comments. 

## Bot Counts (via the bot_counter)
The command line input as well as the output for running the `bot_counter.py` file on each of my bots is shown below. 
###### bot 1
```
PS C:\Users\natha\OneDrive\Desktop\CMC2021-2\CSCI040\reddit_bot> python3 bot_counter.py --username=CSCIbot
len(comments)= 1000
len(top_level_comments)= 2
len(replies)= 998
len(valid_top_level_comments)= 2
len(not_self_replies)= 998
len(valid_replies)= 708
========================================
valid_comments= 710
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
```

###### bot 2
```
PS C:\Users\natha\OneDrive\Desktop\CMC2021-2\CSCI040\reddit_bot> python3 --username=CSCIbot-jr --praw_name=bot2
len(comments)= 1000
len(top_level_comments)= 0
len(replies)= 1000
len(valid_top_level_comments)= 0
len(not_self_replies)= 1000
len(valid_replies)= 905
========================================
valid_comments= 905
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
```

###### bot 3
```
PS C:\Users\natha\OneDrive\Desktop\CMC2021-2\CSCI040\reddit_bot> python3 --username=CSCIbot-affiliate --praw_name=bot3
len(comments)= 1000
len(top_level_comments)= 5
len(replies)= 995
len(valid_top_level_comments)= 1
len(not_self_replies)= 995
len(valid_replies)= 913
========================================
valid_comments= 914
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
```

###### bot 4
```
PS C:\Users\natha\OneDrive\Desktop\CMC2021-2\CSCI040\reddit_bot> python3 bot_counter.py --username=another_CSCIbot_2 --praw_name=bot4
len(comments)= 1000
len(top_level_comments)= 553
len(replies)= 447
len(valid_top_level_comments)= 106
len(not_self_replies)= 447
len(valid_replies)= 429
========================================
valid_comments= 535
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit   
```

###### bot 5
```
PS C:\Users\natha\OneDrive\Desktop\CMC2021-2\CSCI040\reddit_bot> python3 bot_counter.py --username=opp_bot --praw_name=bot5
len(comments)= 1000
len(top_level_comments)= 78
len(replies)= 922
len(valid_top_level_comments)= 54
len(not_self_replies)= 922
len(valid_replies)= 786
========================================
valid_comments= 840
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
```


## Score?
1. Because of the successful completion of the mandatory tasks, and the creation of this GitHub Repo, 20 points should be awarded.
2. Because of the successful completion of the task *100 valid comments posted on one bot*, 2 points should be awarded.
3. Because of the successful completion of the task *500 valid comments posted on one bot*, 2 points should be awarded.
4. Because of the successful completion of the task *5 bots run simultaneously, each producing at least 500 valid comments*, 2 points should be awarded.
##### In total, 26/30 points were earned. 
###### Naturally, there are no objections to recieving more than this amount.
