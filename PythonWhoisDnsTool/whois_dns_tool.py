import whois
import dns.resolver

def get_whois_info(domain):
    print("\n[WHOIS Info]")
    try:
        w = whois.whois(domain)
        print(w)
    except Exception as e:
        print(f"Error fetching WHOIS: {e}")

def get_dns_info(domain):
    print("\n[DNS Info]")
    record_types = ['A', 'MX', 'NS']
    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"\n{record} Records:")
            for rdata in answers:
                print(rdata.to_text())
        except Exception as e:
            print(f"Failed to retrieve {record} records: {e}")

if __name__ == "__main__":
    domain = input("Enter domain: ")
    get_whois_info(domain)
    get_dns_info(domain)
