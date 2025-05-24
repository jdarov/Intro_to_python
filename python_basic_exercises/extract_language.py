def extract_language(locale_code):
    if len(locale_code) > 1:
        return locale_code[0:2]
    else:
        return "That wasn't nearly long enough to be a local code. Get it right next time"
    
print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko
print(extract_language('e'))                #That wasn't nearly long enough to be a local code. Get it right next time
print(extract_language('fr'))               #fr