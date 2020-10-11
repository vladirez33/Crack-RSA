# Crack-RSA
Simple RSA Cracking tool
Cracking RSA means finding private key from a public key.
 
This code extracts the components from a public key, performs factoring, and if all is successful, it will build the private key.

RSA is a public key cryptographic system that is widely used for secure data transfer.

What is RSA?
RSA is a public key cryptographic system that is widely used for secure data transfer.
n a public key encryption system, the encryption key is public and different from the decryption key, which is kept secret (private). 
RSA user creates and publishes a public key based on two large prime numbers, along with auxiliary value. The prime numbers are kept secret. 
Messages can be encrypted by anyone, using the public key, but can only be decrypted by someone who knows the prime numbers.

To use this:
First you need to generates a private key using any free tool. Any tool can be used as long as it has an option to create a private key with 2 given prime numbers.
Then, generates the public key using the private key.
After that, get the public key components: modulus and and exponent. 
With only this information, we are supposed to get the private key
Use msieve to factorize n, a big number, Msive is an implementation of the fastest factorization algorithm known today, GNFS.
If successful, we have p and q.
Finally, compares the found key with the original to verify success
