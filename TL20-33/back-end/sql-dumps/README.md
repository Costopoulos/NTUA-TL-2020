Προκειμένου να εγκατασταθεί το project πρέπει να γίνουν τα εξής:
(Θεωρείται πως οι εντολές "python" και "pip" ισχύουν στο σύστημα, και αν όχι αντίστοιχα οι "python3" ή "pip3", καθώς και η venv)

Πρέπει να γίνουν:
pip install  
Τα:
	Django                        2.2.12       
	django-cors-headers           3.7.0               
	djangorestframework           3.12.2              
	djangorestframework-csv       2.1.0               
	djangorestframework-simplejwt 4.6.0        
	mysqlconnector                2.2.9       
	mysqlclient                   2.0.3
	PyJWT                         1.7.1
	
(η εντολή τρέχεται μόνο με το όνομα, τα versions που χρησιμοποιήθηκαν είναι ενδεικτικά)
αν χρειαστούν άλλα θα φανεί όταν πάει να τρέξει το σύστημα

Αφού γίνει clone το repo:

source activate στο φάκελο back-end/bin για να ξεκινήσει virtual environment (optional)
create database mydb; (mysql command line)
python manage.py makemigrations (στο φάκελο back-end/src)
python manage.py migrate (στο φάκελο back-end/src)
mysql dump το αρχείο "users_dump.sql" (insert user values)
mysql dump το αρχείο "db_dump.sql" (create all other tables and insert data)
(Ο user γίνεται ξεχωριστά επειδή χρησιμοποιείται η κλάση AbstractUser του django, και γίνεται το mix με το custom μοντέλο μας)

python manage.py runserver 8765 (όσο βρίσκεται στο αρχείο back-end/src για να τρέξει ο server στο port 8765 - πιθανά σφάλματα αφορούν την pip install εντολή)

Χρειάζεται να μπορεί να οριστεί η εντολή "ev_group33" του node.js globally στον υπολογιστή
Πρέπει να γίνει install το Angular με όλα τα πακέτα που χρειάζεται (εδώ έχω παραθέσει μόνο τα πακέτα του django)
Το αρχείο charging_dump.csv στο φάκελο sql-dumps είναι ένα dump της βάσης σε csv


