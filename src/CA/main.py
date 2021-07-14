from src.CA.CA_model import CA

user_pub_key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCf3YpgBxziryN+i/qkhuEvvkxM
oRd4cGcLEiMFP4jhH4iBcH/r+zUwDkBC9UNqq0G5Kw4yRuwsSVIrGkwLZD/n8sTs
8G7XhvkLmYjuksFzSZNv5mHP23UeBih0jy2rmV3F5+U8Pne6ZlzUupxh9Qd4U+zn
IYgqoaPLY31qCl8mNQIDAQAB
-----END PUBLIC KEY-----"""
if __name__ == '__main__':
    ca = CA()
    ca.incoming_certificate_request("**********************", user_pub_key)
    ca.incoming_response_verification_code("**********************", input("Enter code:"))
