import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from flask_smorest import abort


class Verify:
    def __init__(self):
        self.client = Client(
            "TWILIO_SID", "TWILIO_AUTH_TOKEN"
        )
        # self.sid = self.client.verify.v2.services.create(
        #     friendly_name="ClassyCommerce authorize login"
        # ).sid
        self.sid = "VA76c092f0d625010e2653bb889c27e94a"
        print(self.sid)

    # def createNewAuthService(self):
    #     service = self.client.verify.services.create(
    #                                  friendly_name='ClassyCommerce authorize login'
    #                              )
    #     return(service.sid)

    def sendOtp(self, moNo):
        try:
            verification = self.client.verify.v2.services(self.sid).verifications.create(
                to=moNo, channel="sms"
            )
            # print(verification.__dict__)
            return verification.status
        except TwilioRestException as e:
            print(e.__str__(),"hello")
            raise TwilioRestException(
                401, e
            )
            # raise TwilioRestException

    def verifyOtp(self, moNo, code):
        try:
            verification_check = self.client.verify.services(
                self.sid
            ).verification_checks.create(to=moNo, code=code)
            return verification_check.status
        except TwilioRestException as e:
            raise TwilioRestException(
                401, e
            )
