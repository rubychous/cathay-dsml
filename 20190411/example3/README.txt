0. pip install cython
1. Put all the module .py files to the lib folder
2. Put the mainPy.py to the same directory of the lib folder
   e.g., 
   example3 (folder)
     |___ mainPy.py
     |___ compile.py 
     |___ lib (folder)
           |___ expPy.py
           |___ sqrtPy.py
           |___ timeSeries.py

3. Modify the extension script in compile.py 

4. Run: python3 compile.py build_ext --inplace
   this step will generate .so files; remember to delete all the .c files
5. Run: mkdir -p proj1/lib
5. Put mainPy.xxx.so into proj1/
6. Put the rest of the .so files into proj1/lib/
7. Put your pivot.py to the same directory of the mainPy.xxx.so
   Note that the pivot.py is to call the mainPy.xxx.so
   e.g., 
   proj1 (folder)
     |___ mainPy.xxx.so 
     |___ pivot.py
     |___ lib (folder)
           |___ expPy.so
           |___ sqrtPy.so
           |___ timeSeries.so


   