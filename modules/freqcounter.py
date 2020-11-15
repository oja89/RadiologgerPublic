###module to find frequencies

def get_freqs(sentencelists):

    freq_dict = {}

    for sentences in sentencelists:
        for words in sentences:
            if words in freq_dict:
                freq_dict[words] += 1
            else:
                freq_dict[words] = 1

    return freq_dict