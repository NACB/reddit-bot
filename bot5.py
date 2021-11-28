import praw
import random
import datetime
import time

madlibs = [
    "[I] [DISLIKE] [TRUMP]. [DEMOCRATS] are [BETTER].",
    "To make things [BETTER] for America, pick [DEMOCRATS] over [TRUMP].",
    "[DEMOCRATS] are [BETTER] for our country.",
    "[TRUMP] is worthy of [DISLIKE]. A [BETTER] choice is [DEMOCRATS].",
    ]

replacements = {
    'I' : ['I', 'People', 'Real Americans', 'Smart people'],
    'DISLIKE' : ['dislike', 'scorn', 'hate'],
    'TRUMP' : ['Donald Trump', 'Donald J Trump', 'Donny T', 'The Donald', 'Trump', 'Bossman T'],
    'DEMOCRATS' : ['Democrats', 'Leftists', 'Rational politicians'],
    'BETTER' : ['Better', 'an improvement', 'superior'],
    }

def generate_comment():

    comment = random.choice(madlibs)
    for key in replacements.keys():
        comment = comment.replace("["+key+"]", random.choice(replacements[key]))
    return comment

reddit = praw.Reddit('bot5')  #CHANGE
submission_url = 'https://www.reddit.com/r/BotTown2/comments/r3pyx9/anchor_2/'   #CREATE NEW HOME SUBMISSION
submission = reddit.submission(url=submission_url)

while True:
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    submission.comments.replace_more(limit=None)
    all_comments = []
    for comment in submission.comments.list():
        all_comments.append(comment)
    print('len(all_comments)=',len(all_comments))

    not_my_comments = []
    for comment in all_comments:
        if str(comment.author) != 'opp_bot':   #CHANGE
            not_my_comments.append(comment)
    print('len(not_my_comments)=',len(not_my_comments))
    
    has_not_commented = len(not_my_comments) == len(all_comments)
    if has_not_commented:
        text = generate_comment()
        try:
            submission.reply(text)
        except praw.exceptions.RedditAPIException as error:
            print('waiting 120s because', error)
            time.sleep(120)
    else:
        comments_without_replies = []
        for comments in not_my_comments:
            not_replied = True
            for comment in comments.replies:
                if str(comment.author) != 'opp_bot':   #CHANGE
                    not_replied = False
            if not_replied:
                comments_without_replies.append(comments)

        print('len(comments_without_replies)=',len(comments_without_replies))

        for comments in comments_without_replies:
            selection = random.choice(comments_without_replies)
            generated_reply = generate_comment()
            try:
                selection.reply(generated_reply)
            except praw.exceptions.APIException as error:
                if "DELETED_COMMENT" in str(error):
                    print('not replying to deleted comment')
                else:
                    pass
            except praw.errors.RateLimitExceeded as error:
                print('waiting, because', error)
                pass
            except praw.exceptions.RedditAPIException:
                print('waiting 120s because', error)
                time.sleep(120)
    
    randomnumber = random.random()
    allsubmissions = []
    if randomnumber >= 0.9:
        print('Checking the BotCave for unwanted political opinions...')
        submission = reddit.submission(url='https://www.reddit.com/r/BotTown2/comments/r3pyx9/anchor_2/')
        try:
            submission.reply(generate_comment())
        except praw.exceptions.RedditAPIException as error:
            print (error)
            time.sleep(120)
    if randomnumber < 0.9:
        print('Infiltrating Top Subreddits')
        for submission in reddit.subreddit('BotTown2').hot(limit=5):
            allsubmissions.append(submission)
        newsubmission = random.choice(allsubmissions)
        submission = reddit.submission(id=newsubmission)
        print('Submission ID: ', newsubmission)
        print(newsubmission.title)

        time.sleep(1)