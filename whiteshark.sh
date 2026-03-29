#!/bin/bash

# WhiteShark - Mobile/Email OSINT Extraction Tool
# Author: Authorized Pentester
# Usage: ./whiteshark.sh -e email@example.com OR ./whiteshark.sh -m +1234567890

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

banner() {
    echo -e "${BLUE}"
    echo "██╗  ██╗ █████╗ ███╗   ███╗███████╗     ██████╗ ██████╗ ███╗   ███╗███████╗"
    echo "██║  ██║██╔══██╗████╗ ████║██╔════╝    ██╔════╝██╔═══██╗████╗ ████║██╔════╝"
    echo "███████║███████║██╔████╔██║███████╗    ██║     ██║   ██║██╔████╔██║█████╗  "
    echo "██╔══██║██╔══██║██║╚██╔╝██║╚════██║    ██║     ██║   ██║██║╚██╔╝██║██╔══╝  "
    echo "██║  ██║██║  ██║██║ ╚═╝ ██║███████║    ╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗"
    echo "╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝"
    echo -e "${NC}"
    echo -e "${YELLOW}Mobile/Email OSINT Extraction Tool${NC}\n"
    echo -e "${GREEN}Created by: Ankon Polley${NC}\n"
}

usage() {
    echo "Usage: $0 [OPTIONS]"
    echo "Options:"
    echo "  -e, --email    Extract mobile from email"
    echo "  -m, --mobile   Extract email/social from mobile"
    echo "  -h, --help     Show this help"
    exit 1
}

extract_from_email() {
    local email=$1
    echo -e "${GREEN}[+] Extracting mobile numbers from: $email${NC}"
    python3 extractor.py --email "$email"
}

extract_from_mobile() {
    local mobile=$1
    echo -e "${GREEN}[+] Extracting emails and social profiles from: $mobile${NC}"
    python3 extractor.py --mobile "$mobile"
    echo -e "${GREEN}[+] Searching social media...${NC}"
    python3 social_finder.py --mobile "$mobile"
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -e|--email)
            EMAIL="$2"
            extract_from_email "$EMAIL"
            shift 2
            ;;
        -m|--mobile)
            MOBILE="$2"
            extract_from_mobile "$MOBILE"
            shift 2
            ;;
        -h|--help)
            usage
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            usage
            ;;
    esac
done

if [[ -z "$EMAIL" && -z "$MOBILE" ]]; then
    banner
    usage
fi

