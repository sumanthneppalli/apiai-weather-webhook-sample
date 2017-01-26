#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") != "yahooWeatherForecast":
        return {}
    baseurl = "https://www.tastekid.com/api/similar?q=humsafar&k=257475-MovieRec-2525O9YA"
    result = urllib.urlopen(baseurl).read()
    data = json.loads(result)
    res = makeWebhookResult(data)
    return res


def makeWebhookResult(data):
    query = data.get('similar')
    if query is None:
        return {}

    query1 = query.get('info')
    if query1 is None:
        return {}

    result = query1.get('name')
    if result is None:
        return {}
  

    # print(json.dumps(item, indent=4))

    speech = what

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')
