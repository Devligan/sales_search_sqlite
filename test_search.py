import unittest
from search import Search

class Testing(unittest.TestCase):
    
    def test_department_total(self):
        search = Search()
        tests = {
            "Electronics": 25233.68,
            "Tools": 26047.24,
            "Computers": 24817.93,
            "Clothing": 26733.61,
            "Baby": 25163.75,
            "Automotive": 24489.48
        }
        for key in tests:
            self.assertAlmostEqual(tests[key], search.department_total(key), msg="department_total(" + key + ") incorrect", delta=0.01)

    def test_department_total_bydate(self):
        search = Search()
        tests = []
        tests.append(("Electronics", '2020-09-15', 1114.69))
        tests.append(('Baby', '2020-09-01', 811.20))
        tests.append(('Music', '2020-09-30', 0))
        tests.append(('Jewelery', '2020-09-12', 1034.1))
        tests.append(('NotADepartment', '2020-09-25', 0))
        tests.append(('Computers', '2020-10-01', 0))
        tests.append(('Garden', '2020-08-31', 0))
        for test in tests:
            actual = search.department_total_bydate(test[0], test[1])
            if actual == None:
                actual = 0
            self.assertAlmostEqual(test[2], actual, msg="department_total_bydate('" + test[0] + "', '" + test[1] + "') incorrect", delta=0.01)

    def test_country_count_date_range(self):
        search = Search()
        tests = []
        tests.append(('Russia', '2020-09-15', '2020-09-17', 3673.99))
        tests.append(('Ukraine', '2020-09-01' , '2020-09-15', 4195.61))
        tests.append(('Finland', '2020-08-31', '2020-09-25', 1275.57))
        tests.append(('Macedonia', '2020-09-20', '2020-09-20', 31.69))
        tests.append(('Stroudonia', '2020-09-10', '2020-09-15', 0))
        tests.append(('Brazil', '2020-08-15', '2020-08-25', 0))
        tests.append(('France', '2020-10-01', '2020-10-15', 0))
        for test in tests:
            actual = search.country_count_date_range(test[0], test[1], test[2])
            if actual == None:
                actual = 0
            self.assertAlmostEqual(test[3], actual, msg="country_count_date_range('" + test[0] + "', '" + test[1] + "', '" + test[2] + "') incorrect", delta=0.01)

    def test_biggest_spender(self):
        search = Search()
        self.assertEqual(('Remus', "O' Scallan"), search.biggest_spender(), msg="biggest_spender() incorrect")

    def test_biggest_spenders(self):
        search = Search()
        tests = []
        tests.append((10, 'Baby', [('Hedwig', 'Ivoshin', 248.1), ('Ellyn', 'Reddihough', 226.59), ('Sterne', 'Gutteridge', 199.36), ('Aurthur', 'Want', 192.54), ('Liv', 'Vasnev', 191.32), ('Germaine', 'Whistlecraft', 190.33), ('Mathew', 'MacMorland', 184.46), ('Swen', 'Pride', 172.91), ('Augy', 'Chataignier', 172.40), ('Shaughn', 'Godwyn', 166.99)]))
        tests.append((1, 'Shoes', [('Jammal', 'Strood', 239.43)]))
        tests.append((5, 'Health', [('Stanleigh', 'Symson', 272.18), ('Dael', 'Spadari', 249.77), ('Land', 'Sparway', 214.61), ('Ashlan', 'Hatter', 174.25), ('Harriett', 'Izhaky', 170.79)]))
        tests.append((25, 'Kids', [('Rudolph', 'Aldous', 369.31), ('Jaime', 'Scarf', 248.12), ('Cristine', 'Moscone', 223.0), ('Shirlene', 'Kingcote', 217.22), ('Bari', 'Barraclough', 212.47), ('Gran', 'Bentzen', 189.83), ('Torre', 'McQuarter', 186.92), ('Kalila', 'Somes', 184.04), ('Nicolette', 'Dudley', 174.0), ('Sidoney', 'Bes', 165.13), ('Hieronymus', 'Ashpital', 163.17), ('Ax', 'Eannetta', 158.66), ('Lowrance', 'Prentice', 157.49), ('Jeannette', 'Merrigans', 146.97), ('Stefano', 'McKeggie', 144.52), ('Germain', 'Stiebler', 144.04), ('Harri', 'Mathiasen', 142.42), ('Benedetto', 'Choupin', 141.72), ('Euphemia', 'Waldocke', 137.92), ('Domenico', 'Marley', 136.87), ('Sanderson', 'Bartholomaus', 134.43), ('Maisie', 'Hawkshaw', 133.26), ('Tiffanie', 'Djorevic', 133.12), ('Johannes', 'Astell', 132.61), ('Oralie', 'Lambert', 131.38)]))
        tests.append((12, 'Movies', [('Ermengarde', 'Streatley', 230.57), ('Ly', 'Wallege', 212.79), ('Jenna', 'Punch', 174.93), ('Ferdinanda', 'Daltrey', 171.51), ('Efren', 'Pauletto', 168.75), ('Hussein', 'Leith', 160.53), ('Angel', 'Aharoni', 158.63), ('Eran', 'McEntee', 157.9), ('Florina', 'Baradel', 148.92), ('Larry', 'Worsell', 148.63), ('Ferdie', 'Perel', 148.34), ('Martita', 'Shawdforth', 147.73)]))
        tests.append((100, 'Tools', [('Hesther', 'Velte', 226.57), ('Lyndsey', 'Woltering', 216.05), ('Caresa', 'Brodeau', 192.01), ('Yalonda', 'Ranking', 188.86), ('Ambrosio', 'Bonnick', 186.22), ('Sara', 'Glasspool', 184.62), ('Judd',
'Drexel', 180.14), ('Izabel', 'Huckett', 168.58), ('Felike', 'Ludovici', 163.97), ('Dalila', 'Uttermare', 160.69), ('Anselma', 'Johnes', 157.33), ('Carolina', 'Howchin', 156.92), ('Codee', 'Hryniewicki', 156.62), ('Lucille', 'Prium', 156.55), ('Cindra', 'Chable', 155.5), ('Fanni', 'Kesterton', 155.4), ('Euphemia', 'Peasnone', 154.26), ('Maddalena', 'Brumfitt', 150.89), ('Nicola', 'Kincaid', 149.51), ('Leon', 'Point', 146.78), ('Rollie', 'Briance', 146.46), ('Callie', 'Wattam', 146.05), ('Sinclare', 'Lyenyng', 142.11), ('Wanda', 'Udall', 141.64), ('Brittney', 'Doram', 141.62), ('Toby', 'Dooher', 140.71), ('Kendra', 'Moreing', 139.08), ('Vickie', 'Cathee', 137.77), ('Amil', 'Kennaway', 137.72), ('Gill', 'Matejka', 136.08), ('Jaimie', 'Perez', 135.44), ('Valentino', 'McVeagh', 134.37), ('Heinrick', 'Lamb', 132.37), ('Carie', 'Normanville', 129.25), ('Jae', 'Kamall', 126.34), ('Laurella', 'Fumagalli', 126.29), ('Konrad', 'Keele', 126.15), ('Wynne', 'Snowball', 125.17), ('Jaquith', 'Loosemore',
124.03), ('Giulia', 'Lammertz', 122.91), ('Retha', 'Durbann', 121.97), ('Natasha', 'Crosskill', 121.53), ('Reeba', 'Bahde', 121.01), ('Domenico', 'Tilt', 118.61), ('Hanson', 'Moniker', 117.47), ('Verine', 'Woltering', 117.3), ('Charis', 'Davydychev', 116.92), ('Ingaborg', 'Kenwell', 116.62), ('Starr', 'Cressar', 116.05), ('Bernie', 'Vasyaev', 114.94), ('Lezley', 'Scalera', 113.45), ('Arabelle', 'Rodd', 113.13), ('Bambi', 'Danels', 111.27), ('Norry', 'Batchelar', 110.16), ('Nelli', 'Lukasik', 110.1), ('Harland', 'Lickess', 108.86), ('Trista', 'Etherson', 107.6), ('Carlin', 'Blowick', 103.56), ('Efren', 'Pauletto', 103.42), ('Lauren', 'Lettice', 102.74), ('Lauren', 'Karlolczak', 100.89), ('Lonny', 'Stedman', 100.64), ('Lombard', 'Aspall', 99.73), ('Graig', 'Novic', 99.5), ('Birk', 'Clere', 99.48), ('Chandler', 'Perrone', 99.37), ('Yance', 'Ashenhurst', 99.24), ('Florri', 'Negal', 99.04), ('Moshe', 'Gerrans', 98.73), ('Pen', 'Briggdale', 98.69), ('Lotti', 'Le Sieur', 98.46), ('Portie', 'Cleland', 98.13), ('Humberto', 'Corradi', 97.93), ('Katerine', 'Arger', 97.85), ('Ashlan', 'Hatter', 97.79), ('Engracia', 'Mc Andrew', 96.9), ('Margarethe', 'Dunbleton', 96.65), ('Clementius', 'Sapsed', 96.17), ('Wheeler', 'Karolowski', 95.97), ('Ilene', 'Gracewood', 95.75), ('Paulette', 'Escalera', 95.65), ('Loise', 'Wisden', 95.63), ('Domenico', 'Marley', 95.16), ('Harri', 'Mathiasen', 95.03), ('Florance', 'Jeaves', 94.6), ('Candace', 'Fennelly', 94.5), ('Kalila', 'Somes', 94.43), ('Cassandry', 'Iacovino', 93.69), ('Linet', 'Llywarch', 93.69), ('Zebadiah', 'Lanham', 93.4), ('Farra', 'Petrovic', 93.4), ('Martin', 'Pinchen', 93.21), ('Bobby', 'Trank', 92.84), ('Matilde', 'Briscow', 92.69), ('Ab', 'Standage', 92.61), ('Averil', 'Waddilove', 92.61), ('Clarinda', 'Isacq', 92.61), ('Kelsey', 'Whitechurch', 92.47), ('Petr', 'Proffer', 92.25), ('Frannie', 'Iddy', 91.85)]))
        tests.append((50, 'Not A Department', []))

        for test in tests:
            actual = search.biggest_spenders(test[0], test[1])    
            rounded_actual = []
            for a in actual:
                rounded_actual.append((a[0], a[1], round(a[2], 2)))         
            self.assertEqual(test[2], rounded_actual, msg="biggest_spenders(" + str(test[0]) + ", '" + test[1] + "') incorrect'")

if __name__ == '__main__':
    unittest.main()