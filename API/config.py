viewer = {'id': 'viewer_acc', 'pw': 'viewer'}
admin = {'id': 'root', 'pw': 'root'}
DB = {'host': 'localhost', 'port': 3306, 'db_name': 'FMP'}
table = {'pill': 'test', 'ingredient': "element"}
table_info = {'pill-ingredient': 'Pill_Info', 'pill-name-type': 'Pill_Specification', 'ingredient': 'Material_Info'}
columns_info = {'Pill Info': {'id': 'mediumint(8)', 'Material Info': 'mediumint(8)', 'amount': 'varchar(100)'},
                'Pill Specification': {'id': 'mediumint(8)', 'name': 'varchar(100)', 'type': 'varchar(100)',
                                       'company': 'varchar(100)', 'consume': 'varchar(100)', 'DIN': 'varchar(100)'},
                'Material Info': {'id': 'mediumint(8)', 'name': 'varchar(100)'}}
max_pill_cache = 5
max_el_cache = 5
