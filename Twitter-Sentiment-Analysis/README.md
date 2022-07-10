# Twitter-sentiment-analysis

The main objective of this project is to analyze sentiment of tweets .In this project ,user has two options for getting tweets , either he can enter a keyword to get tweets about or he can enter a username of twitter user  to get his tweets . User will collect  200 tweets from twitter using Tweepy API and will analyze them into positive, negative ,neutral using TextBlob API by using Natural Language Processing(NLP). Note: Use your own tweepy credentials for API authorization.

- The main objective of this project is to analyze sentiment of tweets.
- User will collect 200 tweets from twitter using Tweepy API and will analyze them into positive, negative ,neutral using TextBlob API by using Natural Language Processing(NLP).
- user has two options for getting tweets, either he can enter a keyword to get tweets about or he can enter a username of twitter user to get his tweets .

## Prerequisite

* [Tweepy](http://www.tweepy.org), the official Python library for accessing the Twitter API
* [TextBlob](https://textblob.readthedocs.io/en/dev/), a Python library for processing textual data
* Twitter `API_key` and `API_secret_key` is required to execute this python program (API keys can be retrieved from [Twitter Developer Application Management](https://developer.twitter.com/) site
  - bearer_token
  - Api_key
  - Api_key_secret
  - Access token
  - Access token secret

## Project View


## Installation

Download or Clone the repo, Navigate to the directory containing the files and run
```
python setup.py install
```
or if you have different versions of python installed then
```
python3 setup.py install 
```
to install the dependencies.
The **Tweepy** library can be installed by using the command
```
pip3 install tweepy
```  
</br>

The **TextBlob** library can be installed using
```
pip3 install textblob
```  
</br>

The **numpy** library can be installed using
```
pip3 install numpy
```  
</br>

The **pandas** library can be installed using
```
pip3 install pandas
```  
</br>

To obtain the **api keys** and **access tokens** from the Twitter Dev Application Management site, a new app needs to be created using a Twitter account.

* Open [apps.twitter.com](https://apps.twitter.com/) and use the `Create New App` button.
* Complete the form with the necessary application details. The application name must be unique.
* Navitgate to the `Keys and Access Tokens` tab.
* Copy `api Key`, `api key Secret`, `Access Token`, `bearer Token` and `Access Token Secret` and update the variables `api Key`, `api key Secret`, `Access Token`, `bearer Token` and `Access Token Secret` in the `twitter_credentials.py` file accordingly.

</br>


## Usage

Once you have created an app on twitter and installed all the dependencies and open twitter_credentials.py and paste your api Key, api Secret key, Access Token and Access Token Secret. After that save and run the script. You will be prompted to enter the keyword/hashtag you want to analyze and the number of tweets you want to analyze. Once the analysis is completed, a pie chart will be generated disclosing the results of analysis.

## Built With

* Python 3.8.10
* tweepy
* textblob
* matplotlib
* numpy
* pandas

## Contributing

1. Fork it
2. Create your feature branch: git checkout -b my-new-feature
3. Commit your changes: git commit -am 'Add some feature'
4. Push to the branch: git push origin my-new-feature
5. Submit a pull request


## 🚀 Technologies

* [Python](https://www.python.org/downloads/release/python-3810/)
* [Tweepy](http://www.tweepy.org)
* [TextBlob](https://textblob.readthedocs.io/en/dev/)
* [Twitter](https://apps.twitter.com/)
* [Twitter Developer Application Management](https://developer.twitter.com/)

## 🤝 Contribute

To contribute, fork the repository and push the changes to the **master** branch. Then submit a pull request for merging with the source. If your code passes the review and checks it will be merged into the master branch.

## 💬 Feedback

Feel free to send us feedback on gmail => "jatinkesharwani360@gmail.com"  or [file an issue](https://github.com/jatinkesharwani/Twitter-Sentiment-Analysis/issues). Feature requests are always welcome.

