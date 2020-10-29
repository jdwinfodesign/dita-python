endswith.py
	Not especially useful. Uses shutil and os.walk() to iterate over files in a tree. Uses filepath.endswith() to find XML or DITA files by their extension. I think ".endswith" is a string method which I suppose you can call on "filepath" because it is a string. 

fixDoctype.py
	For a set of XML files, it replaces the DOCTYPE with one of your choosing. It is pretty crude right now, about on the level of running the old DITA-OT from the command line, but it does the job and isn't used frequently enough to justify more time to refine it right now.
	It prompts you for absolute paths to the source and output folders, and you have to provide the information types and the doctype declaration to replace it. These have to be hardcoded in the Python file. Despite its limitations, it does exactly what I wanted it to do, and you can specify DITA and XML files to include, and file types to ignore, which can save time and effort.

getChildrenOnly.py
	This is an especially slick little bit of code, thanks to the use of pathlib and glob, which saves so much time and effort. In its current form, it prints out only the child directories of the current wording directory. To dig further down the tree, you adjust a single argument.
		for a in p.glob('*'):
			if a.is_dir():
				print(a)
	Change '*' to '*/*' or some variation thereof and it digs deeper in the tree. 

getElements.py
	This one is fun. It uses os.walk() to walk all files in a tree (should try pathlib and glob some time), then uses etree to parse each file and etree.iter() to print each element.tag in the file. 
	TODO: Count and sort for file and total. 

getRoots.py
	This is the daddy of getElements.py. It uses os.walk() to walk all files in a tree (should try pathlib and glob some time), the prints the root, filepath, and file extension of each file.

pathlibPlay.py
See getChildrenOnly.py. I think this was just a learning exercise that didn't get deleted.

walkPlay.py
	Demonstrates use of the Python os.walk() method and its arguments on a directory tree. Quoting the documentation: "For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames)."
	----------------------------------------
		dirpath:  C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\walkTestShort\A
	   dirnames:  ['AA']
	  filenames:  ['1.dita']
	----------------------------------------
	You can list single directories and files, but needs work. I think pathlib might be better.
