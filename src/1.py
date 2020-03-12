def extract_domain(url, remove_http=True):
    uri = urlparse(url)
    if remove_http:
        domain_name = f"{uri.netloc}"
    else:
        domain_name = f"{uri.netloc}://{uri.netloc}"
    return domain_name
url = 'https://pydeep.com/get-domain-name-from-url-python'
print("Original: ", url)
print("Extracted: ", extract_domain(url))