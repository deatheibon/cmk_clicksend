# cmk_clicksend
Check_MK SMS Notification via clicksend 

## USAGE

- Copy the script to /opt/omd/sites/"your site"/local/share/check_mk/notifications/clicksend
- In wato go to notification and create new rule for sms notifications 
- in "Notification Method" section choose "clicksend" from drop down list
- call with follwing parameters: username, api key, from (optonal)
