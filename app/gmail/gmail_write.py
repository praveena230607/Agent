import os
import re
import urllib.parse

KEYWORDS={
  "gmail", "email", "e-mail", "mail",
  "write an email", "send an email", "draft an email",
  "compose an email", "write mail", "send mail", "draft mal",
  "compose mail"
}
def is_email_command(text):
  text=text.lower()
  return any(k in text for k in KEYWORDS)
  def extract_email(text):
    match = re.search(r"[\w.+-]+@[\w.-]+\.\w+",text)
    if match:
      return match.group(0)
      match = re.send
    
  def create_gmail_url(subjects="", body="", recipent=""):
  params = urllib.parse.urlencode({
    "view": "cm",
    "fs": "1",
    "to": recipient,
    "su": subject,
    "body": body
  })
  return f"https://mail.google.com/mail/u/0/?{params}"
