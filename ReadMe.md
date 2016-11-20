
Demo
----

Text Three Words
![screen shot 2016-11-20 at 6 49 10 pm](https://cloud.githubusercontent.com/assets/121151/20467255/1785a13c-af52-11e6-8275-b92d0f41a148.png)

The corresponding address and photo are sent via MMS
![screen shot 2016-11-20 at 6 50 13 pm](https://cloud.githubusercontent.com/assets/121151/20467268/52121cc2-af52-11e6-9751-25028592f4e4.png)


Currently, the only two supported locations are:
 * encounter.inhaled.mime (Dan Dye's house)
 * encounter.prelude.cube (Patterson St. Park)

Pre-requisites
--------------
 - [Install the Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)


```
[107]dandye@Huginn:~/Projects/TreasureTampa$ conda env create --name TreasureTampa
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
# > source activate TreasureTampa
#
# To deactivate this environment, use:
# > source deactivate TreasureTampa
#
```

Conda venv env vars
-------------------

[Conda Saved Environment Variables](http://conda.pydata.org/docs/using/envs.html#saved-environment-variables)

```
(TreasureTampa) [204]dandye@Huginn:~/Projects/TreasureTampa$ mkdir -p ~/anaconda/envs/TreasureTampa/etc/conda/activate.d
(TreasureTampa) [205]dandye@Huginn:~/Projects/TreasureTampa$ mkdir -p ~/anaconda/envs/TreasureTampa/etc/conda/deactivate.d
(TreasureTampa) [206]dandye@Huginn:~/Projects/TreasureTampa$ touch ~/anaconda/envs/TreasureTampa/etc/conda/activate.d/env_vars.sh
(TreasureTampa) [207]dandye@Huginn:~/Projects/TreasureTampa$ touch ~/anaconda/envs/TreasureTampa/etc/conda/deactivate.d/env_vars.sh
```

Deploy to Heroku
----------------
```
(TreasureTampa) [182]dandye@Huginn:~/Projects/TreasureTampa$ pip freeze > requirements.txt
(TreasureTampa) [186]dandye@Huginn:~/Projects/TreasureTampa$ heroku buildpacks:set heroku/python
Buildpack set. Next release on peaceful-meadow-37904 will use heroku/python.
Run git push heroku master to create a new release using this buildpack.
(TreasureTampa) [188]dandye@Huginn:~/Projects/TreasureTampa$ git add .
(TreasureTampa) [189]dandye@Huginn:~/Projects/TreasureTampa$ git commit -m "heroku setup"
(TreasureTampa) [190]dandye@Huginn:~/Projects/TreasureTampa$ git push heroku master
(TreasureTampa) [191]dandye@Huginn:~/Projects/TreasureTampa$ heroku ps:scale web=1
```

Tail Heroku
-----------
```
(TreasureTampa) [192]dandye@Huginn:~/Projects/TreasureTampa$ heroku logs --tail
```
