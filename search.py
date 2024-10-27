import sqlite3
class Search:

    _conn = sqlite3.connect('sales.sqlite')

    def department_total(self, dept):
        """
        Returns the sum of all sales within a department
        """
        cursor = self._conn.cursor()
        cursor.execute(f"SELECT SUM(amount) FROM sales WHERE department = ?", (dept,))
        result = cursor.fetchone()[0]
        return result if result else 0

    def department_total_bydate(self, dept, date):
        """
        Returns the sum of all sales within a department on a specific date
        """
        cursor = self._conn.cursor()
        cursor.execute(f"SELECT SUM(amount) FROM sales WHERE department = ? AND sale_date = ?", (dept, date))
        result = cursor.fetchone()[0]
        return result if result else 0

    def country_count_date_range(self, country, start_date, end_date):
        """
        Returns the number of sales to buyers in a specific country between 2 dates, inclusive
        """
        query = f"""
            SELECT SUM(s.amount)
            FROM sales s
            JOIN buyers b ON s.buyer_id = b.id
            WHERE b.country = '{country}' AND s.sale_date BETWEEN '{start_date}' AND '{end_date}'
        """
        result = self._conn.execute(query).fetchone()[0]
        return result if result else 0

    def biggest_spender(self):
        """
        Returns a tuple with the first and last name of the buyer who spent the most money
        """
        cursor = self._conn.cursor()
        cursor.execute("SELECT buyers.first_name, buyers.last_name, SUM(sales.amount) as total FROM sales JOIN buyers ON sales.buyer_id = buyers.id GROUP BY buyers.id ORDER BY total DESC LIMIT 1")
        result = cursor.fetchone()
        return result[:2]

    def biggest_spenders(self, how_many, department):
        """
        Returns the how_many highest spenders in a specific department
        """
        cursor = self._conn.cursor()
        cursor.execute(f"SELECT b.first_name, b.last_name, SUM(s.amount) FROM sales s JOIN buyers b ON s.buyer_id = b.id WHERE s.department = ? GROUP BY s.buyer_id ORDER BY SUM(s.amount) DESC LIMIT ?", (department, how_many))
        result = cursor.fetchall()
        return result if result else []