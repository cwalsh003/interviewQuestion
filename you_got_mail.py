import csv
import re
from collections import OrderedDict

email_pattern = re.compile(r'^([a-zA-Z0-9_\-\.]+)@{1}([a-zA-Z0-9_\-\.]+)\.([a-zA-Z0-9_\-\.]+)$')
domain_pattern = re.compile(r'(@{1}[a-zA-Z0-9_\-\.]+\.{1}[a-zA-Z0-9_\-\.]+){1}')


def send_it(num_of_addresses, unique_addresses, num_of_valid_addresses, domain_counts):

    print("Number of Records in File: ", num_of_addresses - 1)
    print("Number of Unique Email addresses: ", len(unique_addresses))
    print("Number of valid Email addresses: ", num_of_valid_addresses)
    print("Domain\t\t\t\t\tCount")
    for domain in domain_counts:

        print('{0:10} ==> {1:10d}'.format(domain, domain_counts[domain]))


def reader_and_parse():
    domain_counts = OrderedDict()
    email_addresses = csv.reader(open('sample_data.csv', newline=''), delimiter=',', quotechar='|')
    unique_addresses = set()
    num_of_addresses = 0
    num_of_valid_addresses = 0
    for row in email_addresses:
        num_of_addresses += 1
        email_address = row[0]
        unique_addresses.add(email_address)
        if check_if_valid(email_address):
            num_of_valid_addresses += 1
            domain_counts = get_domain(email_address, domain_counts)
    send_it(num_of_addresses, unique_addresses, num_of_valid_addresses, domain_counts)



def check_if_valid(email):
    return email_pattern.match(email)
def get_domain(email, domain_counts):
    domain = domain_pattern.findall(email)
    key = ""
    for tuples in domain:

        if tuples.lower() in domain_counts:
            domain_counts[tuples.lower()] += 1
        else:
            domain_counts[tuples.lower()] = 1
    return  OrderedDict(sorted(domain_counts.items(), key=lambda t: t[1], reverse=True))
    # print(domain_counts)
if __name__ == '__main__':
    reader_and_parse()
