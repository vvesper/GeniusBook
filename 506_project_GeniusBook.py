#SI 506 Final Project 
#"GeniusBook"
#Vanessa Rychlinski
#Dec. 2016

import requests 
import json 
import webbrowser
import string
import unittest

#Classes and functions 

#Facebook Post Class goes here

class FBPost():
    

    def __init__(self, post_dict={}): #FB post obj with .message and .comments attributes
        if 'message' in post_dict:
            self.message = post_dict['message']
        else:
            self.message = ''
        if 'comments' in post_dict:
            for commenter in post_dict['comments']['data']:
                self.comments = commenter["message"]
        else:
            self.comments = ''
        if 'name' in post_dict:
            self.name = post_dict['name']
        else:
            self.name = ''
         # use variables in 2 other methods 

    def word_lst(self): 
        word_list= []   # call 
        for word in self.message.split():
            if word in word_list:
				word_list.append(word)
            else:
                word_list.append(word)
        return word_list 

    def rmv(self):  
    	remove = ["he", "she", "they", "them", "they", "their", "theirs", "it", "the", "an", "a", "in", "and", "or", 'but', "what", "who", "with", "I", "than", "that", "are", "which", "this", "though" , "so"]
    	clean_list = []
        badchars = string.digits + string.punctuation
        for i in self.word_lst():
            if i not in remove:
                clean_list.append(i)
        clean_list_final = []
        for item in clean_list:
            item_lst = []
            bad_lst = []
            badchars = string.digits + string.punctuation
            for char in badchars:
                bad_lst.append(char)
            for ch in item:
                item_lst.append(ch)
                keepitem = [i for i in item_lst if i not in bad_lst]
            finalitem = ''.join(keepitem)
            clean_list_final.append(finalitem)
        return clean_list_final
		#call class, then call this particular method to get the word dictionary


fb_access_token = "EAACEdEose0cBAPr0o4wii1Xn07a0TM9pbXZCTwZC9QFmlGllqqEpJobr15lhdIKLs3P3U7SvQUfTWigtgPPbVhykBEvd7U9jxObV0cebMiZAnIZBLeSKm4kwZABqFa98UZA7OXCT0KOhNdwZC9P0Cj69vRfYIGtt4ApMK438NWdFAZDZD"

baseurl = "https://graph.facebook.com/v2.3/me?fields=feed" 

url_params = {}
url_params["access_token"] = fb_access_token
url_params["fields"] = "feed" 
url_params['limit'] = 2

#create cache

try:
    fileref = open("facebook_wall_cache.txt").read() #.read turns it into a string 
    fb_wall_data = json.loads(fileref) #.loads creates dictionary from string
    #print fb_wall_data
    print "Getting cache data..."
except: 
    #if file doesnt exist 
    fb_requests = requests.get(baseurl, params= url_params)
    if fb_requests.status_code != 200:
        fb_access_token = raw_input("Please enter the access token for your Facebook feed at the Facebook Graph Explorer - https://developers.facebook.com/tools/explorer. Be sure the version is set to 2.3 and that the fields key is followed by 'feed'. Select user_posts on the permissions menu.")
    fb_wall_data = json.loads(fb_requests.text)
    print "Making a request to Facebook..."

    f = open('facebook_wall_cache.txt', 'w')
    f.write(json.dumps(fb_wall_data))
    f.close()


post_insts = [FBPost(p) for p in fb_wall_data['feed']['data']] #create a list of instances

#print type(post_insts)

#post_ints is list
def create_word_lst(posts):  
    words = []
    for post in posts:
        FBPost.word_lst(post)
        for item in FBPost.rmv(post):
            words.append(item)
    return words
# print final_word_list

 
word_list = create_word_lst(post_insts)

def nonrepeat(L):
    final = []
    for i in L:
        i = i.lower()
        if i not in final:
            final.append(i)
    return final

#print final_word_list

final_word_list = nonrepeat(word_list)

final_word_list_sorted = sorted(final_word_list, key = len, reverse = True)
top_25_words = final_word_list_sorted[:26]

# print "The Top 25 words are " , top_25_words

class GeniusHit():  #

    def __init__(self, querydict= {}):  
        self.title = querydict['result']['full_title']
        self.url = querydict['result']['url']
        self.title = querydict['type']
        self.img = querydict['result']['header_image_url']
    # def read_lyrics(self):
    #     webbrowser.open(self.url)

    def song_img(self):
        if self.title == "song":
            return self.img

    def __str__(self):
        return ('Your song for this keyword is {}!').format(self.title.encode('utf-8'))
        


