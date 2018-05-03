import os
import string
import time
import datetime
	
class plagiarism(object):

	def __init__(self,path):
		self.path=path

	def magnitude(self,dic): #to calculate the magnitude as in vectors
		k=0
		for x in dic:
			k+=dic[x]*dic[x]
		return k

	def wordfreq(self,l): #will return a dictionary containing all unique keys in the file along with correspnding frequency.
		dic={}
		for i in range(len(l)):
			c=0
			for j in range(len(l)):
				if(l[i]==l[j]):
					c+=1
			dic[l[i]]=c
		if '' in dic:
			del dic['']
		return dic

	def fileset(self,f): #will set the file, i.e., removes all the punctuations and special characters
		f=f.lower()
		f=f.replace('\n',' ')
		f=f.split(' ')
		f=[word.strip(string.punctuation)for word in f]
		return f

	def plagbow(self): #BagOfWords technique
		
		lst=[p for p in os.listdir(self.path) if p.endswith('.txt')]
		if 'output.txt' in lst:
			lst.remove('output.txt')
		
		matrix=[]
		m=[]
		m.append('Name of the file')
		m.extend(lst)
		matrix.append(m)

		for filenamemain in lst:
	
			#file1 being opened to compare
			file1=open(filenamemain, 'r')
			f1=str(file1.read())
			f1=self.fileset(f1)

			matrix2=[]
			matrix2.append(str(filenamemain))

			for filename in lst:	
			
				""" 
				for 
				s= Dot Product(Frequency of file1, Frequency of file2)
				f1mag= magnitude of f1 = |f1|
				f2mag= magnitude of f2 = |f2|
				percent= the plagirism percentage when f1 is compared with f2
				"""
				
				if filenamemain==filename:

					percent=None #when same files are compared the plagiarism percentage is 'None'
				
				else:

					#file2 being opened to be compared with
					file2=open(filename, 'r')
					f2=str(file2.read())
					f2=self.fileset(f2)

					dic1=self.wordfreq(f1)
					dic2=self.wordfreq(f2)

					"""Dot product calculation"""
					s=0
					for x in dic1:
						for y in dic2:
							if(x==y):
								s+=dic1[x]*dic2[y]

					"""Magnitude calculation"""
					f1mag=self.magnitude(dic1)
					f2mag=self.magnitude(dic2)


					"""Percentage calculation"""
					
					if f1mag==0 or f2mag==0:
						percent=0
					else:
						percent=(s*100.0)/((f1mag**0.5)*(f2mag**0.5))
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
	output.write('\nAs per BagOfWords technique:\n\n')	
	output.close()
	
	output=open('output.txt','a+')
	display(check.plagbow(),path)
	output.close()

main()