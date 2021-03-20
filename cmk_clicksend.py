#!/usr/bin/env python2

from __future__ import print_function
import os
import clicksend_client
from clicksend_client import SmsMessage
from clicksend_client.rest import ApiException

# Configure HTTP basic authorization: BasicAuth
configuration = clicksend_client.Configuration()
configuration.username = os.environ.get('NOTIFY_PARAMETER_1')
configuration.password = os.environ.get('NOTIFY_PARAMETER_2')

# create an instance of the API class
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))

# If you want to explictly set from, add the key _from to the message.

if os.environ.get('NOTIFY_CONTACTPAGER') != "":
    if os.environ.get('NOTIFY_WHAT') == "HOST":
        sms_message = SmsMessage(source="php",
                                 _from=os.environ.get('NOTIFY_PARAMETER_3'),
                                 body="""
                                    %s %s
                                    Message  : %s
                                    Address  : %s
                                    Date/Time: %s
                                    """ % (os.environ.get('NOTIFY_HOSTNAME'),
                                        os.environ.get('NOTIFY_HOSTSTATE'),
                                        os.environ.get('NOTIFY_HOSTOUTPUT'),
                                        os.environ.get('NOTIFY_HOSTADDRESS'),
                                        os.environ.get('NOTIFY_SHORTDATETIME')),
                              to=os.environ.get('NOTIFY_CONTACTPAGER'))
    else:
        sms_message = SmsMessage(source="php",
                                 _from=os.environ.get('NOTIFY_PARAMETER_3'),
                                 body="""
                                 %s %s
                                 Service  : %s
                                 Message  : %s
                                 Address  : %s
                                 Date/Time: %s
                                 """ % (os.environ.get('NOTIFY_HOSTNAME'),
                                        os.environ.get('NOTIFY_SERVICESTATE'),
                                        os.environ.get('NOTIFY_SERVICEDESC'),
                                        os.environ.get('NOTIFY_SERVICEOUTPUT'),
                                        os.environ.get('NOTIFY_HOSTADDRESS'),
                                        os.environ.get('NOTIFY_SHORTDATETIME')),
                               to=os.environ.get('NOTIFY_CONTACTPAGER'))

    print(sms_message)
    sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])

    try:
        # Send sms message(s)
        api_response = api_instance.sms_send_post(sms_messages)
        print(api_response)
    except ApiException as e:
        print("Exception when calling SMSApi->sms_send_post: %s\n" % e)
