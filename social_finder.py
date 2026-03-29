#!/usr/bin/env python3
import requests
import re
import argparse
import sys
from urllib.parse import quote

class SocialShark:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def find_social_profiles(self, mobile):
        """Discover social media profiles linked to mobile number"""
        profiles = {}
        
        # Social media search patterns
        platforms = {
            'facebook': f'"{mobile}" site:facebook.com',
            'instagram': f'"{mobile}" site:instagram.com',
            'linkedin': f'"{mobile}" site:linkedin.com',
            'twitter': f'"{mobile}" site:twitter.com OR site:x.com',
            'tiktok': f'"{mobile}" site:tiktok.com',
        }
        
        print(f"[+] Searching {len(platforms)} social platforms...")
        
        for platform, query in platforms.items():
            try:
                # Google dork style search
                search_url = f"https://www.google.com/search?q={quote(query)}"
                resp = self.session.get(search_url)
                
                # Extract profile URLs (simplified regex)
                profile_links = re.findall(r'https?://(?:www\.)?[^\/]+{}.*?(?="| )'.format(platform.replace('.', r'\.'), resp.text), re.IGNORECASE)
                
                if profile_links:
                    profiles[platform] = profile_links[:3]  # Top 3 results
                
            except Exception as e:
                continue
        
        self.print_results(profiles, mobile)
    
    def print_results(self, profiles, mobile):
        if profiles:
            print(f"\n[+] Found {sum(len(v) for v in profiles.values())} social profiles for {mobile}")
            for platform, links in profiles.items():
                print(f"\n  🌐 {platform.upper()}:")
                for link in links:
                    print(f"     → {link}")
        else:
            print("[-] No social profiles found")

def main():
    parser = argparse.ArgumentParser(description='WhiteShark Social Finder')
    parser.add_argument('--mobile', required=True, help='Mobile number to search')
    args = parser.parse_args()
    
    shark = SocialShark()
    shark.find_social_profiles(args.mobile)

if __name__ == "__main__":
    main()
