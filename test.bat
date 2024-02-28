@echo off 

echo -----------------
echo $$$ No input provided:
python script.py "" debug
echo -----------------

echo $$$ Bad file name:
python script.py "examples/non_existent" debug
echo -----------------

echo $$$ No vars file:
python script.py "examples/no_vars" debug
echo -----------------

echo $$$ Bad file format:
python script.py "examples/bad_format" debug
echo -----------------

echo $$$ ALL OK:
python script.py "examples/good" debug
echo -----------------
