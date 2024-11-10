import hashlib

def simple_sha256_hash(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

input_string = "It is without a doubt something cool!"
hashed_value = simple_sha256_hash(input_string)
print(f"The SHA-256 hash of '{input_string}' is: {hashed_value}")

                                      