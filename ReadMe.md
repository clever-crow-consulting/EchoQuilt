
Demo
----

Text Three Words

![screen shot 2016-11-20 at 6 49 10 pm](https://cloud.githubusercontent.com/assets/121151/20467255/1785a13c-af52-11e6-8275-b92d0f41a148.png)

The corresponding address and photo are sent via MMS
![screen shot 2016-11-20 at 6 50 13 pm](https://cloud.githubusercontent.com/assets/121151/20467268/52121cc2-af52-11e6-9751-25028592f4e4.png)


Currently, the only two supported locations are:
 * encounter.inhaled.mime (Dan Dye's house)
 * encounter.prelude.cube (Patterson St. Park)


Spoken command: "Text my location to Alice Roberts" (I have the Twilio phone number saved under that code name)

The app returns The.Three.Words for that location:

![screen shot 2016-12-06 at 7 09 39 pm](https://cloud.githubusercontent.com/assets/121151/20949507/ada73fc6-bbe7-11e6-9317-faf7ba692632.png)

This currently relies on the text in the msg being *exactly*:
```
I'm here:
https://maps.google.com/maps?q=[lat],[lon]
```

The heroku log for that command:
```
2016-12-06T23:59:22.123801+00:00 app[web.1]: sms_body: I'm here:
2016-12-06T23:59:22.123803+00:00 app[web.1]: https://maps.google.com/maps?q=28.017378,-82.450272
2016-12-06T23:59:22.123805+00:00 app[web.1]: 
2016-12-06T23:59:22.123808+00:00 app[web.1]: Entering latlon2wtw...
2016-12-06T23:59:22.123869+00:00 app[web.1]: lat: 28.017378, lon: -82.450272
2016-12-06T23:59:22.124473+00:00 app[web.1]: <httplib.HTTPSConnection instance at 0x7f21a8186878>
2016-12-06T23:59:22.124482+00:00 app[web.1]: request_url: https://api.what3words.com/v2/reverse?coords=28.017378%2C-82.450272&key=[redacted]&lang=en&format=json&display=full
2016-12-06T23:59:22.738776+00:00 app[web.1]: data_str: {"crs":{"type":"link","properties":{"href":"http:\/\/spatialreference.org\/ref\/epsg\/4326\/ogcwkt\/","type":"ogcwkt"}},"words":"drill.bronzer.outdoors","bounds":{"southwest":{"lng":-82.450299,"lat":28.017357},"northeast":{"lng":-82.450269,"lat":28.017384}},"geometry":{"lng":-82.450284,"lat":28.01737},"language":"en","map":"http:\/\/w3w.co\/drill.bronzer.outdoors","status":{"status":200,"reason":"OK"},"thanks":"Thanks from all of us at index.home.raft for using a what3words API"}
2016-12-06T23:59:22.739009+00:00 app[web.1]: {u'thanks': u'Thanks from all of us at index.home.raft for using a what3words API', u'language': u'en', u'geometry': {u'lat': 28.01737, u'lng': -82.450284}, u'crs': {u'properties': {u'href': u'http://spatialreference.org/ref/epsg/4326/ogcwkt/', u'type': u'ogcwkt'}, u'type': u'link'}, u'status': {u'reason': u'OK', u'status': 200}, u'bounds': {u'northeast': {u'lat': 28.017384, u'lng': -82.450269}, u'southwest': {u'lat': 28.017357, u'lng': -82.450299}}, u'map': u'http://w3w.co/drill.bronzer.outdoors', u'words': u'drill.bronzer.outdoors'}
2016-12-06T23:59:22.739026+00:00 app[web.1]: [u'thanks', u'language', u'geometry', u'crs', u'status', u'bounds', u'map', u'words']
2016-12-06T23:59:22.739190+00:00 app[web.1]: Words: drill.bronzer.outdoors
2016-12-06T23:59:22.739764+00:00 app[web.1]: 10.150.160.72 - - [06/Dec/2016 23:59:22] "POST / HTTP/1.1" 200 -
2016-12-06T23:59:22.735775+00:00 heroku[router]: at=info method=POST path="/" host=peaceful-meadow-37904.herokuapp.com request_id=[redacted] fwd="[ip address]" dyno=web.1 connect=1ms service=633ms status=200 bytes=270
```



Pre-requisites
--------------
 - [Install the Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)


```
[107]dandye@Huginn:~/Projects/EchoQuilt$ conda env create --name EchoQuilt
Using Anaconda API: https://api.anaconda.org
Fetching package metadata .......
Solving package specifications: ..........
Fetching packages ...
pip-9.0.1-py27 100% |#######################################################################################| Time: 0:00:00   4.35 MB/s
Extracting packages ...
[      COMPLETE      ]|##########################################################################################################| 100%
Linking packages ...
[      COMPLETE      ]|##########################################################################################################| 100%
Collecting twilio>=3.3.6
  Downloading twilio-5.6.0.tar.gz (194kB)
    100% |████████████████████████████████| 194kB 1.5MB/s
Collecting httplib2>=0.7 (from twilio>=3.3.6)
  Downloading httplib2-0.9.2.zip (210kB)
    100% |████████████████████████████████| 215kB 1.4MB/s
Collecting six (from twilio>=3.3.6)
  Downloading six-1.10.0-py2.py3-none-any.whl
Collecting pytz (from twilio>=3.3.6)
  Downloading pytz-2016.7-py2.py3-none-any.whl (480kB)
    100% |████████████████████████████████| 481kB 1.3MB/s
Building wheels for collected packages: twilio, httplib2
  Running setup.py bdist_wheel for twilio ... done
  Stored in directory: /Users/dandye/Library/Caches/pip/wheels/a2/26/f3/df907c29456ce320e66583c50ddd521296b906d92d5b807b92
  Running setup.py bdist_wheel for httplib2 ... done
  Stored in directory: /Users/dandye/Library/Caches/pip/wheels/c7/67/60/e0be8ccfc1e08f8ff1f50d99ea5378e204580ea77b0169fb55
Successfully built twilio httplib2
Installing collected packages: httplib2, six, pytz, twilio
Successfully installed httplib2-0.9.2 pytz-2016.7 six-1.10.0 twilio-5.6.0
#
# To activate this environment, use:
# > source activate EchoQuilt
#
# To deactivate this environment, use:
# > source deactivate EchoQuilt
#
```

Conda venv env vars
-------------------

[Conda Saved Environment Variables](http://conda.pydata.org/docs/using/envs.html#saved-environment-variables)

```
(EchoQuilt) [204]dandye@Huginn:~/Projects/EchoQuilt$ mkdir -p ~/anaconda/envs/EchoQuilt/etc/conda/activate.d
(EchoQuilt) [205]dandye@Huginn:~/Projects/EchoQuilt$ mkdir -p ~/anaconda/envs/EchoQuilt/etc/conda/deactivate.d
(EchoQuilt) [206]dandye@Huginn:~/Projects/EchoQuilt$ touch ~/anaconda/envs/EchoQuilt/etc/conda/activate.d/env_vars.sh
(EchoQuilt) [207]dandye@Huginn:~/Projects/EchoQuilt$ touch ~/anaconda/envs/EchoQuilt/etc/conda/deactivate.d/env_vars.sh
```

Deploy to Heroku
----------------
```
(EchoQuilt) [182]dandye@Huginn:~/Projects/EchoQuilt$ pip freeze > requirements.txt
(EchoQuilt) [186]dandye@Huginn:~/Projects/EchoQuilt$ heroku buildpacks:set heroku/python
Buildpack set. Next release on peaceful-meadow-37904 will use heroku/python.
Run git push heroku master to create a new release using this buildpack.
(EchoQuilt) [188]dandye@Huginn:~/Projects/EchoQuilt$ git add .
(EchoQuilt) [189]dandye@Huginn:~/Projects/EchoQuilt$ git commit -m "heroku setup"
(EchoQuilt) [190]dandye@Huginn:~/Projects/EchoQuilt$ git push heroku master
(EchoQuilt) [191]dandye@Huginn:~/Projects/EchoQuilt$ heroku ps:scale web=1
```

Tail Heroku
-----------
```
(EchoQuilt) [192]dandye@Huginn:~/Projects/EchoQuilt$ heroku logs --tail
`
Reconfigure Heroku
------------------

```
(EchoQuilt)[542]ddye@corax:EchoQuilt$ cat ~/anaconda/envs/EchoQuilt/etc/conda/activate.d/env_vars.sh
TWILIO_ACCOUNT_SID=ABC123...abc123
TWILIO_AUTH_TOKEN=abc123...abc123
DANDYE_GOOGLE_VOICE=+18135551234
TWILIO_PHONE_NUMBER=+18135551234
```

```
(EchoQuilt)[540]ddye@corax:EchoQuilt$ git remote add heroku git@heroku.com:peaceful-meadow-37904.git
```
