from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
import pandas as pd
import Twitter_usertimeline
import Twitter_searchtweets

'''GUI OF Twitter Sentiment Analysis'''
root=Tk()
root.title("Twitter Sentiment Analysis")
root.geometry('720x460+300+100')
root.configure(background="floral white")
head=Label(root,text="SENTIMENT ANALYSIS ",fg="black",relief=GROOVE,font=("Impact 30"),bg="cornsilk3",bd=12,borderwidth=10)
head.pack(side=TOP)
l1=Label(root,text="1) Sentiment analysis of a keyword",bg="cornsilk3",font = ('Impact',12)).place(x=0,y=90)
l2=Label(root,text="2) Sentiment analysis of a person",bg="cornsilk3",font = ('Impact',12)).place(x=0,y=130)
l3=Label(root,text="Enter your choice :",bg="cornsilk3",font = ('Impact',12)).place(x=0,y=180)
e=Entry(root)
e.place(x=150,y=180)
def click():
    '''For getting tweets and analyzing them'''
    def get_tweets_for_analysis(S,search):
        df = pd.DataFrame()
        tweets=[]
        tlist=[]
        if S==1:
          twitter_sentiment_analysis_st=Twitter_searchtweets.Twitter_Sentiment_search_tweet()
          tweets=twitter_sentiment_analysis_st.get_tweets(search)
          df=twitter_sentiment_analysis_st.tweet_to_frame(tweets)
          for i in tweets:
               tweet_dict = {}
               tweet_dict['text'] = i.text
               tweet_dict['sentiment'] = twitter_sentiment_analysis_st.get_tweet_sentiment(i.text)
               tlist.append(tweet_dict)
        else:
          twitter_sentiment_analysis_ut=Twitter_usertimeline. Twitter_Sentiment_user_timeline()
          tweets=twitter_sentiment_analysis_ut.get_user_timeline(search)
          df=twitter_sentiment_analysis_ut.tweet_to_frame(tweets)
          for i in tweets:
               tweet_dict = {}
               tweet_dict['text'] = i.text
               tweet_dict['sentiment'] = twitter_sentiment_analysis_ut.get_tweet_sentiment(i.text)
               tlist.append(tweet_dict)
        print(df.head(200))
        positweets = [tweet for tweet in tlist if tweet['sentiment'] == 'positive']
        negatweets = [tweet for tweet in tlist if tweet['sentiment'] == 'negative']
        print("\n\nPositive tweets:")
        for tweet in positweets[:10]:
         print(tweet['text'])
        print("\n\nNegative tweets: ")
        for tweet in negatweets[:10]:
          print(tweet['text'])
                
        rt=Tk()
        rt.geometry("1000x800+250+200")
        l1=Label(rt,text="TWEETS",fg="black",relief=GROOVE,font=("Impact 20"),borderwidth=1).pack()
        frame=Frame(rt)
        frame.pack(pady=30)
        cols = list(df.columns)
        tree = ttk.Treeview(frame,selectmode='browse')
        verscrlbar = ttk.Scrollbar(frame,orient ="vertical",command = tree.yview)
        verscrlbar.pack(side =RIGHT, fill =Y)
        hbar = ttk.Scrollbar(frame,orient ="horizontal",command = tree.xview)
        hbar.pack(side =BOTTOM, fill =X)
        tree.pack(side=LEFT)
        tree.configure(xscrollcommand = hbar.set)
        tree.configure(yscrollcommand = verscrlbar.set)
        tree["columns"] = cols
        for i in cols:
          tree.column(i, anchor="w")
          tree.heading(i, text=i, anchor='w')

        for index, row in  df[::-1].iterrows():
           tree.insert("",0,text=index,values=list(row))

        positive=len(df[df['Sentiment'] == 'positive'])
        negative=len(df[df['Sentiment'] == 'negative'])
        neutral=len(df[df['Sentiment'] == 'neutral'])
        if max(positive,negative,neutral)==positive:
          result="Positive"
        elif max(positive,negative,neutral)==negative:
          result="Negative"
        else:
          result="Neutral"
        L1=Label(rt,text="Mostly "+result,fg="grey",font=("Impact 20")).pack()
        labels = ['Positive ['+str((positive*100)/len(tweets))+'%]' , 'Neutral ['+str((neutral*100)/len(tweets))+'%]','Negative ['+str((negative*100)/len(tweets))+'%]']
        sizes = [positive, neutral, negative]
        patches, texts = plt.pie(sizes, startangle=90)
        plt.style.use('default')
        plt.legend(labels)
        plt.title('Sentiment Analysis of {}:'.format(search))
        plt.axis('equal')
        plt.show()
         
    s=int(e.get())
    if(s==1):
     '''For getting tweets based on a hashtag or keyword'''
     ad=Toplevel(root)
     ad.title("Sentiment Analysis")
     ad.configure(background="floral white")
     ad.geometry('440x300+400+200')
     l1=Label(ad,text="Sentiment Analysis of a keyword",font = ("Impact 15")).pack(side=TOP)
     l2=Label(ad,text="Enter a keyword to get tweets about",font = ("Impact 10")).pack(pady=60)
     e1=Entry(ad)
     e1.pack(side=TOP)
     b1=Button(ad,text="Submit",command=lambda: get_tweets_for_analysis(s,e1.get()),font = ("Impact 8"),bg="cornsilk3").pack()   
    
    else:
     ud=Toplevel(root)
     ud.title("Sentiment Analysis")
     ud.configure(background="floral white")
     ud.geometry('440x300+400+200')
     u1=Label(ud,text="Sentiment Analysis of a user's tweets",font = ("Impact 15")).pack(side=TOP)
     l2=Label(ud,text="Enter a username to get tweets about",font = ("Impact 10")).pack(pady=60)
     e2=Entry(ud)
     e2.pack(side=TOP) 
     b1=Button(ud,text="Submit",command=lambda: get_tweets_for_analysis(s,e2.get()),font = ("Impact 8"),bg="cornsilk3").pack()   
     
b=Button(root,text="Submit",font = ("Impact 8"),bg="cornsilk3",command=click).place(x=300,y=180)

root.mainloop()
