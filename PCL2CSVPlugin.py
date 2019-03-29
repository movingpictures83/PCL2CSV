import sys
import numpy

import PyPluMA

class PCL2CSVPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      firstline = filestuff.readline()
      secondline = filestuff.readline()
      self.abundances = []
      self.genes = []
      first = True
      for line in filestuff:
         contents = line.split()
         self.genes.append(contents[0])
         pos = 0
         for j in range(3, len(contents)):
            if (first):
               self.abundances.append([])
            value = float(contents[j])
            self.abundances[pos].append(value)
            pos += 1
            #abund.append(value)
         if (first):
            first = False
         #self.abundances.append(abund)

   def output(self, filename):
      #csvfilename = self.myfile[0:len(self.myfile)-3] + "csv"
      csvfile = open(filename, 'w')
      PyPluMA.log("Writing CSV file ")

      # First Line
      csvfile.write("\"\",")
      for gene in self.genes:
         csvfile.write(gene)
         if (gene != self.genes[len(self.genes)-1]):
            csvfile.write(",")
         else:
            csvfile.write("\n")

      # Rest of Samples
      for abund in self.abundances:
         csvfile.write("\""+self.myfile[0:len(self.myfile)-3]+"\",")
         i = 0
         for value in abund:
             csvfile.write(str(value / sum(abund)))
             i += 1
             if (i == len(abund)):
                csvfile.write("\n")
             else:
                csvfile.write(",")


