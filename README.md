# Voter Information Scraper

This python project aims to extract voter information from web site (https://electoralsearch.in/) by filling some basic details of voter and captcha code.


## Requirements

 - To run this project you need to have python environment setup on your
   system
 - I've attached requirements.txt which contains libraries required to
   use this script. Run following command for installing libraries:
   >***pip install -r requirements.txt***
  -  You also need appropriate web driver based on your browser that you can download by googling it.
- If required you need to change code if using other than chrome browser, in this script I've used chrome driver (version. 70-72).

>It is developed with **Python 3.7** using **selenium** and **open-ocr api** for captcha text extraction, so for captcha correction you might need to run this multiple times.

## How to run?

After setting up environment, you just need to type following command in your command prompt/terminal to use this script:
> ***python webscrapper.py***

## Where to find extracted information?

After running above command you'll get **Voter.csv** file at your script location which will contain all the information of your voter.

#### NOTE:

>For extracting each voter information, as of now you need to call this script every time and also need to fill required information in code itself!
>Make sure you are not overwriting your existing voter information, as running second time will replace previous **Voter.csv** file.








