# WhiteShark modules package
# Created by: Ankon Polley

from .email_scan import find_emails
from .phone_scan import find_phones

__all__ = ["find_emails", "find_phones"]
