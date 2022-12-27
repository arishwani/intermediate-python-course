import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
}
req = requests.get(url, headers=headers)

print(req.status_code)

res = req.json()

submission_dicts = []
for submission_id in res[:30]:
    #make API calls for each submission

    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')

    submission_res = requests.get(url)
    #print("The status code for the submission is ", submission_res.status_code)
    response_dict = submission_res.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id), 
        'comments': response_dict.get('descendants', 0)

    }
    submission_dicts.append(submission_dict)
#submission_dicts = sorted(submission_dicts,  key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print('\nTitle: ', submission_dict['title'])
    print('Discussion Link: ', submission_dict['link'])
    print('Comments:', submission_dict['comments'])
