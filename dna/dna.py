import csv
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python dna.py <database> <dna file>")
        exit(1)

    str_names = []
    subjects_db = []
    with open(sys.argv[1], mode="r") as csvfile:
        reader = csv.DictReader(csvfile)
        str_names = reader.fieldnames[1:]
        for row in reader:
            subjects_db.append(row)

    dna_sequence = ""
    with open(sys.argv[2], mode="r") as textfile:
        dna_sequence = textfile.read().strip()

    subseq_match_results = {subsequence: 0 for subsequence in str_names}
    for subseq in str_names:
        subseq_match_results[subseq] = longest_match(dna_sequence, subseq)

    for subject in subjects_db:
        match = True
        for subseq in str_names:
            if int(subject[subseq]) != subseq_match_results[subseq]:
                match = False
                break
        if match:
            print(subject["name"])
            return
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
