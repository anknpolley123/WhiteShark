#!/usr/bin/env python3
import re
import requests
import argparse
import sys
from urllib.parse import urlparse, parse_qs
import json

class WhiteSharkExtractor:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def extract_mobile_from_email(self, email):
        """Extract mobile numbers associated with email via common OSINT sources"""
        mobiles = set()
        
        # Pattern matching for mobile numbers (international formats)
        mobile_patterns = [
            r'\+?[\d\s\-\(\)]{10,15}',  # General international
            r'\+1[\d\s\-\(\)]{10,}',    # US/Canada
            r'\+44[\d\s\-\(\)]{10,}',   # UK
            r'\+91[\d\s\-\(\)]{10,}',   # India
        ]
        
        # 1. Check haveibeenpwned-like data leaks (simplified)
        try:
            # Simulate breach data lookup
            response = self.session.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}", 
                                      headers={'hibp-api-key': 'demo'})
            if response.status_code == 200:
                data = response.json()
                for breach in data:
                    # Extract phones from breach data (hypothetical structure)
                    if 'phones' in breach:
                        for phone in breach['phones']:
                            mobiles.add(phone)
        except:
            pass
        
        # 2. Email pattern analysis from common leak formats
        leak_patterns = [
            rf'{email}[^\w]*([\d\+\-\s\(\)]{{10,15}})',
            rf'([\d\+\-\s\(\)]{{10,15}})[^\w]*{email}',
        ]
        
        print(f"[+] Found {len(mobiles)} mobile numbers")
        for mobile in mobiles:
            print(f"  📱 {mobile}")
    
    def extract_email_from_mobile(self, mobile):
        """Extract emails associated with mobile number"""
        emails = set()
        
        # Common email patterns linked to mobile
        email_patterns = [
            r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        ]
        
        # 1. Reverse phone lookup via public APIs
        apis = [
            f"https://api.fullcontact.com/v3/person.enrich.json?phone={mobile.replace('+', '')}",
            f"https://numverify.com/api/json/{mobile}?accessKey=demo",
        ]
        
        for api in apis:
            try:
                resp = self.session.get(api)
                if resp.status_code == 200:
                    data = resp.json()
                    if 'emails' in data:
                        for email in data['emails']:
                            emails.add(email)
            except:
                pass
        
        print(f"[+] Found {len(emails)} emails")
        for email in emails:
            print(f"  ✉️  {email}")

def main():
    parser = argparse.ArgumentParser(description='WhiteShark Extractor')
    parser.add_argument('--email', help='Email to extract mobile from')
    parser.add_argument('--mobile', help='Mobile to extract email/social from')
    args = parser.parse_args()
    
    extractor = WhiteSharkExtractor()
    
    if args.email:
        extractor.extract_mobile_from_email(args.email)
    elif args.mobile:
        extractor.extract_email_from_mobile(args.mobile)
    else:
        print("[-] Provide --email or --mobile")
        sys.exit(1)

if __name__ == "__main__":
    main()
