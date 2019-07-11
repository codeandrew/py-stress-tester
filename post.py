from multiprocessing import Pool
import requests
import json
import time

url = "http://ghost-dev.whitecloak.io/api/forum/questions"

def f(i):
    payload = {
      "title": "Lorem Ipsum a%d"  % i,
      "content": "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit... c%d" % i,
      "author": {
        "user_id": "5d16f219169b230001af94be",
        "pet_id": "null"
      },
      "tags": [
        "stressTest"
      ]
    }

    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7Il9pZCI6IjVkMTZmMjE5MTY5YjIzMDAwMWFmOTRiZSIsImVtYWlsIjoiNWQxNmYyMTkxNjliMjMwMDAxYWY5NGJlIiwiZmlyc3RfbmFtZSI6IlR5bGVyIiwibGFzdF9uYW1lIjoiWmFtb3Jlc2VuIiwiZGlzcGxheV9uYW1lIjoiVHlsZXIgWmFtb3Jlc2VuIiwiYWRkcmVzcyI6bnVsbCwiYmlydGhfZGF0ZSI6IiIsImFib3V0IjpudWxsLCJwcm9maWxlX3BpY3R1cmUiOm51bGwsInByb2ZpbGVfdmlldyI6MCwicXVlc3Rpb25fY291bnQiOjEsImFuc3dlcl9jb3VudCI6MSwiYm9vcF9jb3VudCI6NCwiY3JlYXRlZF9hdCI6IjA2LzI5LzIwMTkgMTM6MDc6MzciLCJiYWRnZSI6eyJfaWQiOm51bGwsInN0YXR1cyI6IiIsImltYWdlX3VybCI6IiIsImJhZGdlX3R5cGUiOiIifSwidXNlcl90eXBlIjoiVVNFUiJ9LCJ1c2VyX25hbWUiOiI1ZDE2ZjIxOTE2OWIyMzAwMDFhZjk0YmUiLCJzY29wZSI6WyJyZWFkIiwid3JpdGUiLCJ0cnVzdCJdLCJleHAiOjE1NjIzOTg1NTQsImF1dGhvcml0aWVzIjpbIlVTRVIiXSwianRpIjoiZDgzNDZmYzQtMGRhZi00MjZlLWJkMWQtNzY4MWFjZDViYmFjIiwiY2xpZW50X2lkIjoiN2I0ZTFhYmEtYmE1Zi00ZDMyLTkyNzEtYzgzMTZjMmMzOGI5In0.4-KbWYU70SAXvXlacd1ogcIO3cxtnV_fvgO9So0ZLHE",
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "a7900f02-4c1b-41aa-af68-e731a65235ac,d9627630-4c8a-44d1-8005-c595d36a2a0e",
        'Host': "ghost-dev.whitecloak.io",
        'accept-encoding': "gzip, deflate",
        'content-length': "254",
        'referer': "http://ghost-dev.whitecloak.io/api/forum/questions",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    print(response.text)

    return response


def main():
    p = Pool(16)
    return p.map(f, range(100))


if __name__ == '__main__':
    start_time = time.time()
    result = str(main())
    print("--- %s seconds ---" % (time.time() - start_time))

    success = result.count("20")
    server = result.count("50")
    error = result.count("40")

    print("success: ",success)
    print("server errors: ", server)
    print("client errors: ", error )
