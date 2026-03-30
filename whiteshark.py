import argparse
from modules.email_scan import find_emails
from modules.phone_scan import find_phones

def main():
    parser = argparse.ArgumentParser(description="WhiteShark OSINT Scanner")
    parser.add_argument("-f", "--file", help="Target text file")
    
    args = parser.parse_args()

    if args.file:
        print("[+] Scanning file:", args.file)
        emails = find_emails(args.file)
        phones = find_phones(args.file)

        print("\nEmails Found:")
        for e in emails:
            print(e)

        print("\nPhone Numbers Found:")
        for p in phones:
            print(p)

if __name__ == "__main__":
    main()
