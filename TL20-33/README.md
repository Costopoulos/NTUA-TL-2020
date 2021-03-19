# Σχολή Ηλεκτρολόγων Μηχανικών & Μηχανικών Η/Υ, ΕΜΠ

Εργασία στο μάθημα Τεχνολογία Λογισμικού - Χειμερινό εξάμηνο 2020

| Επώνυμο             | Όνομα        | Αριθμός Μητρώου |
|---------------------|--------------|-----------------|
| Ζευγολατάκος        | Παναγιώτης   |   3117804       |
| Kωστόπουλος         | Κωνσταντίνος |   3117043       |
| Λαγός               | Γιώργος      |   3117034       |
| Σαραντινόπουλος     | Ευστάθιος    |   3116801       |

## Δομή φακέλων

Η υποχρεωτική κοινή δομή των φακέλων του repository περιγράφεται στο έγγραφο των παραδοτέων (βλ. moodle μαθήματος). 

Η δομή των φακέλων στο συγκεκριμένο παράδειγμα είναι η εξής:

* Στον φάκελο `back-end` περιέχεται ο κώδικας του back-end.
* Στον φάκελο `cli-client` περιέχεται ο κώδικας του command line application.
* Στον φάκελο `front-end` περιέχεται ο κώδικας της front-end web εφαρμογής.
* Στον φάκελο `documentation` περιέχονται οι προδιαγραφές της εφαρμογής.


## Κύριες τεχνολογίες του παραδείγματος


### Back-end

* [Django](https://www.djangoproject.com/)
* [Django rest framework](https://www.django-rest-framework.org/)

### CLI client

* [Node](https://nodejs.org/en/)
* [Commander js](https://www.npmjs.com/package/commander)
* [Axios js](https://www.npmjs.com/package/axios)

### Front-end
* [Angular](https://angular.io/)
* [Angular material](https://material.angular.io/) (theme)
* [NgCharts 2](https://github.com/valor-software/ng2-charts) (graphs)
* [Angular FlexLayout](https://github.com/angular/flex-layout) (styling & layout)

## Oδηγίες



*	Προκειμένου να εγκατασταθεί το project πρέπει να γίνουν τα εξής: (Θεωρείται πως οι εντολές "python" και "pip" ισχύουν στο σύστημα, και αν όχι αντίστοιχα οι "python3" ή "pip3", καθώς και η venv)

*	Για το back-end πρέπει να γίνουν: pip install τα:

	```
	Django 2.2.12
	django-cors-headers 3.7.0
	djangorestframework 3.12.2
	djangorestframework-csv 2.1.0
	djangorestframework-simplejwt 4.6.0
	mysqlconnector 2.2.9
	mysqlclient 2.0.3 PyJWT 1.7.1
	```
	

	(η εντολή τρέχεται μόνο με το όνομα, τα versions που χρησιμοποιήθηκαν είναι ενδεικτικά) αν χρειαστούν άλλα θα φανεί όταν πάει να τρέξει το σύστημα

	Αφού γίνει clone το repo:

	```
	source activate στο φάκελο back-end/bin για να ξεκινήσει virtual environment (optional) 
	create database mydb; (mysql command line) python manage.py makemigrations (στο φάκελο back-end/src) 
	python manage.py migrate (στο φάκελο back-end/src) 
	mysql dump το αρχείο "users_dump.sql" (insert user values) mysql dump το αρχείο "db_dump.sql" (create all other tables and insert data) 
	//(Ο user γίνεται ξεχωριστά επειδή χρησιμοποιείται η κλάση AbstractUser του django, και γίνεται το mix με το custom μοντέλο μας)
	``` 
	
	Η εντολή είναι:
	
	```
	python manage.py runserver 8765 
	```
	(όσο βρίσκεται στο αρχείο back-end/src για να τρέξει ο server στο port 8765 - πιθανά σφάλματα αφορούν την pip install εντολή)

	Χρειάζεται να μπορεί να οριστεί η εντολή "ev_group33" του node.js globally στον υπολογιστή Πρέπει να γίνει install το Angular με όλα τα πακέτα που χρειάζεται
	(εδώ έχω παραθέσει μόνο τα πακέτα του django) 
	Το αρχείο charging_dump.csv στο φάκελο sql-dumps είναι ένα dump της βάσης σε csv



* Το REST API base URL είναι το `http://localhost:8765/evcharge/api`, όπως απαιτείται από την εργασία. 



* Για τo front-end:

	Εγκατάσταση angular cli 
	
	```npm install -g @angular/cli```
	
	```npm update```
	
	Πλοήγηση στον φάκελο του front-end:
	```cd front-end/evcharge```
	
	Εκτέλεση εντολής:
	```ng serve```
	
	Πλέον το front-end μας είναι διαθέσιμο στην διέυθυνση `http://localhost:4200`
