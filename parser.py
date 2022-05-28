import os 
import datetime
import sys
def parser():
	file_name = sys.argv[1]
	if "Log" in file_name:
		print_name = file_name.split("Log")
		print_name = print_name[1].split(".")
		print_name = print_name[0]
	else:
		print_name = file_name.split(".")
		print_name = print_name[0]
	file =  open(file_name)
	lines = file.readlines()
	j = 0
	format = '%H:%M%p'
	t = "00:00pm"
	ttt = " "
	total_time = datetime.timedelta()	
	for i in lines:
		if "Time Log:" in i:
			pass
		temp = i.split("-")
		j +=1
		try:
			check1 = str(temp[0])
			check2 = str(temp[1])
		except Exception:
			pass
		try:
			if ('am' in check1 or 'pm' in check1 or 'Am' in check1 or 'aM' in check1 or 'pM' in check1 or 'Pm' in check1 or 'PM' in check1 or 'AM' in check1 ) and ('am' in check2 or 'pm' in check2 or 'Am' in check2 or 'aM' in check2 or 'pM' in check2 or 'Pm' in check2 or 'PM' in check2 or 'AM' in check2):
				t1 = check1.split(": ")
				#print(t1)
				if len(t1) < 2:
					t1 = t1[0]

					t1 = str(t1)
					if ("Pm" in t1 ):
						t1 = t1.replace("Pm","pm")
					elif ("pM" in t1):
						t1 = t1.replace("pM","pm")
					elif ("Am" in t1):
						t1 = t1.replace("Am","am")
					elif ("aM" in t1):
						t1 = t1.replace("aM","am")
					elif ("AM" in t1):
						t1 = t1.replace("AM","am")
					elif ("PM" in t1):
						t1 = t1.replace("PM","pm")


					t1=t1.strip()

					

				else:
					t1 = t1[1]

					t1 = str(t1)
					if ("Pm" in t1 ):
						t1 = t1.replace("Pm","pm")
					elif ("pM" in t1):
						t1 = t1.replace("pM","pm")
					elif ("Am" in t1):
						t1 = t1.replace("Am","am")
					elif ("aM" in t1):
						t1 = t1.replace("aM","am")
					elif ("AM" in t1):
						t1 = t1.replace("AM","am")
					elif ("PM" in t1):
						t1 = t1.replace("PM","pm")

					t1 = t1.strip()

			


				t2 = check2.split(" ")
				#t2 = t2[1]
				if t2 [1] == 'getting':
					t2 = t2[0]
				else:
					t2 = t2[1]
				t2 = str(t2)
				if ("Pm" in t2 ):
					t2 = t2.replace("Pm","pm")
				elif ("pM" in t2):
					t2 = t2.replace("pM","pm")
				elif ("Am" in t2):
					t2 = t2.replace("Am","am")
				elif ("aM" in t2):
					t2 = t2.replace("aM","am")
				elif ("AM" in t2):
					t2 = t2.replace("AM","am")
				elif ("PM" in t2):
					t2 = t2.replace("PM","pm")

				t2 = t2.strip()
		

				format = '%I:%M%p'

				# if '13' in t2:
				# 	t2 = t2.replace("13","1")


				a = datetime.datetime.strptime(t1,format)
				b = datetime.datetime.strptime(t2,format)
				
				temp = b-a
				tempp = str(temp)
				if "-1 day" in tempp:
					singletemp = tempp.replace("-1 day, ","")
				else:
					singletemp = tempp
				(hr, mn, se) = singletemp.split(':')
				d = datetime.timedelta(hours=int(hr), minutes=int(mn), seconds=int(se))
				total_time += d
				final_time = '%02d:%02d:%02d.%06d' % (total_time.days*24 + total_time.seconds // 3600, (total_time.seconds % 3600) // 60, total_time.seconds % 60, total_time.microseconds)
				ttt = final_time.split(":")[0] + " hours " + final_time.split(":")[1] + " minutes"
				#print(ttt)
		except Exception:
				print("Error at line", j)
	print(print_name,':', ttt)


if __name__ == '__main__':
	parser()

