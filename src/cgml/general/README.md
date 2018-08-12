### Bloom filter 
Space-efficient probabilistic data structure that is used to test whether an element is a member of a set. 
For example, checking availability of username is set membership problem, where the set is the list of all 
registered username. The price we pay for efficiency is that it is probabilistic in nature that means, 
there might be some False Positive results. False positive means, it might tell that given username is already 
taken but actually it’s not.

Probability of false positive (type I error): P = (1 - (1 - 1/m)^kn)^k 
- where m size of bit array, k number of hash functions
Probability of false negative (type II error): P = 0

If n known, then m = -n*ln(P) / (ln 2)^2
Optimal number of hash functions: k = m/n * ln2

##### Space efficiency 
- O(m) - don't need actual values of a set to be stored
##### Hash function
- The hash function used in bloom filters should be independent and uniformly distributed. 
They should be fast as possible. Fast simple non cryptographic hashes which are independent enough include murmur, 
FNV series of hash functions and Jenkins hashes. Generating hash is major operation in bloom filters. 
Cryptographic hash functions provide stability and guarantee but are expensive in calculation. 
With increase in number of hash functions k, bloom filter become slow. 
All though non-cryptographic hash functions do not provide guarantee but provide major performance improvement.
