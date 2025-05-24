def extract_region(locale_code):
    if len(locale_code) > 4:
        return locale_code[3:5]
    else:
        return "That wasn't nearly long enough to be a locale code. Get it right next time"
#highlight    
print(extract_region('en_US.UTF-8'))      # US
print(extract_region('en_GB.UTF-8'))      # GB
print(extract_region('ko_KR.UTF-16'))     # KR
print(extract_region('e'))                #That wasn't nearly long enough to be a locale code. Get it right next time
print(extract_region('fr'))               #fr
#endhighlight
