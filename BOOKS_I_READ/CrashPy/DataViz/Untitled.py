from operator import itemgetter
import requests

# make an API call and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code : {r.status_code}")

# process information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # make a separate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    repsonse_dict = r.json()

    # build a dictionary for each article
    submission_dict = {
                'title': repsonse_dict['title'],
                'hn_linl': f"https://news.ycombinator.com/item?id={submission_id}",
                'comment': repsonse_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key = itemgetter('comments'),reverse = True)

for submission_dict in submission_dicts:
    print(f"\nTitle : {submission_dict['title']}")
    print(f"Discussion link : {submission_dict['hn_linl']}")
    print(f"Comments: {submission_dict['comments']}")
