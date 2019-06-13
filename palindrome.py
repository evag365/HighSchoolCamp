def removing(check):
    check = check.lower().replace("  ", "").replace(" ,", "").replace(" !", "").replace(" .", "").replace(" '", "").replace(" :", "")
    return check
    print(removing("Madam, I'm Adam"))
    clear = removing("Madam, I'm Adam")
    print(clear)


def palindrome (check):
    check= removing(check)
    return check == check[::-1]

print(palindrome("MadamImAdam"))
print(palindrome("computer"))