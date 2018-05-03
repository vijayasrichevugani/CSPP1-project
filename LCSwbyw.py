"""Longest Common Substring when computed word by word"""
import os
import string
import time
import datetime
	
class plagiarism(object):

	def __init__(self,path):
		self.path=path

	def plaglcswbyw(self): #LargestCommonSubstring technique for word by word
	
		lst=[p for p in os.listdir(self.path) if p.endswith('.txt')]
		if 'output.txt' in lst:
			lst.remove('output.txt')
		
		matrix=[]
		m=[]
		m.append('Name of file')
		m.extend(lst)
		matrix.append(m)

		for filenamemain in lst:
	
			#file1 being opened to compare
			file1=open(filenamemain, 'r')
			f1=str(file1.read())
			f1.lower()
			lenf1=len(f1)
			f1=(str,f1.split(' '))
			
			matrix2=[]
			matrix2.append(str(filenamemain))
			maxi=0

			for filename in lst:	
		
				if filenamemain==filename:

					percent=None #when same files are compared the plagiarism percentage is 'None'
			
				else:
					
					#file2 being opened to be compared with
					file2=open(filename, 'r')
					f2=str(file2.read())
					f2.lower()
					lenf2=len(f2)
					f2=(str,f2.split(' '))
					
					#to find the length string by string of largest common Substring
					cmax=0
					for temp in range(0,len(f1),1):
						for j in range(0,len(f2),1):
							c=0
							i=temp
							if(f1[i]==f2[j]):
								while i<len(f1) and j<len(f2) and f1[i]==f2[j]:
									c+=len(str(f1[i]))
									i+=1
									j+=1
			
							if(c>cmax):
								cmax=c

					#percentage of plagiarism being calculated
					
					if (lenf1+lenf2)==0:
						
						percent='both files are empty'
					
					elif lenf1==0 or lenf2==0:

						percent=0

					else:
						
						percent=((cmax*200.0)/(lenf1+lenf2))
						percent=round(percent,2)
				
				matrix2.append(str(percent))
			
			matrix.append(matrix2)

			"""Matrix is the fina output of this particular technique containing all the plagiarism percentages when all files are subjected"""

		return (matrix)

def matrix(l):
	col_lens=[]
	for j in range(len(l)):
		maxi=0
		for i in range(len(l)):
			if maxi<len(str(l[i][j])):
				maxi=len(str(l[i][j]))
		col_lens.append(maxi)
	f='\t'.join('{{:{}}}'.format(n) for n in col_lens)
	t=[f.format(*row) for row in l]
	return (t)

def display(mat,path):
	os.chdir(path)
	finalmat=matrix(mat)
	output=open('output.txt','a+')
	for i in finalmat:
		output.write((str(i)))
		output.write('\n')
	output.close()

def main():
	path=raw_input('enter path to check plagiarism for .txt files:\n')
	check=plagiarism(path) #'check' is the object for plagiarism type
	os.chdir(path)
	
	output=open('output.txt','w+')
	output.write(str(datetime.datetime.now()))
	output.write('\n\nPlagiarism check\n')
	output.write('\nAs per LargestCommonSubstring technique when computed word by word:\n\n')	
	output.close()

	output=open('output.txt','a+')
	display(check.plaglcswbyw(),path)
	output.close()

main()