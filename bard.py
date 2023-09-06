from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID":"aQjhEASJPXap2Pc7PIdmHRoRzjew10pcD0F4mBsbt1eSuFwbxkiuN2m-y1Ypq2TFsC-EGg.",
    "__Secure-1PSIDTS":"sidts-CjIBSAxbGd2lm0p_HOuIt0JQrP43qRxej21RnUddQpeyw7g_ZIDvnRe_fmrvFEprFFnBaxAA",
    "__Secure-1PSIDCC":"APoG2W_HQIxqwMuBc4QhVfmD4KBNXZlF5OeBUdg1TRCqCUzIgou2xhInVTn4upJ0bk3SDgmgIQ"
}

bard = BardCookies(cookie_dict=cookie_dict)

while True:
    query = input("Enter your query:")
    Reply = bard.get_answer(query)['content']
    print(Reply)