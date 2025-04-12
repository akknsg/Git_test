import dns.resolver

def resolve_dns(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')  # Resolve A record (IPv4)
        for answer in answers:
            print(f"{domain} -> {answer}")
    except Exception as e:
        print(f"Error resolving {domain}: {e}")

resolve_dns("google.com.sg")
resolve_dns("starhub.com.sg")