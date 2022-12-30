# MariaDB 설정법

### 윈도우 사용시
1. MariaDB 를 설치한 적이 없다면 https://mariadb.org/ 로 이동후 다운받아준다.
2. 블로그, https://kitty-geno.tistory.com/55 에 나와있는대로 기본세팅을 해준다.
3. 프로젝트 세팅으로 이동.

### 맥 사용시

### 프로젝트 세팅
1. `CREATE DATABASE fmp;`
2. `USE fmp;`
3. `CREATE TABLE Pill_Info(id MEDIUMINT(8), Material_Info MEDIUMINT(8), amount VARCHAR(100));`
4. `CREATE TABLE Pill_Specification(id MEDIUMINT(8), name VARCHAR(100), type VARCHAR(100), company VARCHAR(100), consume VARCHAR(100), DIN VARCHAR(100));`
5. `CREATE TABLE Material_Info(id MEDIUMINT(8), name VARCHAR(100));`
6. `INSERT INTO Pill_Info VALUES(1,1,"500 mg");`
7. `INSERT INTO Pill_Info VALUES(1,2,"10 mg");`
8. `INSERT INTO Pill_Info VALUES(1,3,"5 mg");`
9. `INSERT INTO Pill_Info VALUES(2,1,"500 mg");`
10. `INSERT INTO Pill_Info VALUES(3,1,"500 mg");`
11. `INSERT INTO Material_Info VALUES(1, "ACETAMINOPHEN");`
12. `INSERT INTO Material_Info VALUES(2, "DEXTROMETHORPHAN HYDROBROMIDE");`
13. `INSERT INTO Material_Info VALUES(3, "PHENYLEPHRINE HYDROCHLORIDE");`
14. `INSERT INTO Pill_Specification VALUES(1,"EXTRA STRENGTH TYLENOL COLD DAYTIME","Tablet","JOHNSON & JOHNSON INC","Oral","02276186");`
15. `INSERT INTO Pill_Specification VALUES(2,"TYLENOL EXTRA STRENGTH","Tablet","JOHNSON & JOHNSON INC","Oral","00559407");`
16. `INSERT INTO Pill_Specification VALUES(3,"TYLENOL EXTRA STRENGTH","Suspension","JOHNSON & JOHNSON INC","Oral","00559407");`
17. `CREATE USER 'viewer_acc'@'localhost' IDENTIFIED BY 'viewer';`
18. `CREATE USER 'adder_acc'@'localhost' IDENTIFIED BY 'adder';`
19. `CREATE USER 'remover_acc'@'localhost' IDENTIFIED BY 'remover';`
20. `GRANT SELECT ON fmp.* to 'viewer_acc'@'localhost';`
21. `GRANT INSERT ON fmp.* to 'adder_acc'@'localhost';`
22. `GRANT DELETE ON fmp.* to 'remover_acc'@'localhost';`
23. `FLUSH PRIVILEGES;`

를 순서대로 한번 쳐주자. 아니면 아래 코드를 복붙해주자 (추천).

`CREATE DATABASE fmp;
USE fmp;
CREATE TABLE Pill_Info(id MEDIUMINT(8), Material_Info MEDIUMINT(8), amount VARCHAR(100));
CREATE TABLE Pill_Specification(id MEDIUMINT(8), name VARCHAR(100), type VARCHAR(100), company VARCHAR(100), consume VARCHAR(100), DIN VARCHAR(100));
CREATE TABLE Material_Info(id MEDIUMINT(8), name VARCHAR(100));
INSERT INTO Pill_Info VALUES(1,1,"500 mg");
INSERT INTO Pill_Info VALUES(1,2,"10 mg");
INSERT INTO Pill_Info VALUES(1,3,"5 mg");
INSERT INTO Pill_Info VALUES(2,1,"500 mg");
INSERT INTO Pill_Info VALUES(3,1,"500 mg");
INSERT INTO Material_Info VALUES(1, "ACETAMINOPHEN");
INSERT INTO Material_Info VALUES(2, "DEXTROMETHORPHAN HYDROBROMIDE");
INSERT INTO Material_Info VALUES(3, "PHENYLEPHRINE HYDROCHLORIDE");
INSERT INTO Pill_Specification VALUES(1,"EXTRA STRENGTH TYLENOL COLD DAYTIME","Tablet","JOHNSON & JOHNSON INC","Oral","02276186");
INSERT INTO Pill_Specification VALUES(2,"TYLENOL EXTRA STRENGTH","Tablet","JOHNSON & JOHNSON INC","Oral","00559407");
INSERT INTO Pill_Specification VALUES(3,"TYLENOL EXTRA STRENGTH","Suspension","JOHNSON & JOHNSON INC","Oral","00559407");
CREATE USER 'viewer_acc'@'localhost' IDENTIFIED BY 'viewer';
CREATE USER 'adder_acc'@'localhost' IDENTIFIED BY 'adder';
CREATE USER 'remover_acc'@'localhost' IDENTIFIED BY 'remover';
GRANT SELECT ON fmp.* to 'viewer_acc'@'localhost';
GRANT INSERT ON fmp.* to 'adder_acc'@'localhost';
GRANT DELETE ON fmp.* to 'remover_acc'@'localhost';
FLUSH PRIVILEGES;`