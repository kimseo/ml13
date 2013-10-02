ml13
====
* save data as file
	python ./main.py -f <filename>

* load data from file
	python ./main.py -l <filename>

* set data count as 20 ((5 + 5) + (5 + 5)) default is 5
	python ./main.py -c 5

* apply kernel
	python ./main.py -k linear
	python ./main.py -k poly
	python ./main.py -k radial
	python ./main.py -k sigmoid

* apply slack and kernel
	python ./main.py -k linear -s 1
	python ./main.py -k poly -s 1
	python ./main.py -k radial -s 1
	python ./main.py -k sigmoid -s 1

* apply slack and kernel from file
	python ./main.py -k linear -s 1 -l <filename>

