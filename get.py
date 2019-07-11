from multiprocessing import Pool
import requests
import json
import time

url = "https://my.smart.com.ph/paybills/authenticationform.aspx"

def f(i):
    headers = {
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "5b2e3c04-9e8f-47bf-8d78-802487aa316b,f95b90b8-6db0-455b-bbae-c160465b0ba7",
        'Cookie': "NSC_Q_MC_TNBSU.DPN.QI_SPPU=ffffffff09a2efd845525d5f4f58455e445a4a423660; visid_incap_1981217=Q4sagO2YQS2goBxGotCx/kgKJ10AAAAAQUIPAAAAAACeLtws17KHw5xOcGKCAyqB; incap_ses_1185_1981217=32Q6LqHsbnjebAeRYQJyEEgKJ10AAAAAPV1nOFgXSFWq3yS0/yN9pQ==; incap_ses_224_1981217=bTP/OnpX7ApjqtiHmNAbA1sKJ10AAAAAlY8v79fBXTBzs9bFP8M4Xg==",
        'Accept-Encoding': "gzip, deflate",
        'Referer': "https://smart.com.ph/corporate/message/error.html",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

    return response


def main():
    p = Pool(4)
    return p.map(f, range(20))


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
