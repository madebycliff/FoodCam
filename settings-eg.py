import RPi.GPIO as GPIO
slackUrl='https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXX'
slackTestUrl='https://hooks.slack.com/services/XXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXX'
mailgunUrl='https://api.mailgun.net/v3/sandboxa5b983d793f545d484633162c581bf61.mailgun.org/messages'
mailgunTestUrl='https://api.mailgun.net/v3/sandboxa5b983d793f545d484633162c581bf61.mailgun.org/messages'
mailgunUser='api:979b65fbe1b9f4da9a749f8582aa1d58-afab6073-660077d5'
mailgunSender='foodcam@sandboxa5b983d793f545d484633162c581bf61.mailgun.org'
copiaUrl='https://copia.food.cloud'
copiaTestUrl='https://copia-c.food.cloud'

location='the kitchen'
recipient='FoodCloud'
on=GPIO.HIGH
off=GPIO.LOW

button=4

blue=17
red=21
amber=22
green=23

leds_pin=18

bakery=1
grocery=2
pantry=3
chilled=11
non_food=5

bakery_led=6
grocery_led=7
pantry_led=8
chilled_led=9
non_food_led=10

weight_data=5
weight_clock=6

max_quantity=2# 2 means food or no food, 10 means 0-9 trays etc