def read_lyrics(url):
    webbrowser.open(url)

client_id = 'L2H-rsSHESwx6hxidYkCZWsqKXA9v2HBmcycGDEMnQkc8_cuUplkwrG7IIXyxSWj'
client_secret = 'CPkbZxuodrRYt5Rs_1NPKl9i3dqv1qx74pLTDyyNBVIeV2Nu8w6lAA-xT5Q5UriZFhntjMU-WEjI2DZpdy0iwQ'
client_access_token = 'DVV3XVcbqqBJd_deyktnWMdF6vfKeyFVPuAhc33cAuMCLu1mIxGdQIpP0E5msa33'  #how it goes into url -->  http://api.genius.com/search?q=surfin&access_token=hXPnD2cD1zUzwwFPKD5SiV9-A78sPA_HusvG9Xse7YmQIC77BhgFToZz-wK9m8DH


BASE_URL = "http://api.genius.com/search"
ACCESS_TOKEN = client_access_token


try:
    f = open("genius_cache.txt").read() #use the cache first 
    ff = f.encode('utf-8') #encoding to put make string normal not in unicode ? 
    #print type(ff)
    genius_dict = json.loads(ff)
    ff.close()

except:
    genius_dict = {}
    url_dict = {} 
    str_dict = {}
    img_dict = {}
    for search_term in top_25_words:

        if search_term not in genius_dict.keys():
            response = requests.get(BASE_URL, params= {'q': search_term, "access_token" : ACCESS_TOKEN, 'per_page' : 10, "page" : 1})
            
            query_data = json.loads(response.text)
            
            f = open("genius_cache.txt", "w")
            f.write(json.dumps(query_data))
            f.close()

            for hit in query_data['response']['hits']:
                search_inst = GeniusHit(hit)
                
                genius_dict[search_term] = search_inst.title
                url_dict[search_term] = search_inst.url
                str_dict[search_term] = search_inst.__str__
                img_dict[search_term] = search_inst.song_img()
        else:
            pass
        f = open("genius_cache.txt", "w")
        f.write(json.dumps(query_data))
        f.close()  
    
#print genius_dict
#print type(genius_dict)


file = open("lyric_profile.csv", "w")
file.write('Facebook Keyword Song, Artist\n')
for k,v in genius_dict.items():
    file.write('"{}","{}"\n'.format(k,v.encode("utf-8")))
file.close()

ss = raw_input("Would you like to see the songs associated with your Facebook words? Please enter y or n. ")

while ss == 'y':
    print top_25_words
    s = raw_input("Pick one of your Facebook words. ") 
    print "For the Facebook word " + s + "..."
    s_str = str_dict[s]
    lyric_url = url_dict[s]
    read_lyrics(lyric_url)
    ss = raw_input("Would you like to choose another word? Enter y or n. ")

aa = raw_input("Would you like to view some cover art? Enter y or n. ")

while aa == "y" :
    print top_25_words
    b = raw_input("Pick one of your Facebook words. ") 
    print "For the Facebook word " + b + "..."
    s_str = str_dict[b]
    lyric_url = img_dict[b]
    read_lyrics(lyric_url)
    aa = raw_input("Would you like to choose another word? Enter y or n. ")

print "OK! I hope you enjoyed your GeniusBook experience. Bye!"



#UNITTESTS 
class Myunittests(unittest.TestCase):

    def test1(self):
        self.assertTrue(type(word_list) == "<type 'list'>" )
    def test2(self):
        self.assertEqual(top_25_words[2], u'superhighway' )
    def test3(self):
        self.assertTrue(type(genius_dict) == "<type 'dict'>")
    def test4(self):
        self.assertTrue(len(top_25_words) == 25)
    def test5(self):
        self.assertTrue(len(img_dict.keys())== 25)
    def test6(self):
        self.assertEqual(top_25_words[2:8], [u'superhighway', u'commercially', u'preservation', u'unidentified', u'information', u'yellowstone'])
    def test7(self):
        self.assertFalse(top_25_words[7], u"Yellowstone", "Checking that capitalized words were changed to lowercase")
    def test8(self):
        self.assertEqual(url_dict['emblazoned'], 'http://genius.com/Beowulf-chapter-22-beowulf-seeks-grendels-mother-annotated')



