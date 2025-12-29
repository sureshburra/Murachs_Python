# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 18:16:58 2025

@author: suresh.burra
"""

import re
from datetime import datetime
from typing import Optional

class UserProfile:
    def __init__(self):
        self.username: Optional[str] = None
        self.email: Optional[str] = None
        self.first_name: Optional[str] = None
        self.last_name: Optional[str] = None
        self.age: Optional[str] = None
        self.phone: Optional[str] = None
        self.bio: Optional[str] = None
        self.created_at: datetime = datetime.now()
        
    def __str__(self):
        return (f"User: {self.username} ({self.first_name} {self.last_name}),"
                f"Email: {self.email}, Age: {self.age}, Phone: {self.phone}")
    
    
class UserProfileBuilder:
    def __init__(self):
        self.profile = UserProfile()
        
    def set_username(self, username: str):
        if len(username)<3:
            raise ValueError("Username must be at least 3 characters")
        self.profile.username = username
        return self
    
    def set_email(self, email: str):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValueError('Invalid email format')
        self.profile.email = email
        return self
    
    def set_name(self, first_name: str, last_name: str):
        self.profile.first_name = first_name
        self.profile.last_name = last_name
        return self
    
    def set_age(self, age: int):
        if age<13 or age>120:
            raise ValueError("Age must be between 13 and 120")
        self.profile.age = age
        return self
    
    def set_phone(self, phone: str):
        phone_pattern = r'^\+?1?\d{9,15}$'
        if not re.match(phone_pattern, phone):
            raise ValueError("Invalid phone number format")
        self.profile.phone = phone
        return self
    
    def set_bio(self, bio: str):
        if len(bio)>500:
            raise ValueError("Bio must be 500 characters or less")
        self.profile.bio = bio
        return self
    
    def build(self):
        if not self.profile.username:
            raise ValueError("Username is required")
        if not self.profile.email:
            raise ValueError("Emai is required")
        return self.profile
    
    
# Usage
user = (UserProfileBuilder()
        .set_username("john_doe")
        .set_email("john@example.com")
        .set_name("John","Doe")
        .set_age(30)
        .set_phone("+1234567890")
        .set_bio("Software developer and tech enthusiast")
        .build()
        )
        
print(user)