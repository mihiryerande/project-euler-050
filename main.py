# Problem 50:
#     Consecutive Prime Sum
#
# Description:
#     The prime 41, can be written as the sum of six consecutive primes:
#         41 = 2 + 3 + 5 + 7 + 11 + 13
#
#     This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
#     The longest sum of consecutive primes below one-thousand that adds to a prime,
#       contains 21 terms, and is equal to 953.
#
#     Which prime, below one-million, can be written as the sum of the most consecutive primes?

from math import floor, sqrt


def main():
    """
    Returns the longest sequence of consecutive primes
      which itself sums to a prime below one million.

    Returns:
        (List[int]): Longest sequence of consecutive primes
            which itself sums to a prime below `n`
    """
    # Use a sieve to find all primes < 1,000,000
    prime_list = []
    prime_set = set()
    for x in range(2, 10**6):
        # Check whether x is prime
        i = 0
        is_prime = True
        x_mid = floor(sqrt(x)) + 1
        while i < len(prime_list) and prime_list[i] < x_mid:
            p = prime_list[i]
            if x % p == 0:
                is_prime = False
                break
            else:
                i += 1
        if is_prime:
            prime_list.append(x)
            prime_set.add(x)
        else:
            continue
    print('Found {} primes below 1M'.format(len(prime_list)))

    # First figure out the largest possible length of a subseq to stay under 1M
    s = 0
    n_max = 0
    while n_max < len(prime_list) and s < 10**6:
        s += prime_list[n_max]
        n_max += 1
    # n_max shouldn't have maxed out at len(prime_list), but just to make sure
    if s >= 10**6:
        n_max -= 1

    # Consider subsequences of these primes, from longest to shortest
    for n in range(n_max, 0, -1):
        print('Checking subsequences of length {} ...'.format(n))
        for i in range(len(prime_list)-n):
            subseq = prime_list[i:i+n]
            s = sum(subseq)
            if s > 10**6:
                # Don't need to consider further subsequences of length n,
                #   as their sums will be too large
                break
            elif sum(subseq) in prime_set:
                return subseq
            else:
                continue


if __name__ == '__main__':
    consecutive_prime_seq = main()
    print('Sequence of {} primes:'.format(len(consecutive_prime_seq)))
    for consecutive_prime in consecutive_prime_seq:
        print('  {}'.format(consecutive_prime))
    print('Sums to {}'.format(sum(consecutive_prime_seq)))
