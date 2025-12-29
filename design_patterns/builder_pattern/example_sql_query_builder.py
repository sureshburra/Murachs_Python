# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 00:05:27 2025

@author: suresh.burra
"""

from typing import List, Optional, Dict, Any

class SQLQuery:
    def __init__(self):
        self.select_fields: List[str] = []
        self.table: Optional[str] = None
        self.joins: List[str] = []
        self.where_conditions: List[str] = []
        self.group_by: List[str] = []
        self.having: Optional[str] = None
        self.order_by: List[str] = []
        self.limit: Optional[int] = None
        self.offset: Optional[int] = None
        
    def to_sql(self) -> str:
        if not self.table:
            raise ValueError("Table must be specified")
            
        fields = ", ".join(self.select_fields) if self.select_fields else "*"
        sql = f"SELECT {fields} FROM {self.table}"
        
        if self.joins:
            sql += " " + " ".join(self.joins)
            
        if self.where_conditions:
            sql += " WHERE " + " AND ".join(self.where_conditions)
            
        if self.group_by:
            sql += " GROUP BY " + ", ".join(self.group_by)
            
        if self.having:
            sql += f" HAVING {self.having}"
            
        if self.order_by:
            sql += " ORDER BY " + ", ".join(self.order_by)
            
        if self.limit:
            sql += f" LIMIT {self.limit}"
            
        if self.offset:
            sql += f" OFFSET {self.offset}"
            
        return sql
    
class SQLQueryBuilder:
    def __init__(self):
        self.query = SQLQuery()
        
    def select(self, *fields: str):
        self.query.select_fields.extend(fields)
        return self
    
    def from_table(self, table: str):
        self.query.table = table
        return self
    
    def join(self, table: str, on: str, join_type: str = "INNER"):
        self.query.joins.append(f"{join_type} JOIN {table} ON {on}")
        return self
    
    def where(self, condition: str):
        self.query.where_conditions.append(condition)
        return self
    
    def group_by(self, *fields: str):
        self.query.group_by.extend(fields)
        return self
    
    def having(self, condition: str):
        self.query.having = condition
        return self
    
    def order_by(self, field: str, direction: str = "ASC"):
        self.query.order_by.append(f"{field} {direction}")
        return self
    
    def limit(self, limit: int):
        self.query.limit = limit
        return self
    
    def offset(self, offset: int):
        self.query.offset = offset
        return self
    
    def build(self) -> str:
        return self.query.to_sql()
    
    
# Usage
query = (SQLQueryBuilder()
         .select("u.id", "u.name", "COUNT(o.id) as order_count")
         .from_table("users u")
         .join("orders o", "u.id = o.user_id", "LEFT")
         .where("u.status = 'active'")
         .where("u.age >= 18")
         .group_by("u.id", "u.name")
         .having("COUNT(o.id) > 5")
         .order_by("order_count", "DESC")
         .limit(10)
         .build()
         )
    
    
print(query)
