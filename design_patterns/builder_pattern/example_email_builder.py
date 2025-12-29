# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 08:03:46 2025

@author: suresh.burra
"""
from typing import List, Optional
from dataclasses import dataclass
from enum import Enum

class EmailPriority(Enum):
    LOW = "Low"
    NORMAL = "Normal"
    HIGH = "High"
    

@dataclass
class Attachment:
    filename: str
    content: bytes
    content_type: str
    
    
class Email:
    def __init__(self):
        self.sender: Optional[str] = None
        self.recipients: List[str] = []
        self.cc: List[str] = []
        self.bcc: List[str] = []
        self.subject: Optional[str] = None
        self.body: Optional[str] = None
        self.html_body: Optional[str] = None
        self.attachments: List[Attachment] = []
        self.priority: EmailPriority = EmailPriority.NORMAL
        self.reply_to: Optional[str] = None
        
        
    def __str__(self):
        return (f"Email:\n"
                f"From: {self.sender}\n"
                f"To: {', '.join(self.recipients)}\n"
                f"CC: {', '.join(self.cc)}\n"
                f"Subject: {self.subject}\n"
                f"Priority: {self.priority.value}\n"
                f"Attachments: {len(self.attachments)}"
                )
    
    
class EmailBuilder:
    def __init__(self):
        self.email = Email()
        
    def from_address(self, sender: str):
        if "@" not in sender:
            raise ValueError("Invalid sender email address")
        self.email.sender = sender
        return self
    
    def to(self, *recipients: str):
        for recipient in recipients:
            if "@" not in recipient:
                raise ValueError(f"Invalid recipient email: {recipient}")
        self.email.recipients.extend(recipients)
        return self
    
    def cc(self, *recipients: str):
        self.email.cc.extend(recipients)
        return self
    
    def bcc(self, *recipients: str):
        self.email.bcc.extend(recipients)
        return self
    
    def subject(self, subject: str):
        self.email.subject = subject
        return self
    
    def body(self, body: str):
        self.email.body = body
        return self
    
    def html_body(self, html: str):
        self.email.html_body = html
        return self
    
    def attach(self, filename: str, content: bytes, content_type: str):
        attachment = Attachment(filename, content, content_type)
        self.email.attachments.append(attachment)
        return self
    
    def priority(self, priority: EmailPriority):
        self.email.priority = priority
        return self
    
    def reply_to(self, reply_to: str):
        self.email.reply_to = reply_to
        return self
    
    def build(self):
        if not self.email.sender:
            raise ValueError("Sender email is required")
        if not self.email.recipients:
            raise ValueError("At least one recipient is required")
        if not self.email.subject:
            raise ValueError("Subject is required")
        if not self.email.body and not self.email.html_body:
            raise ValueError("Email body is required")
        return self.email
    
    
# Usage
email = (EmailBuilder()
         .from_address("sender@example.com")
         .to("recipient1@example.com","recipient2@example.com")
         .cc("cc@example.com")
         .subject("Important Update")
         .body("This is the email body")
         .priority(EmailPriority.HIGH)
         .attach("report.pdf", b"PDF Content", "application/pdf")
         .build()         
         )

print(email)