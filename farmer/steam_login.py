import steam.webauth as wa
import json

class SteamLogin:
    def __init__(self, config):
        self.account_name = config["ACCOUNT_NAME"]
        self.password = config["PASSWORD"]
        self.shared_secret = config.get("SHARED_SECRET", None)
        self.session = None

    def login(self):
        user = wa.WebAuth(self.account_name, self.password, self.shared_secret)
        try:
            self.session = user.login()
            print("Logged in successfully")
        except wa.CaptchaRequired:
            print("Captcha required, please try logging in manually.")
        except wa.EmailCodeRequired:
            print("Email code required, please check your inbox.")
        except wa.TwoFactorCodeRequired:
            print("2FA code required, please check your authenticator app.")
        except wa.LoginIncorrect:
            print("Incorrect login details.")

    def get_session(self):
        return self.session
