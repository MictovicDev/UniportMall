def validateemail(email):
    for x in email:
        if type(x) == int:
            return False
        ans = email.split('.')
        second = ans.pop()
    for x in ans:
        for i in x:
            if i == '@':
                if second == 'com':
                    return True

    return False