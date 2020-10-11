"""
Author: Vl4d
Description: RSA Cracker
"""

mini_ascii_table = ['0', 'A', 'E', 'G', 'I', 'O', 'R', 'T', 'X', '!']
cypher_text = 'ITG!AAEXEX IRRG!IGRXI OIXGEREAGO'

def return_factors(num):
    """Returns prime factors of num, assuming num's only factors are
    1, p, q, num, where p, q are prime
    """
    p = 3; q = None
    while True:
        if num % p == 0:
            q = int(num/p)
            break
        else:
            p += 2  # increment by 2 since p can never be even...
    return (p,q)  # return prime factors

def cypher_to_num(text):
    """Return number from cypher text based on mini ascii table
    """
    num = 0
    for ch in text:
        dig = mini_ascii_table.index(ch)
        num = (num*10) + dig
    return num

def num_to_text(num):
    """Convert decrypted number to text based on ascii table
    """
    text = ''
    while num != 0:
        text += mini_ascii_table[num%10]
        num = int(num/10)
    return "".join(reversed(text))  # return reversed string


# 1. Convert cypher text to number.
words_to_decrypt = []

for word in cypher_text.split():
    num = cypher_to_num(word)
    words_to_decrypt.append(num)
    print("word: {0}\nto_num_and_back: {1}".format(word, num_to_text(num)))
    print(words_to_decrypt[-1])

# 2. Determine private key of the encryptor
n = 10539750919; e = 49  # public key = (e=49, n=10,539,750,919)
p, q = return_factors(n)  # determine prime factors of n

# compute d such that ed % (p-1)(q-1) == 1; starting d is simply n
d = n; mod = (p-1)*(q-1)
while True:
    result = (e*d) % mod
    if result == 1:
        print("Found d : {0}".format(d))
        break
    else:
        # Update d intelligently. First, calculate diff between mod and result
        diff = abs(result - mod)
        # we want to add x to d such that (e*d) % mod == diff + 1; thus (diff+1)/e is approximately
        # how much we want to update d by. This might not be an integer, since we're not guaranteed
        # there exists such an x, so cast as an integer and continue looping
        d += int((diff/e) + 1)

# 3. Decrypt each number
message = []
for num_to_decrypt in words_to_decrypt:
    # cypher_text ^ private_key mod n ... i.e. (num_to_decrypt ^ d) % n
    decrypted_num = pow(num_to_decrypt, d, n)
    message.append(num_to_text(decrypted_num))

print("Decrypted Message: {0}".format(" ".join(message)))
    
# ANSWER
answer = 'RSA Owned!'