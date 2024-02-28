@echo off 

echo -----------------
echo $$$ No input provided:
python script.py
echo -----------------

echo $$$ Bad file name:
python script.py "examples/non_existent"
echo -----------------

echo $$$ No vars file:
python script.py "examples/no_vars"
echo -----------------

echo $$$ Bad file format:
python script.py "examples/bad_format"
echo -----------------

echo $$$ ALL OK:
python script.py "examples/good"
echo -----------------
