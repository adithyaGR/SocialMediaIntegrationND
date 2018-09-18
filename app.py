import os
from flask import Flask, render_template, jsonify, request
import urllib2
from twitter import *

app = Flask(__name__)

@app.route("/")
def home():
    # db = getattr(g, 'hashtag', None)
    entries = []
    #, entries=entries 
    return render_template('home.html')
    
@app.route('/twitter')
def twitter():
    hashtag = request.args.get('hashtag', 0, type=str)
    #api code here
    access_token = ''
    access_token_secret = ''
    consumer_key = ''
    consumer_secret = ''
    # hashtag = '#' + hashtag
    twitter = Twitter(auth=OAuth(access_token, access_token_secret,consumer_key,consumer_secret))
    results = twitter.search.tweets(q=hashtag, count=30)
    
    return jsonify(result=results.get('statuses'))
  
@app.route('/facebook')
def facebook():
    #api code here
    page_id = request.args.get('link', 0, type=str)
    app_id = ""
    app_secret = ""
    get_auth_token = 'https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id='+app_id+'&client_secret='+app_secret
    authToken = urllib2.urlopen(get_auth_token).read()
    feed_url = "https://graph.facebook.com/"+page_id+"/feed?"+authToken
    page_feed = urllib2.urlopen(feed_url).read()
    #print page_feed
    
    return jsonify(result=page_feed)
    

app.run(debug=True,host=os.getenv("IP", "0.0.0.0"),port=int(os.getenv("PORT", 8080)))

#http://socialmedia-arathakr.c9users.io/
