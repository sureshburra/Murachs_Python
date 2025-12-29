class SQLQueryBuilder:
    def __init__(self, table):
        self._table = table
        self._columns = ["*"]
        self._conditions = []
        self._order_by = None
        self._limit = None

    def select(self, *columns):
        if columns:
            self._columns = list(columns)
        return self

    def where(self, condition):
        self._conditions.append(condition)
        return self

    def order_by(self, column, descending=False):
        self._order_by = (column, descending)
        return self

    def limit(self, n):
        self._limit = n
        return self

    def build(self):
        query = f"SELECT {', '.join(self._columns)} FROM {self._table}"

        if self._conditions:
            query += f" WHERE {' AND '.join(self._conditions)}"

        if self._order_by:
            query += f" ORDER BY {self._order_by[0]} \
            {'DESC' if self._order_by[1] else 'ASC'}"

        if self._limit:
            query += f" LIMIT {self._limit}"

        return query


# Usage
sql = (
    SQLQueryBuilder("users")
    .select("id", "username", "email")
    .where("age>=18")
    .where("country = 'IN'")
    .order_by("created_at", descending=True)
    .limit(100)
    .build()
)

print(sql)
